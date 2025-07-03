# 📡 9M2PJU APRS Thursday Check-in Bot

A lightweight, fully-automated **APRS bot** that checks in to the global [#APRSThursday](https://aprsph.net/aprsthursday/) net every **Thursday**. Built with Python and packaged in Docker for effortless deployment.

---

## 🚀 Features

- ⏰ Sends **weekly check-in** message to `ANSRVR` at the correct time
- 🌐 Connects to APRS-IS server (`aprs.hamradio.my:14580`)
- 🐍 Written in pure **Python** using `aprslib` and `schedule`
- 🐳 **Dockerized** for consistent, cross-platform use
- 🔌 **Manual test mode** to trigger messages instantly
- 🧠 Designed for **low-resource systems** (e.g. Raspberry Pi)
- 📦 Works out-of-the-box with **zero cron or systemd setup**

---

## 📨 What It Sends

This bot sends an APRS message to `ANSRVR` in the correct format:

```
CQ HOTG Hello from 9M2PJU-4 APRS Bot
```

This message checks into the [#APRSThursday](https://aprsph.net/aprsthursday/) net, which promotes APRS usage worldwide.

---

## 🛠 Requirements

- Docker & Docker Compose
- APRS-IS credentials (callsign + passcode)

---

## 📦 Quick Start

### 1. Clone this repo

```bash
git clone git@github.com:9M2PJU/APRS-Thursday-Check-in-Bot-Dockerized.git
cd APRS-Thursday-Check-in-Bot-Dockerized
```

### 2. Build the Docker image

```bash
docker compose build
```

### 3. Start the bot

```bash
docker compose up -d
```

The container will now run 24/7 and send a message every Thursday at 9PM (MYT).

---

## 🧪 Test the Bot Manually

You can run it instantly using:

```bash
docker compose run --rm aprs-bot python aprs_bot.py --test
```

This immediately sends the APRS message for testing purposes.

---

## 🛑 Stop the Bot

```bash
docker compose down
```

---

## 🔒 Configuration

To update callsign, passcode, or message, edit the `aprs_bot.py` file:

```python
CALLSIGN = "CALLSIGN"
PASSCODE = "YOURPASSCODE"
SERVER = "aprs.hamradio.my"
PORT = 14580
DEST = "ANSRVR"
MESSAGE = "CQ HOTG Hello from CALLSIGN"
```

---

## 📚 Learn More

- [APRS Thursday Net – aprs.org](https://aprsph.net/aprsthursday/)
- [APRS-IS Server Network](http://www.aprs-is.net/)
- [Passcode Generator](https://pass.hamradio.my/)

---

## 🧑‍💻 Author

Created by [9M2PJU](https://github.com/9M2PJU) 🇲🇾  
Licensed under MIT

---

## ❤️ Support the APRS Community

This bot helps promote message-based APRS activity and participation in [#APRSThursday](https://aprsph.net/aprsthursday/).  

