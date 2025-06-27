# Satellite Defense Toolkit Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
RUN pip install streamlit

# Copy all files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Default command
CMD ["streamlit", "run", "live_correlation_dashboard.py"]