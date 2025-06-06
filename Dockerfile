# Use official Python slim image
FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend and frontend
COPY api ./api
COPY app.py .

# Expose ports
EXPOSE 8000
EXPOSE 8501

# Entrypoint script to run both FastAPI and Streamlit together
CMD ["sh", "-c", "\
  uvicorn api.main:app --host 0.0.0.0 --port 8000 & \
  streamlit run app.py --server.port=8501 --server.headless=true"]

