
import json
import random
import time
from datetime import datetime

output_file = "demo_data/telemetry_stream.jsonl"

def generate_gnss_drift():
    base_lat = 37.7749
    base_lon = -122.4194
    drift_lat = base_lat + random.uniform(-0.001, 0.001)
    drift_lon = base_lon + random.uniform(-0.001, 0.001)
    return {"type": "GNSS_DRIFT", "lat": round(drift_lat, 6), "lon": round(drift_lon, 6)}

def generate_rf_spike():
    return {"type": "RF_SPIKE", "freq_mhz": random.randint(1570, 1620), "power_db": random.uniform(-30, 10)}

def generate_firmware_tamper():
    return {
        "type": "FIRMWARE_TAMPER",
        "firmware_version": f"v{random.randint(1,5)}.{random.randint(0,9)}.{random.randint(0,9)}",
        "crc_status": random.choice(["FAILED", "CORRUPTED", "UNVERIFIED"]),
        "hmac_check": random.choice(["INVALID", "TAMPERED", "OK"]),
    }

def write_event(event):
    event["timestamp"] = datetime.utcnow().isoformat() + "Z"
    with open(output_file, "a") as f:
        f.write(json.dumps(event) + "\n")
    print(f"[+] Event written: {event['type']}")

def run_loop(interval=5):
    print("Starting Real-Time Threat Simulator... Press Ctrl+C to stop.")
    while True:
        threat = random.choice([
            generate_gnss_drift(),
            generate_rf_spike(),
            generate_firmware_tamper()
        ])
        write_event(threat)
        time.sleep(interval)

if __name__ == "__main__":
    run_loop()
