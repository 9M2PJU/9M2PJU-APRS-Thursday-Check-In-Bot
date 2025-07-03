import schedule
import time
import argparse
from datetime import datetime
import pytz
import aprslib

# === APRS CONFIGURATION ===
CALLSIGN = "CALLSIGN"
PASSCODE = "PASSCODE"
SERVER = "aprs.hamradio.my"
PORT = 14580
DEST = "ANSRVR"
MESSAGE = "CQ HOTG Hello from CALLSIGN"

# Malaysia timezone
MALAYSIA = pytz.timezone("Asia/Kuala_Lumpur")

def send_aprs_message():
    now = datetime.now(MALAYSIA)
    print(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Sending APRS message...")

    try:
        aprs = aprslib.IS(CALLSIGN, passwd=PASSCODE)
        aprs.connect(SERVER, PORT)

        # Construct APRS message packet to ANSRVR
        # Format: "CALLSIGN>APRS,TCPIP*:;DST :message"
        packet = f"{CALLSIGN}>APRS::{'ANSRVR':<9}:CQ HOTG Hello from CALLSIGN"

        aprs.sendall(packet)
        print("✅ APRS message sent successfully to ANSRVR.")
    except Exception as e:
        print(f"❌ Failed to send APRS message: {e}")

def job_wrapper():
    now = datetime.now(MALAYSIA)
    if now.weekday() == 3:  # Thursday
        send_aprs_message()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Send APRS message immediately for testing')
    args = parser.parse_args()

    if args.test:
        send_aprs_message()
    else:
        schedule.every().day.at("21:00").do(job_wrapper)
        print("📡 APRS Bot is running. Waiting for Thursday 9:00 PM MYT to send message...")
        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    main()
