---
title: "네이버 블로그 글 목록"
layout: single
permalink: /naver-blog/
author_profile: true
toc: false
share: false
related: false
excerpt: "비바마켓 · Beaten by the Market 네이버 블로그에 올린 글 전체 목록입니다. IPO 증권신고서, 지분공시, 시장 데이터 분석 글을 모았습니다."
---

새 글은 **네이버 블로그 [비바마켓 · Beaten by the Market](https://blog.naver.com/beatenbythemarket)**{: style="color: #4682B4;"}에 올리고 있습니다. 이 목록은 네이버 블로그 RSS로 자동으로 갱신됩니다.

<style>
.naver-posts { list-style: none; margin: 1.5em 0 0; padding: 0; }
.naver-posts li { margin: 0 0 1.4em; padding: 0 0 1.2em; border-bottom: 1px solid #eee; }
.naver-posts .meta { font-size: 0.75em; color: #777; margin: 0 0 0.2em; }
.naver-posts .meta .cat { margin-left: 0.6em; color: #4682B4; }
.naver-posts .title { font-size: 1em; font-weight: bold; margin: 0 0 0.3em; }
.naver-posts .excerpt { font-size: 0.8em; color: #555; margin: 0; }
</style>

{% assign naver_posts = site.data.naver_posts %}
<p>총 <strong>{{ naver_posts | size }}</strong>편 · 최신순</p>

<ol class="naver-posts">
{% for post in naver_posts %}
  <li>
    <p class="meta">{% if post.date %}<time datetime="{{ post.date }}">{{ post.date | date: "%Y-%m-%d" }}</time>{% endif %}{% if post.category %}<span class="cat">{{ post.category | escape }}</span>{% endif %}</p>
    <p class="title"><a href="{{ post.url | escape }}">{{ post.title | escape }}</a></p>
    {% if post.excerpt != "" %}<p class="excerpt">{{ post.excerpt | escape }}</p>{% endif %}
  </li>
{% endfor %}
</ol>
