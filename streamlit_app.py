import os
import joblib
import pandas as pd
import numpy as np
import streamlit as st

MODEL_FILE = "model.pkl"
PIPELINE_FILE = "pipeline.pkl"

# Page configuration
st.set_page_config(
    page_title="Housing Price Predictor",
    page_icon="🏠",
    layout="wide"
)

@st.cache_resource
def load_model():
    """Load model and pipeline with caching"""
    if os.path.exists(MODEL_FILE) and os.path.exists(PIPELINE_FILE):
        model = joblib.load(MODEL_FILE)
        pipeline = joblib.load(PIPELINE_FILE)
        return model, pipeline
    return None, None

def main():
    st.title("🏠 Housing Price Prediction System")
    st.markdown("Predict median house values based on California housing data")
    
    # Load model
    model, pipeline = load_model()
    
    if model is None or pipeline is None:
        st.error(f"❌ Model files not found. Please ensure {MODEL_FILE} and {PIPELINE_FILE} exist.")
        st.info("Run `python main.py` to train the model first.")
        return
    
    st.success("✅ Model loaded successfully!")
    
    # Create tabs
    tab1, tab2 = st.tabs(["Single Prediction", "Batch Prediction"])
    
    with tab1:
        st.header("Enter Housing Details")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            longitude = st.number_input("Longitude", value=-122.23, format="%.2f")
            latitude = st.number_input("Latitude", value=37.88, format="%.2f")
            housing_median_age = st.number_input("Housing Median Age", value=41.0, min_value=0.0, format="%.1f")
        
        with col2:
            total_rooms = st.number_input("Total Rooms", value=880.0, min_value=0.0, format="%.1f")
            total_bedrooms = st.number_input("Total Bedrooms", value=129.0, min_value=0.0, format="%.1f")
            population = st.number_input("Population", value=322.0, min_value=0.0, format="%.1f")
        
        with col3:
            households = st.number_input("Households", value=126.0, min_value=0.0, format="%.1f")
            median_income = st.number_input("Median Income (in $10,000s)", value=8.3252, min_value=0.0, format="%.4f")
            ocean_proximity = st.selectbox(
                "Ocean Proximity",
                options=["NEAR BAY", "<1H OCEAN", "INLAND", "NEAR OCEAN", "ISLAND"]
            )
        
        if st.button("🔮 Predict Price", type="primary"):
            # Create input dataframe
            input_data = pd.DataFrame({
                'longitude': [longitude],
                'latitude': [latitude],
                'housing_median_age': [housing_median_age],
                'total_rooms': [total_rooms],
                'total_bedrooms': [total_bedrooms],
                'population': [population],
                'households': [households],
                'median_income': [median_income],
                'ocean_proximity': [ocean_proximity]
            })
            
            try:
                # Transform and predict
                transformed_input = pipeline.transform(input_data)
                prediction = model.predict(transformed_input)[0]
                
                st.success(f"### Predicted Median House Value: ${prediction:,.2f}")
                
                # Show input summary
                with st.expander("View Input Details"):
                    st.dataframe(input_data)
                
            except Exception as e:
                st.error(f"Error making prediction: {str(e)}")
    
    with tab2:
        st.header("Upload CSV File for Batch Predictions")
        
        st.markdown("""
        **Required columns:**
        - longitude
        - latitude
        - housing_median_age
        - total_rooms
        - total_bedrooms
        - population
        - households
        - median_income
        - ocean_proximity
        """)
        
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        
        if uploaded_file is not None:
            try:
                # Read CSV
                input_df = pd.read_csv(uploaded_file)
                
                st.info(f"Loaded {len(input_df)} records")
                
                # Show preview
                with st.expander("Preview Input Data"):
                    st.dataframe(input_df.head(10))
                
                if st.button("🔮 Generate Predictions", type="primary"):
                    # Transform and predict
                    transformed_input = pipeline.transform(input_df)
                    predictions = model.predict(transformed_input)
                    
                    # Add predictions to dataframe
                    result_df = input_df.copy()
                    result_df['predicted_median_house_value'] = predictions
                    
                    st.success(f"✅ Generated {len(predictions)} predictions!")
                    
                    # Show statistics
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Average Prediction", f"${predictions.mean():,.2f}")
                    with col2:
                        st.metric("Minimum", f"${predictions.min():,.2f}")
                    with col3:
                        st.metric("Maximum", f"${predictions.max():,.2f}")
                    
                    # Show results
                    st.dataframe(result_df)
                    
                    # Download button
                    csv = result_df.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Predictions as CSV",
                        data=csv,
                        file_name="predictions.csv",
                        mime="text/csv"
                    )
                    
            except Exception as e:
                st.error(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()
