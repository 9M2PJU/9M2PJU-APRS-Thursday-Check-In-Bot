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
        packet = f"{CALLSIGN}>APRS::{'ANSRVR':<9}:{MESSAGE}"
        aprs.sendall(packet)
        print("✅ APRS message sent successfully to ANSRVR.")
    except Exception as e:
        print(f"❌ Failed to send APRS message: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help='Send APRS message immediately (manual trigger)')
    args = parser.parse_args()

    if args.test:
        print("🔧 Test mode: Manual APRS message trigger")
    send_aprs_message()

if __name__ == "__main__":
    main()
