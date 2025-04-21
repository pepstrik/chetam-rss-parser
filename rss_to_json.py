import feedparser
import json

RSS_URL = "https://st.zvuk.com/r/c8908758-89a7-431e-90bf-bb0f4c80bc97/rss.xml"
feed = feedparser.parse(RSS_URL)

episodes = []
for entry in feed.entries:
    episodes.append({
        "name": entry.title,
        "desc": entry.get("summary", ""),
        "link": entry.link
    })

with open("episodes.json", "w", encoding="utf-8") as f:
    json.dump(episodes, f, ensure_ascii=False, indent=2)