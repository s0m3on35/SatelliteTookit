#!/bin/bash
echo "[+] Starting Satellite Defense Toolkit via Docker..."
docker build -t satellite-defense-toolkit .
docker run -p 8501:8501 satellite-defense-toolkit