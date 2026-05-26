#!/usr/bin/env python3
"""AI News Daily Fetcher - 抓取AI领域最新新闻"""

import feedparser
from datetime import datetime
import json
import os

# AI新闻源 RSS
FEEDS = {
    "Hacker News - AI": "https://hnrss.org/newest?q=ai+machine+learning&count=10",
    "Hacker News - LLM": "https://hnrss.org/newest?q=llm+gpt+transformer&count=10",
    "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
    "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/",
    "Ars Technica AI": "https://arstechnica.com/tag/ai/feed/",
}

def fetch_news():
    all_news = []
    
    for feed_name, url in FEEDS.items():
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:
                news_item = {
                    "title": entry.title,
                    "link": entry.link,
                    "source": feed_name,
                    "published": entry.get("published", ""),
                    "summary": entry.get("summary", "")[:200] if entry.get("summary") else "",
                }
                all_news.append(news_item)
        except Exception as e:
            print(f"[WARN] Failed to fetch {feed_name}: {e}")
    
    return all_news

def format_output(news_list):
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    print(f"🤖 AI News Daily | {today}")
    print("=" * 60)
    print()
    
    # 按来源分组
    by_source = {}
    for item in news_list:
        source = item["source"]
        if source not in by_source:
            by_source[source] = []
        by_source[source].append(item)
    
    for source, items in by_source.items():
        print(f"📡 {source}")
        print("-" * 40)
        for i, item in enumerate(items[:3], 1):
            print(f"  {i}. {item['title']}")
            if item["summary"]:
                # 清理HTML标签
                import re
                summary = re.sub(r'<[^>]+>', '', item["summary"])
                if len(summary) > 150:
                    summary = summary[:150] + "..."
                print(f"     {summary}")
            print(f"     🔗 {item['link']}")
            print()
    
    print("=" * 60)
    print(f"📊 共获取 {len(news_list)} 条新闻")
    print(f"💡 建议: 关注 Hugging Face、OpenAI、Google DeepMind 等官方博客获取更深度内容")

if __name__ == "__main__":
    news = fetch_news()
    if news:
        # 输出JSON文件（可用于webhook推送）
        output_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(output_dir, "news.json"), "w", encoding="utf-8") as f:
            json.dump(news, f, ensure_ascii=False, indent=2)
        
        # 输出控制台可读格式
        format_output(news)
    else:
        print("❌ 未获取到任何新闻，请检查网络或RSS源")
