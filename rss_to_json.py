from datetime import datetime
import feedparser
import json
import re

# Скачиваем RSS
rss_url = "https://st.zvuk.com/r/c8908758-89a7-431e-90bf-bb0f4c80bc97/rss.xml"
feed = feedparser.parse(rss_url)

# Парсим RSS и создаём список эпизодов
episodes_data = []
for entry in feed.entries:
    pub_date = entry.get('published', '')
    year = None

    # Проверяем, есть ли год в поле 'published' и правильно его извлекаем с использованием регулярных выражений
    if pub_date:
        # Применяем регулярное выражение для извлечения года
        match = re.search(r'(\d{4})', pub_date)
        if match:
            year = match.group(1)
        else:
            # Если год не удалось извлечь, используем текущий
            year = datetime.now().year

    episodes_data.append({
        "name": entry.title,
        "desc": entry.get('summary', ''),
        "link": entry.link,
        "year": year,  # Добавляем год
    })

# Сохраняем данные в JSON
with open("episodes.json", "w", encoding="utf-8") as f:
    json.dump(episodes_data, f, ensure_ascii=False, indent=2)
