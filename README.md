# 🏠 Housing Price Prediction System

A machine learning system for predicting median house values in California based on various housing features.

## 📖 Overview

This project uses a Random Forest Regressor to predict housing prices based on features like location, median income, housing age, and ocean proximity. The model is trained on California housing data and can be deployed in multiple ways.

## 🎯 Features

- **REST API** - Flask-based API for programmatic predictions
- **Web Interface** - Interactive Streamlit app for easy predictions
- **Batch Processing** - Support for CSV file uploads
- **Docker Support** - Containerized deployment
- **Production Ready** - Includes Gunicorn for production deployments

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the Model (if needed)
```bash
python main.py
```
This creates `model.pkl` and `pipeline.pkl` files.

### 3. Choose Your Deployment Method

#### Option A: Streamlit Web App (Easiest)
```bash
streamlit run streamlit_app.py
```
Open http://localhost:8501 in your browser.

#### Option B: Flask API
```bash
python app.py
```
API available at http://localhost:5000

#### Option C: Docker
```bash
docker-compose up -d
```
- API: http://localhost:5000
- Streamlit: http://localhost:8501

## 📊 Model Features

The model uses the following input features:
- **longitude**: Longitude coordinate
- **latitude**: Latitude coordinate  
- **housing_median_age**: Median age of houses in the block
- **total_rooms**: Total number of rooms in the block
- **total_bedrooms**: Total number of bedrooms in the block
- **population**: Total population in the block
- **households**: Total number of households in the block
- **median_income**: Median income of households (in $10,000s)
- **ocean_proximity**: Proximity to ocean (categorical)

## 🔌 API Usage

### Health Check
```bash
curl http://localhost:5000/health
```

### Make Predictions
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

### Test API
```bash
python test_api.py
```

## 📁 Project Structure

```
.
├── main.py                 # Training script
├── app.py                  # Flask API
├── streamlit_app.py        # Streamlit web app
├── test_api.py            # API test script
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── DEPLOYMENT.md          # Detailed deployment guide
├── README.md              # This file
├── model.pkl              # Trained model
├── pipeline.pkl           # Preprocessing pipeline
└── housing.csv            # Training data
```

## 🛠️ Technology Stack

- **ML Framework**: scikit-learn
- **API**: Flask + Flask-CORS
- **Web UI**: Streamlit
- **Server**: Gunicorn (production)
- **Containerization**: Docker + Docker Compose
- **Data Processing**: pandas, numpy

## 📈 Model Performance

The model uses:
- **Algorithm**: Random Forest Regressor
- **Preprocessing**: StandardScaler for numerical features, OneHotEncoder for categorical
- **Missing Value Handling**: Median imputation

## 🚢 Deployment Options

See [DEPLOYMENT.md](DEPLOYMENT.md) for comprehensive deployment instructions including:
- Local deployment
- Docker deployment
- Cloud deployment (Heroku, AWS, GCP)
- Production configurations

## 🧪 Testing

Run the test script to verify API functionality:
```bash
python test_api.py
```

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 📧 Support

For issues or questions, please open an issue in the repository.
