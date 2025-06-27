
import json
import os
from datetime import datetime

TELEMETRY_FILE = "demo_data/telemetry_stream.jsonl"
ENRICHED_FILE = "reports/ioc_enriched_feed.json"

# Simulated enrichment database (mocked threat intel mappings)
MOCK_THREAT_FEED = {
    "GNSS_DRIFT": {
        "description": "GNSS signal deviation detected",
        "linked_ttp": "T1632 - GPS Spoofing",
        "associated_actor": "APT-C-23",
        "related_cve": "CVE-2022-38472"
    },
    "RF_SPIKE": {
        "description": "Radio frequency jamming burst",
        "linked_ttp": "T1640 - RF Jamming",
        "associated_actor": "Russian GRU Unit 26165",
        "related_cve": "CVE-2021-45307"
    },
    "FIRMWARE_TAMPER": {
        "description": "Firmware CRC/HMAC anomaly",
        "linked_ttp": "T1542.001 - Firmware Modification",
        "associated_actor": "Lazarus Group",
        "related_cve": "CVE-2019-11932"
    }
}

def enrich_events():
    if not os.path.exists(TELEMETRY_FILE):
        print("[!] No telemetry found.")
        return

    enriched_data = []
    with open(TELEMETRY_FILE, "r") as f:
        for line in f.readlines()[-20:]:
            try:
                entry = json.loads(line)
                enriched = MOCK_THREAT_FEED.get(entry["type"], {})
                entry.update({"enriched": enriched})
                enriched_data.append(entry)
            except:
                continue

    os.makedirs("reports", exist_ok=True)
    with open(ENRICHED_FILE, "w") as f:
        json.dump(enriched_data, f, indent=2)

    print(f"[✓] Enriched IOCs saved to: {ENRICHED_FILE}")

if __name__ == "__main__":
    enrich_events()
