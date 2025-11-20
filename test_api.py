import requests
import json

def test_health():
    """Test the health endpoint"""
    print("Testing health endpoint...")
    response = requests.get("http://localhost:5000/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

def test_predict():
    """Test the prediction endpoint"""
    print("Testing prediction endpoint...")
    
    url = "http://localhost:5000/predict"
    data = {
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
            },
            {
                "longitude": -122.22,
                "latitude": 37.86,
                "housing_median_age": 21.0,
                "total_rooms": 7099.0,
                "total_bedrooms": 1106.0,
                "population": 2401.0,
                "households": 1138.0,
                "median_income": 8.3014,
                "ocean_proximity": "NEAR BAY"
            }
        ]
    }
    
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

if __name__ == "__main__":
    try:
        test_health()
        test_predict()
        print("✅ All tests completed!")
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the API. Make sure the server is running on http://localhost:5000")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
