
import os
import readline
import json
from datetime import datetime

HISTORY_FILE = "logs/copilot_history.log"
os.makedirs("logs", exist_ok=True)

PROMPT = "🧠 Copilot> "
session_memory = []

def save_to_history(entry):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"{datetime.utcnow().isoformat()} - {entry}\n")

def simulate_response(user_input):
    if "gnss" in user_input.lower():
        return "Detected GNSS drift. Possible spoofing in NMEA stream. Suggest verifying with backup GPS source."
    elif "rf" in user_input.lower():
        return "RF spike noted. Cross-check frequency with known jamming ranges. Alert issued."
    elif "firmware" in user_input.lower():
        return "Firmware anomaly found. HMAC invalid — advise integrity check and possible reflash."
    elif "ioc" in user_input.lower():
        return "IOC correlation complete. Matching against BlackEnergy and FancyBear TTPs."
    else:
        return "Input received. Analyzing pattern... No match found. Continue monitoring."

def copilot_loop():
    print("🧠 Copilot CLI – Session started. Type 'exit' to quit.")
    while True:
        try:
            user_input = input(PROMPT).strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("🧠 Session ended.")
                break

            session_memory.append(user_input)
            save_to_history(user_input)

            response = simulate_response(user_input)
            print(f"🤖 {response}")

        except KeyboardInterrupt:
            print("\n🧠 Session interrupted.")
            break

if __name__ == "__main__":
    copilot_loop()
