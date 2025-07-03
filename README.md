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

## 🌍 What is #APRSThursday?

**#APRSThursday** is a weekly global net for [APRS](https://en.wikipedia.org/wiki/Automatic_Packet_Reporting_System) users. It happens every **Thursday from 0000Z to 2359Z** (the whole day in UTC time). The goal is to encourage hams to send APRS messages and have some fun.

---

## ✅ How to Join

You join by sending a message to **ANSRVR** (an APRS messaging group server).

### 📤 Send this message *once* on Thursday:
```
CQ HOTG Your message here
```

- `CQ` = calling anyone  
- `HOTG` = stands for **"Hams on the Gram"** (the APRS group)  
- `Your message here` = whatever short message you'd like to send  

📍 **Send this as an APRS message to the callsign: `ANSRVR`**

When you do this:
- You join the HOTG group for 12 hours
- Your message is sent to everyone in the group
- You’ll also receive any messages sent by others during that time

---

## 🚪 How to Leave the Group

When you're done listening or want to stop receiving messages, send this message to `ANSRVR`:

```
U HOTG
```

- `U` = Unsubscribe from HOTG

This helps reduce traffic on the APRS RF network.

---

## 🔇 Stay Subscribed, But Silent

If you want to stay subscribed **without** sending a message to the group, send:

```
K HOTG
```

- `K` = Silent join

This keeps you in the group for another 12 hours without alerting others.  
Useful if you’re on RF and don’t want to flood the airwaves.

---

## 🧭 Alternative Check-in (No Message Flood)

If you prefer **not** to have your message forwarded to the group (to avoid RF congestion), you can send your check-in **directly to `APRSPH`**.

### 📤 Send this message to `APRSPH`:
```
HOTG Your message here
```

- Your check-in **is logged** for #APRSThursday
- Your message **is NOT sent** to the group
- You'll get a **confirmation reply** with timestamp and a URL

📝 This method still counts for the #APRSThursday logs.

---

## 📊 See Check-in Map & Logs

- You can view visual check-ins at **[aprs.to](https://aprs.to)** (by N2RWE) — started July 13, 2023
- The **APRSPH logging system** started on January 11, 2024

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
