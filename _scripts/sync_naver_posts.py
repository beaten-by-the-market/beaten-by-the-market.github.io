"""네이버 블로그 RSS를 읽어 _data/naver_posts.json에 글 목록을 누적합니다.

Jekyll 페이지(_pages/naver-blog.md)가 이 파일을 읽어 글 링크 목록을 만듭니다.
네이버 블로그 홈은 noindex,nofollow라서 구글이 홈에서 글로 넘어가지 못합니다.
이 블로그에 글 링크를 모아 두면 구글이 여기서 글을 발견할 수 있습니다.

글마다 소개 페이지 _naver/<글번호>.md(주소 /naver-blog/<글번호>/)도 만듭니다.
- 머리말(제목·날짜·카테고리·원문 주소·요약)은 실행할 때마다 다시 씁니다.
- 본문(소개글)은 사람이 쓰며, 스크립트는 처음 만들 때만 RSS 발췌를 넣고 이후로는 건드리지 않습니다.
- 머리말의 excerpt(검색 설명문)는 본문 첫 단락에서 뽑습니다.
아직 소개글이 없는 페이지는 `grep -l "자동 발췌" _naver/`로 찾을 수 있습니다.

사용법:
    python _scripts/sync_naver_posts.py           # RSS 수집 후 변경 시 저장
    python _scripts/sync_naver_posts.py --check   # 저장하지 않고 결과만 출력
    python _scripts/sync_naver_posts.py --pages-only  # RSS 없이 소개 페이지 머리말만 갱신

종료 코드는 성공 시 0, RSS 오류 시 1입니다. 변경 여부는 출력의 changed=로 알립니다.
Python 표준 라이브러리만 사용합니다.
"""

import argparse
from datetime import timedelta, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import parse_qs, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

BLOG_ID = "beatenbythemarket"
RSS_URL = f"https://rss.blog.naver.com/{BLOG_ID}.xml"
ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "_data" / "naver_posts.json"
PAGES_DIR = ROOT / "_naver"
AUTO_MARK = "<!-- 자동 발췌: 소개글을 쓰면 이 줄을 지워 주세요. -->"
PAGE_NOTICE = "# 이 머리말은 _scripts/sync_naver_posts.py가 매번 다시 씁니다. 소개글은 아래 본문에만 쓰세요."
EXCERPT_LENGTH = 150
DESCRIPTION_LENGTH = 160
MAX_FEED_BYTES = 5_000_000
KST = timezone(timedelta(hours=9))


