from flask import Flask, render_template, request, abort
from catboost import CatBoostRegressor
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os
import joblib

app = Flask(__name__)

# Determine the absolute paths
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, '..', 'src', 'models', 'best_catboost_model.cbm')
location_mapping_path = os.path.join(current_dir, '..', 'src', 'models', 'location_mapping.joblib')

# Load the model
try:
    model = CatBoostRegressor()
    model.load_model(model_path)
except Exception as e:
    print(f"Error loading the model: {e}")
    model = None

# Load the location mapping
try:
    location_encoder = joblib.load(location_mapping_path)
    print("Location mapping loaded successfully.")
    print("Type of location_mapping:", type(location_encoder))
    
    # Get the classes (unique locations) from the LabelEncoder
    location_options = location_encoder.classes_
    print("Number of locations:", len(location_options))
    print("Sample of location_options (first 5):", location_options[:5])
except Exception as e:
    print(f"Error loading the location mapping: {e}")
    location_encoder = None
    location_options = []

def calculate_operation_minutes(start_time):
    morning_start = pd.Timestamp(start_time.date()).replace(hour=6, minute=30)
    afternoon_start = pd.Timestamp(start_time.date()).replace(hour=15, minute=0)
    
    if start_time < afternoon_start:  # Morning session
        return max(0, (start_time - morning_start).total_seconds() // 60 + 1)
    else:  # Afternoon session
        return (start_time - afternoon_start).total_seconds() // 60 + 181

def engineer_features(data):
    # Convert input data
    route_id = data['route_id']
    start_location = data['start_location']
    destination_location = data['destination_location']
    start_time = pd.to_datetime(data['start_time'])
    temperature = float(data['temperature'])
    precip_mm = float(data['precip_mm'])
    cloud_cover = float(data['cloud_cover'])
    pressure = float(data['pressure'])

    # Calculate minutes of operation
    minutes_of_operation = calculate_operation_minutes(start_time)

    # Calculate minutes_cos
    minutes_cos = np.cos(2 * np.pi * minutes_of_operation / (24 * 60))

    # Encode start and destination locations
    if location_encoder is not None:
        start_stop_id_encoded = location_encoder.transform([start_location])[0]
        end_stop_id_encoded = location_encoder.transform([destination_location])[0]
    else:
        # Fallback if encoder is not available
        start_stop_id_encoded = hash(start_location) % 1000
        end_stop_id_encoded = hash(destination_location) % 1000

    # For this example, we'll use a placeholder for distance and avg_speed
    # In a real scenario, you'd calculate these based on the start and destination locations
    distance = 10  # placeholder value
    avg_speed = 40  # placeholder value

    # Categorize speed
    speed_category = 1 if avg_speed >= 30 else 0

    # Create feature dictionary
    features = {
        'distance': distance,
        'Speed_Category': speed_category,
        'start_stop_id_encoded': start_stop_id_encoded,
        'minutes_cos': minutes_cos,
        'route_id': route_id,
        'end_stop_id_encoded': end_stop_id_encoded,
        'precip_mm': precip_mm,
        'temperature': temperature,
        'cloud_cover': cloud_cover,
        'pressure': pressure
    }

    return features, start_time

@app.route('/')
def home():
    return render_template('index.html', locations=location_options)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        abort(500, description="Model not loaded. Please check server logs.")

    data = request.form
    engineered_features, start_time = engineer_features(data)
    
    # Convert engineered features to the format expected by the model
    features_list = [
        engineered_features['distance'],
        engineered_features['Speed_Category'],
        engineered_features['start_stop_id_encoded'],
        engineered_features['minutes_cos'],
        engineered_features['route_id'],
        engineered_features['end_stop_id_encoded'],
        engineered_features['precip_mm'],
        engineered_features['temperature'],
        engineered_features['cloud_cover'],
        engineered_features['pressure']
    ]
    
    try:
        # Make prediction
        prediction = model.predict([features_list])
        
        # Convert prediction to minutes
        predicted_duration = round(prediction[0])
        
        # Calculate arrival time
        arrival_time = start_time + timedelta(minutes=predicted_duration)
        
        return render_template('result.html', 
                               prediction=predicted_duration, 
                               start_time=start_time,
                               arrival_time=arrival_time)
    except Exception as e:
        print(f"Error making prediction: {e}")
        abort(500, description="Error making prediction. Please check server logs.")

if __name__ == '__main__':
    app.run(debug=True)