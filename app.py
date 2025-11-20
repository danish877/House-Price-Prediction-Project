import os
import joblib
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MODEL_FILE = "model.pkl"
PIPELINE_FILE = "pipeline.pkl"

# Load model and pipeline at startup
model = None
pipeline = None

def load_model():
    global model, pipeline
    if os.path.exists(MODEL_FILE) and os.path.exists(PIPELINE_FILE):
        model = joblib.load(MODEL_FILE)
        pipeline = joblib.load(PIPELINE_FILE)
        return True
    return False

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    if model is not None and pipeline is not None:
        return jsonify({"status": "healthy", "model_loaded": True}), 200
    return jsonify({"status": "unhealthy", "model_loaded": False}), 503

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict housing prices for input data
    
    Expected JSON format:
    {
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
    }
    """
    try:
        if model is None or pipeline is None:
            return jsonify({"error": "Model not loaded"}), 503
        
        data = request.get_json()
        
        if not data or 'data' not in data:
            return jsonify({"error": "Invalid request format. Expected 'data' field with list of records"}), 400
        
        # Convert to DataFrame
        input_df = pd.DataFrame(data['data'])
        
        # Validate required columns
        required_columns = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 
                          'total_bedrooms', 'population', 'households', 'median_income', 
                          'ocean_proximity']
        
        missing_cols = set(required_columns) - set(input_df.columns)
        if missing_cols:
            return jsonify({"error": f"Missing required columns: {list(missing_cols)}"}), 400
        
        # Make predictions
        transformed_input = pipeline.transform(input_df)
        predictions = model.predict(transformed_input)
        
        # Add predictions to input data
        input_df['predicted_median_house_value'] = predictions
        
        return jsonify({
            "predictions": predictions.tolist(),
            "count": len(predictions)
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict-batch', methods=['POST'])
def predict_batch():
    """
    Predict housing prices from CSV file upload
    """
    try:
        if model is None or pipeline is None:
            return jsonify({"error": "Model not loaded"}), 503
        
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({"error": "Empty filename"}), 400
        
        # Read CSV
        input_df = pd.read_csv(file)
        
        # Make predictions
        transformed_input = pipeline.transform(input_df)
        predictions = model.predict(transformed_input)
        
        # Add predictions to input data
        input_df['predicted_median_house_value'] = predictions
        
        return jsonify({
            "predictions": predictions.tolist(),
            "count": len(predictions)
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    if load_model():
        print("Model and pipeline loaded successfully!")
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        print(f"Error: {MODEL_FILE} or {PIPELINE_FILE} not found. Please train the model first.")
