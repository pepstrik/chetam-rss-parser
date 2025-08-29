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

## Возможные улучшения 

- Добавить больше метаданных из RSS (например: `duration`, `image`, `guid`).  
- Сохранять даты выпусков в формате ISO-8601 (UTC) для более точной сортировки.  
- Сделать атомарную запись файла (`episodes.json`) с защитой от перезаписи при сетевых сбоях.  
- Добавить простые тесты в CI (валидность JSON, обязательные поля).  
- Настроить мониторинг ошибок при парсинге (логирование, алерты).

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
