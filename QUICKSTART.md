# 🚀 Quick Start Guide

## ✅ Your Project is Ready to Deploy!

Your model files (`model.pkl` and `pipeline.pkl`) are already trained and ready to use.

---

## 🎯 Choose Your Deployment Method

### Option 1: Streamlit Web App (Recommended for Beginners)

**Most user-friendly option with a visual interface**

```powershell
# Install dependencies (first time only)
pip install -r requirements.txt

# Start the web app
.\start_streamlit.ps1
# OR
streamlit run streamlit_app.py
```

Then open your browser to **http://localhost:8501**

**Features:**
- 📝 Interactive form for single predictions
- 📊 Upload CSV files for batch predictions
- 📈 Visual statistics and charts
- 💾 Download predictions as CSV

---

### Option 2: Flask REST API (For Programmatic Access)

**Best for integrating with other applications**

```powershell
# Install dependencies (first time only)
pip install -r requirements.txt

# Start the API
.\start_api.ps1
# OR
python app.py
```

API available at **http://localhost:5000**

**Test the API:**
```powershell
# Health check
Invoke-RestMethod -Uri "http://localhost:5000/health"

# Make a prediction
python test_api.py
```

---

### Option 3: Docker (For Production)

**Best for deployment to servers or cloud**

```powershell
# Start both API and Streamlit
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

**Services:**
- Flask API: http://localhost:5000
- Streamlit: http://localhost:8501

---

## 📝 Using Your Existing Files

### Your Input CSV Format
Your `input.csv` should have these columns:
- longitude
- latitude
- housing_median_age
- total_rooms
- total_bedrooms
- population
- households
- median_income
- ocean_proximity

### Generate Predictions

**Via Streamlit:**
1. Run `streamlit run streamlit_app.py`
2. Go to "Batch Prediction" tab
3. Upload your `input.csv`
4. Click "Generate Predictions"
5. Download the results

**Via API:**
```powershell
# Using curl (if installed)
curl -X POST http://localhost:5000/predict-batch -F "file=@input.csv"

# Using Python
python -c "import requests; r = requests.post('http://localhost:5000/predict-batch', files={'file': open('input.csv', 'rb')}); print(r.json())"
```

---

## 🔧 Installation (First Time Setup)

```powershell
# Install all dependencies
pip install -r requirements.txt
```

**Dependencies installed:**
- pandas - Data processing
- scikit-learn - Machine learning
- flask - REST API
- streamlit - Web interface
- joblib - Model serialization

---

## 💡 Common Commands

```powershell
# Start Streamlit web app
streamlit run streamlit_app.py

# Start Flask API
python app.py

# Test API
python test_api.py

# Retrain model (if needed)
python main.py

# Docker - start all services
docker-compose up -d

# Docker - view logs
docker-compose logs -f

# Docker - stop all services
docker-compose down
```

---

## 🌐 Accessing the Applications

| Service | URL | Description |
|---------|-----|-------------|
| Streamlit Web App | http://localhost:8501 | Interactive UI |
| Flask API | http://localhost:5000 | REST API |
| Health Check | http://localhost:5000/health | API status |

---

## 📊 Example Prediction

**Sample input:**
```json
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
```

**Expected output:**
```json
{
  "predictions": [446573.16],
  "count": 1
}
```

---

## 🆘 Troubleshooting

### Port already in use
```powershell
# Find and kill process on port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Missing dependencies
```powershell
pip install -r requirements.txt
```

### Model files not found
Your model files are already there! If you deleted them:
```powershell
python main.py
```

---

## 📚 More Information

- **Full deployment guide**: See `DEPLOYMENT.md`
- **Project overview**: See `README.md`
- **Test your API**: Run `python test_api.py`

---

## ⚡ Fastest Start (30 seconds)

```powershell
# 1. Install (skip if already done)
pip install streamlit pandas scikit-learn joblib

# 2. Run
streamlit run streamlit_app.py

# 3. Open browser to http://localhost:8501
```

That's it! Your model is deployed and ready to use! 🎉
