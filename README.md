# chetam-rss-parser 🔄🎙️

Python-скрипт для парсинга RSS подкаста «Чё там новости» и автогенерации JSON-файла с эпизодами.  

🖥️ Продакшн-версия работает на приватном VPS и GitHub Actions (бот доступен 24/7).  
🔒 В репозитории — витрина: код, requirements, README и CI (без секретов).  
🌐 Используется на официальном сайте подкаста: [chetamnovosti.ru](https://chetamnovosti.ru)

---

## Функции
- Парсинг RSS-ленты подкаста  
- Генерация `episodes.json` (с метаданными выпусков)  
- Автозапуск по расписанию через GitHub Actions (cron)  
- Публикация JSON на GitHub Pages → используется сайтом и ботами  

## Технологии
Python · feedparser · GitHub Actions · JSON · cron  

---

## Demo
- JSON feed: [episodes.json](https://pepstrik.github.io/chetam-rss-parser/episodes.json)  
- Интеграция на сайте: [chetamnovosti.ru](https://chetamnovosti.ru)  
- Используется в: [CheTamNovostiBot](https://github.com/pepstrik/CheTamNovostiBot)

---

![CI](https://github.com/pepstrik/chetam-rss-parser/actions/workflows/ci.yml/badge.svg)  
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

> English version: [README_EN.md](README_EN.md)
