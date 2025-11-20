# Housing Price Prediction - Deployment Guide

This guide covers multiple deployment options for the housing price prediction model.

## 📋 Prerequisites

- Python 3.11+
- Trained model files (`model.pkl` and `pipeline.pkl`)
- Docker (optional, for containerized deployment)

## 🚀 Deployment Options

### Option 1: Local Flask API

The Flask API provides RESTful endpoints for predictions.

#### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the API
python app.py
```

The API will be available at `http://localhost:5000`

#### API Endpoints

**Health Check**
```bash
curl http://localhost:5000/health
```

**Single/Multiple Predictions**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "data": [
      {
        "longitude": -122.23,
        "latitude": 37.88,
        "housing_median_age": 41.0,
        "total_rooms": 880.0,
        "total_bedrooms": 129.0,
        "population": 322.0,
        "households": 126.0,
        "median_income": 8.3252,
        "ocean_proximity": "NEAR BAY"
      }
    ]
  }'
```

**Batch Predictions (CSV Upload)**
```bash
curl -X POST http://localhost:5000/predict-batch \
  -F "file=@input.csv"
```

#### Production Deployment
For production, use Gunicorn:
```bash
gunicorn --bind 0.0.0.0:5000 --workers 4 --timeout 120 app:app
```

---

### Option 2: Streamlit Web App

Interactive web interface for single and batch predictions.

#### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit
streamlit run streamlit_app.py
```

The app will be available at `http://localhost:8501`

#### Features
- Interactive form for single predictions
- CSV file upload for batch predictions
- Real-time prediction statistics
- Download predictions as CSV

---

### Option 3: Docker Deployment

Containerized deployment for consistent environments.

#### Build and Run Flask API
```bash
# Build the image
docker build -t housing-predictor .

# Run the container
docker run -p 5000:5000 housing-predictor
```

#### Run Streamlit App
```bash
docker run -p 8501:8501 housing-predictor \
  streamlit run streamlit_app.py --server.port=8501 --server.address=0.0.0.0
```

#### Using Docker Compose (Both Services)
Run both Flask API and Streamlit together:
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Services:
- Flask API: `http://localhost:5000`
- Streamlit: `http://localhost:8501`

---

### Option 4: Cloud Deployment

#### Deploy to Heroku

1. Create `Procfile`:
```
web: gunicorn app:app
```

2. Deploy:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

#### Deploy to AWS EC2

1. SSH into EC2 instance
2. Clone repository
3. Install dependencies: `pip install -r requirements.txt`
4. Run with Gunicorn: `gunicorn --bind 0.0.0.0:5000 app:app`
5. Configure reverse proxy with Nginx (optional)

#### Deploy to Google Cloud Run

```bash
# Build and push to Google Container Registry
gcloud builds submit --tag gcr.io/PROJECT_ID/housing-predictor

# Deploy to Cloud Run
gcloud run deploy housing-predictor \
  --image gcr.io/PROJECT_ID/housing-predictor \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

#### Deploy Streamlit to Streamlit Cloud

1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Connect repository and select `streamlit_app.py`
4. Deploy

---

## 🔧 Configuration

### Environment Variables
```bash
export MODEL_FILE=model.pkl
export PIPELINE_FILE=pipeline.pkl
export FLASK_ENV=production
```

### Port Configuration
- Flask API: Default port 5000
- Streamlit: Default port 8501

---

## 📊 Monitoring

### Health Checks
```bash
# Check if API is running
curl http://localhost:5000/health
```

### Logs
```bash
# Docker logs
docker logs <container_id>

# Docker Compose logs
docker-compose logs -f api
docker-compose logs -f streamlit
```

---

## 🔒 Security Considerations

1. **API Keys**: Add authentication for production deployments
2. **HTTPS**: Use SSL/TLS certificates
3. **Rate Limiting**: Implement rate limiting to prevent abuse
4. **Input Validation**: Already implemented in the API
5. **CORS**: Configure CORS settings appropriately

---

## 📝 Example Test Scripts

### Python Test Script
```python
import requests
import json

url = "http://localhost:5000/predict"
data = {
    "data": [{
        "longitude": -122.23,
        "latitude": 37.88,
        "housing_median_age": 41.0,
        "total_rooms": 880.0,
        "total_bedrooms": 129.0,
        "population": 322.0,
        "households": 126.0,
        "median_income": 8.3252,
        "ocean_proximity": "NEAR BAY"
    }]
}

response = requests.post(url, json=data)
print(json.dumps(response.json(), indent=2))
```

### PowerShell Test Script
```powershell
$uri = "http://localhost:5000/predict"
$body = @{
    data = @(
        @{
            longitude = -122.23
            latitude = 37.88
            housing_median_age = 41.0
            total_rooms = 880.0
            total_bedrooms = 129.0
            population = 322.0
            households = 126.0
            median_income = 8.3252
            ocean_proximity = "NEAR BAY"
        }
    )
} | ConvertTo-Json -Depth 3

Invoke-RestMethod -Uri $uri -Method Post -Body $body -ContentType "application/json"
```

---

## 🐛 Troubleshooting

### Model files not found
Ensure `model.pkl` and `pipeline.pkl` exist. Run `python main.py` to train if needed.

### Port already in use
```bash
# Find process using port
netstat -ano | findstr :5000

# Kill process (replace PID)
taskkill /PID <PID> /F
```

### Docker build fails
Ensure model files exist before building:
```bash
python main.py  # Train model first
docker build -t housing-predictor .
```

---

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Docker Documentation](https://docs.docker.com/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)

---

## 🎯 Quick Start Commands

```bash
# Local development (Streamlit)
streamlit run streamlit_app.py

# Production API
gunicorn --bind 0.0.0.0:5000 --workers 4 app:app

# Docker (both services)
docker-compose up -d
```