class PlainText(HTMLParser):
    """RSS 본문 HTML에서 스크립트·스타일을 뺀 텍스트만 꺼냅니다."""

    ignored = {"script", "style", "iframe", "object", "template", "noscript"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.ignored:
            self.hidden += 1
        self.parts.append(" ")

    def handle_endtag(self, tag):
        if tag in self.ignored and self.hidden:
            self.hidden -= 1
        self.parts.append(" ")

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def truncate(text, length):
    if len(text) <= length:
        return text
    return text[:length - 1].rstrip() + "…"


def make_excerpt(description):
    if not description:
        return ""
    parser = PlainText()
    parser.feed(description)
    parser.close()
    return truncate(" ".join("".join(parser.parts).split()), EXCERPT_LENGTH)


def post_url(link):
    """PC·모바일·PostView 주소를 m.blog.naver.com/<ID>/<글번호>로 통일합니다.

    모바일 주소는 리다이렉트 없이 본문을 바로 돌려주고 index,follow로 열려 있습니다.
    """
    parts = urlsplit(link)
    if parts.scheme not in ("http", "https") or parts.hostname not in ("blog.naver.com", "m.blog.naver.com"):
        raise ValueError(f"Not a Naver Blog URL: {link}")
    match = re.fullmatch(r"/([A-Za-z0-9_-]+)/(\d+)/?", parts.path)
    if match:
        owner, number = match.groups()
    elif parts.path == "/PostView.naver":
        query = parse_qs(parts.query)
        owner = query.get("blogId", [""])[0]
        number = query.get("logNo", [""])[0]
    else:
        raise ValueError(f"Unrecognized post URL: {link}")
    if owner != BLOG_ID or not number.isdigit():
        raise ValueError(f"Post does not belong to {BLOG_ID}: {link}")
    return f"https://m.blog.naver.com/{owner}/{number}"


def parse_date(value):
    try:
        dt = parsedate_to_datetime(value)
    except (TypeError, ValueError, IndexError):
        return None
    if dt.tzinfo is None:
        return None
    return dt.astimezone(KST).isoformat()


def parse_feed(raw):
    if len(raw) > MAX_FEED_BYTES:
        raise ValueError("RSS exceeds size limit")
    probe = raw.replace(b"\x00", b"").upper()
    if b"<!DOCTYPE" in probe or b"<!ENTITY" in probe:
        raise ValueError("DTD/entity declarations are not allowed")
    root = ET.fromstring(raw)
    channel = root.find("channel")
    if root.tag != "rss" or channel is None:
        raise ValueError("Expected an RSS channel")
    posts = []
    for item in channel.findall("item"):
        title = (item.findtext("title") or "").strip()
        try:
            url = post_url((item.findtext("link") or "").strip())
        except ValueError as error:
            print(f"Warning: skipped item: {error}", file=sys.stderr)
            continue
        if not title:
            continue
        posts.append({
            "title": title,
            "url": url,
            "date": parse_date(item.findtext("pubDate")),
            "category": (item.findtext("category") or "").strip() or None,
            "excerpt": make_excerpt(item.findtext("description")),
        })
    return posts


def sort_posts(posts):
    return sorted(posts, key=lambda p: (p["date"] or "", p["url"]), reverse=True)


def merge(existing, incoming):
    """기존 글은 보존하고(RSS에서 빠져도 유지), RSS에 있는 글은 최신 정보로 갱신합니다."""
    merged = {post["url"]: dict(post) for post in existing}
    for post in incoming:
        old = merged.get(post["url"], {})
        merged[post["url"]] = {
            "title": post["title"],
            "url": post["url"],
            "date": old.get("date") or post["date"],
            "category": post["category"] or old.get("category"),
            "excerpt": post["excerpt"] or old.get("excerpt", ""),
        }
    return sort_posts(merged.values())


def split_page(text):
    """소개 페이지 파일을 (머리말, 본문)으로 나눕니다. 머리말이 없으면 전체가 본문입니다."""
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[4:end], text[end + 5:]
    return "", text


def describe(body):
    """본문 첫 단락을 검색 설명문(excerpt)으로 쓸 평문으로 바꿉니다. 제목·목록·인용·표는 건너뜁니다."""
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block or re.match(r"(#|>|\||[-*+]\s|\d+\.\s)", block):
            continue
        text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", block)
        text = re.sub(r"\*\*|__|`|<[^>]+>", "", text)
        return truncate(" ".join(text.split()), DESCRIPTION_LENGTH)
    return ""


def yaml_string(value):
    # JSON 문자열은 YAML 큰따옴표 문자열로도 그대로 읽힙니다.
    return json.dumps(value, ensure_ascii=False)


def render_page(post, body):
    lines = ["---", PAGE_NOTICE, f"title: {yaml_string(post['title'])}"]
    if post["date"]:
        lines.append(f"date: {post['date']}")
    lines.append(f"naver_url: {yaml_string(post['url'])}")
    if post["category"]:
        lines.append(f"naver_category: {yaml_string(post['category'])}")
    lines.append(f"excerpt: {yaml_string(describe(body))}")
    lines.append("---")
    return "\n".join(lines) + "\n" + body


def sync_pages(posts, write):
    """글마다 _naver/<글번호>.md를 만들거나 머리말을 갱신합니다. 바뀐 파일 수를 돌려줍니다."""
    changed = 0
    for post in posts:
        path = PAGES_DIR / f"{post['url'].rsplit('/', 1)[1]}.md"
        if path.exists():
            old = path.read_text(encoding="utf-8")
            _, body = split_page(old)
        else:
            old = None
            body = f"{post['excerpt']}\n\n{AUTO_MARK}\n" if post["excerpt"] else f"{AUTO_MARK}\n"
        body = body.lstrip("\n")
        if not body.endswith("\n"):
            body += "\n"
        content = render_page(post, body)
        if content != old:
            changed += 1
            if write:
                PAGES_DIR.mkdir(exist_ok=True)
                path.write_text(content, encoding="utf-8", newline="\n")
    return changed


def fetch(url):
    request = Request(url, headers={"User-Agent": "beaten-by-the-market.github.io RSS sync"})
    with urlopen(request, timeout=30) as response:
        return response.read(MAX_FEED_BYTES + 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="저장하지 않고 결과만 출력")
    parser.add_argument("--pages-only", action="store_true", help="RSS 없이 소개 페이지 머리말만 갱신")
    args = parser.parse_args()

    existing = json.loads(DATA_PATH.read_text(encoding="utf-8")) if DATA_PATH.exists() else []
    if args.pages_only:
        pages_changed = sync_pages(existing, write=not args.check)
        print(f"posts={len(existing)} pages_changed={pages_changed} changed={str(pages_changed > 0).lower()}")
        return 0

    incoming = parse_feed(fetch(RSS_URL))
    if not incoming:
        # 일시적 오류로 빈 RSS가 오면 기존 목록을 덮어쓰지 않습니다.
        print("Error: RSS contains zero usable posts; keeping existing data", file=sys.stderr)
        return 1

    posts = merge(existing, incoming)
    content = json.dumps(posts, ensure_ascii=False, indent=2) + "\n"
    data_changed = not DATA_PATH.exists() or DATA_PATH.read_text(encoding="utf-8") != content
    if data_changed and not args.check:
        DATA_PATH.write_text(content, encoding="utf-8", newline="\n")
    pages_changed = sync_pages(posts, write=not args.check)
    changed = data_changed or pages_changed > 0
    print(f"posts={len(posts)} rss_items={len(incoming)} pages_changed={pages_changed} changed={str(changed).lower()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
