FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY main.py .
COPY app.py .
COPY streamlit_app.py .
COPY model.pkl .
COPY pipeline.pkl .

# Expose ports
# 5000 for Flask API
# 8501 for Streamlit
EXPOSE 5000 8501

# Default command runs Flask API
# Override with docker run command to run Streamlit instead
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "app:app"]
