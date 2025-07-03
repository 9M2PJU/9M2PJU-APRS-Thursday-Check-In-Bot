# 📡 9M2PJU APRS Thursday Check-in Bot

A lightweight, fully-automated **APRS bot** that checks in to the global [#APRSThursday](https://aprsph.net/aprsthursday/) net every **Thursday at 9:00 PM Malaysia Time (MYT)**. Built with Python and packaged in Docker with built-in cron for zero-hassle weekly operation.

---

## 🚀 Features

- ⏰ Sends **weekly check-in** message on **Thursdays at 9PM MYT**
- 🌐 Connects to APRS-IS (`aprs.hamradio.my:14580`)
- 🐍 Written in pure **Python** using `aprslib` and `pytz`
- 🐳 **Dockerized with cron** – runs standalone, no host `cron` or `systemd` required
- 🔌 **Manual test mode** for instant triggering (`--test`)
- 🧠 Lightweight, ideal for low-resource systems (e.g. Raspberry Pi, VPS)
- 📤 Contributes to the [#APRSThursday](https://aprsph.net/aprsthursday/) global net

---

## 📨 What It Sends

This bot sends the following APRS message to `ANSRVR`:

```
CQ HOTG Hello from CALLSIGN
```

This checks into the [#APRSThursday](https://aprsph.net/aprsthursday/) net, encouraging global participation in APRS messaging.

---

## 🛠 Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- APRS-IS credentials:
  - Your **callsign** (e.g. `9M2PJU`)
  - Your **passcode** (see [Passcode Generator](https://pass.hamradio.my/))

---

## 📦 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/9M2PJU/9M2PJU-APRS-Thursday-Check-In-Bot.git
cd 9M2PJU-APRS-Thursday-Check-In-Bot
```

### 2. Edit your configuration

Open `aprs_bot.py` and update the following variables:

```python
CALLSIGN = "YOUR_CALLSIGN"
PASSCODE = "YOUR_PASSCODE"
MESSAGE  = "CQ HOTG Hello from YOUR_CALLSIGN"
```

### 3. Build the Docker image

```bash
docker compose build
```

### 4. Start the bot container

```bash
docker compose up -d
```

The bot will now run continuously and auto-send your check-in every Thursday at **9:00 PM MYT**.

---

## 🧪 Manual Test Mode

To send the APRS message immediately (for testing), run:

```bash
docker compose run --rm aprs-bot python /app/aprs_bot.py --test
```

---

## 🛑 Stop the Bot

```bash
docker compose down
```

---

## 🔧 Configuration Notes

- To change the message or server details, edit `aprs_bot.py`.
- Log output is stored in `./log/cron.log` by default.

---

## 📚 Resources

- 🌍 [APRS Thursday Info](https://aprsph.net/aprsthursday/)
- 🌐 [APRS-IS Network](http://www.aprs-is.net/)
- 🔑 [Passcode Generator](https://pass.hamradio.my/)

---

## 🧑‍💻 Author

Created and maintained by [9M2PJU](https://github.com/9M2PJU) 🇲🇾  
Licensed under the [MIT License](https://opensource.org/licenses/MIT)

---

## ❤️ Support the APRS Community

This bot supports the global [#APRSThursday](https://aprsph.net/aprsthursday/) initiative to encourage APRS message-based activity every week.
