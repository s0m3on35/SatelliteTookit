
import streamlit as st
import json
import os
from datetime import datetime

TELEMETRY_FILE = "demo_data/telemetry_stream.jsonl"

st.set_page_config(page_title="🛰️ Satellite Defense Dashboard", layout="wide")

st.title("🛰️ Satellite Defense Toolkit – Live Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.header("📡 Live Telemetry Events")
    if os.path.exists(TELEMETRY_FILE):
        with open(TELEMETRY_FILE, "r") as f:
            lines = f.readlines()[-20:]
            for line in reversed(lines):
                try:
                    event = json.loads(line)
                    st.markdown(f"🔸 `{event['timestamp']}` **{event['type']}**")
                except:
                    continue
    else:
        st.warning("No telemetry data found.")

with col2:
    st.header("🧪 Simulation Control")
    st.markdown("Use CLI or external script to simulate threats.")
    st.code("python real_time_threat_simulator.py")
    st.markdown("Latest snapshot updates every few seconds.")

st.markdown("---")
st.info("👁️ Dashboard auto-refresh recommended every 5–10s.")
