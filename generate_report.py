
import os
import json
from datetime import datetime

HISTORY_FILE = "logs/copilot_history.log"
TELEMETRY_FILE = "demo_data/telemetry_stream.jsonl"
OUTPUT_FILE = "reports/auto_report.md"

def read_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return f.readlines()

def read_telemetry():
    if not os.path.exists(TELEMETRY_FILE):
        return []
    with open(TELEMETRY_FILE, "r") as f:
        return [json.loads(line) for line in f]

def generate_report():
    os.makedirs("reports", exist_ok=True)
    history = read_history()
    telemetry = read_telemetry()

    with open(OUTPUT_FILE, "w") as f:
        f.write("# 🛰️ Satellite Defense Toolkit Report\n\n")
        f.write(f"Generated on: {datetime.utcnow().isoformat()}Z\n\n")

        f.write("##  Copilot Session\n")
        if history:
            for line in history[-10:]:
                f.write(f"- {line.strip()}\n")
        else:
            f.write("_No session history found._\n")

        f.write("\n## 📡 Telemetry Events (Last 10)\n")
        if telemetry:
            for event in telemetry[-10:]:
                f.write(f"- `{event['timestamp']}` **{event['type']}**\n")
        else:
            f.write("_No telemetry events found._\n")

        f.write("\n---\n")
        f.write(" **Status:** Preliminary analysis complete. Correlate with threat feeds for full enrichment.\n")

    print(f"[✓] Report generated: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_report()
