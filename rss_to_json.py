import feedparser
import json
from datetime import datetime
import re

# Скачиваем RSS
rss_url = "https://st.zvuk.com/r/c8908758-89a7-431e-90bf-bb0f4c80bc97/rss.xml"
feed = feedparser.parse(rss_url)

# Словарь для хранения всех слов
all_words = []

# Проходим по всем эпизодам и собираем слова из названий и описаний
for entry in feed.entries:
    # Сбор слов из названия
    title = entry.get('title', '')
    words_from_title = re.findall(r'\w+', title.lower())  # разбиваем текст на слова, приводим к нижнему регистру
    all_words.extend(words_from_title)

    # Сбор слов из описания
    description = entry.get('summary', '')
    words_from_description = re.findall(r'\w+', description.lower())
    all_words.extend(words_from_description)

# Используем Counter для подсчёта частоты слов
from collections import Counter
word_counts = Counter(all_words)

# Сортируем по частоте и выводим самые популярные слова
common_words = word_counts.most_common(50)  # Топ-50 самых частых слов
for word, count in common_words:
    print(f"{word}: {count}")

# Парсим RSS и создаём список эпизодов
episodes_data = []
for entry in feed.entries:
    pub_date = entry.get('published', '')
    try:
        year = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z").year
    except Exception:
        year = None

    # Добавляем данные в эпизоды без тегов
    episodes_data.append({
        "name": entry.title,
        "desc": entry.get('summary', ''),
        "link": entry.link,
        "year": year
    })

# Сохраняем данные в JSON
with open("episodes.json", "w", encoding="utf-8") as f:
    json.dump(episodes_data, f, ensure_ascii=False, indent=2)
