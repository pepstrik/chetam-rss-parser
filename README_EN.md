# chetam-rss-parser 🔄🎙️

Python script for parsing the *Che Tam Novosti* podcast RSS feed and auto-generating a JSON file with episodes.  

🖥️ The production version runs on a private VPS and GitHub Actions (24/7 uptime).  
🔒 This repository is a portfolio showcase: it contains code, requirements, README, and CI (no secrets).  
🌐 Deployed and used on the official podcast website: [chetamnovosti.ru](https://chetamnovosti.ru)

---

## Features
- Parse the podcast RSS feed  
- Generate `episodes.json` with episode metadata  
- Schedule automatic updates via GitHub Actions (cron)  
- Publish JSON to GitHub Pages → consumed by the website and bots  

## Tech Stack
Python · feedparser · GitHub Actions · JSON · cron  

---

## Demo
- JSON feed: [episodes.json](https://pepstrik.github.io/chetam-rss-parser/episodes.json)  
- Website integration: [chetamnovosti.ru](https://chetamnovosti.ru)  
- Used in: [CheTamNovostiBot](https://github.com/pepstrik/CheTamNovostiBot)

> Версия на русском: [README.md](README.md)
