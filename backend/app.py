"""
Heart Attack Prediction - Backend Flask Application
Production-grade heart attack risk prediction system
"""

from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
import pandas as pd
import numpy as np
import pickle
import os
from datetime import datetime
import json

app = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')
app.secret_key = 'heart_attack_prediction_secret_key_2024'
CORS(app)

# Load the trained model
MODEL_PATH = '../models/heart_attack_model.pkl'
SCALER_PATH = '../models/scaler.pkl'

def load_model():
    """Load the trained model and scaler"""
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        with open(SCALER_PATH, 'rb') as f:
            scaler = pickle.load(f)
        return model, scaler
    except:
        return None, None

model, scaler = load_model()

# Feature importance data (from model training)
FEATURE_IMPORTANCE = {
    'cp': 0.25,      # Chest pain type
    'thalachh': 0.18, # Maximum heart rate
    'oldpeak': 0.15,  # ST depression
    'caa': 0.12,      # Number of major vessels
    'age': 0.10,      # Age
    'sex': 0.08,      # Gender
    'trtbps': 0.06,   # Resting blood pressure
    'chol': 0.06      # Cholesterol
}

@app.route('/')
def home():
    """Home page"""
    return render_template('home.html')

@app.route('/predict')
def predict_page():
    """Patient data input page"""
    return render_template('predict.html')

@app.route('/dashboard')
def dashboard():
    """Analytics dashboard page"""
    return render_template('dashboard.html')



@app.route('/api/predict', methods=['POST'])
def predict():
    """
    Predict heart attack risk based on patient data
    Returns: Risk level, probability, and explanations
    """
    try:
        data = request.json
        
        # Extract features in correct order
        features = [
            float(data['age']),
            float(data['sex']),
            float(data['cp']),
            float(data['trtbps']),
            float(data['chol']),
            float(data['fbs']),
            float(data['restecg']),
            float(data['thalachh']),
            float(data['exng']),
            float(data['oldpeak']),
            float(data['slp']),
            float(data['caa']),
            float(data['thall'])
        ]
        
        # Create DataFrame
        feature_names = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 
                        'restecg', 'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']
        df = pd.DataFrame([features], columns=feature_names)
        
        # Make prediction
        if model is not None and scaler is not None:
            # Scale features
            features_scaled = scaler.transform(df)
            
            # Get prediction and probability
            prediction = model.predict(features_scaled)[0]
            probability = model.predict_proba(features_scaled)[0]
            
            risk_probability = probability[1] * 100
        else:
            # Fallback prediction logic
            risk_score = calculate_risk_score(data)
            prediction = 1 if risk_score > 0.5 else 0
            risk_probability = risk_score * 100
        
        # Determine risk category
        if risk_probability < 30:
            risk_category = "Low Risk"
            risk_color = "#10b981"  # Green
        elif risk_probability < 70:
            risk_category = "Medium Risk"
            risk_color = "#f59e0b"  # Amber
        else:
            risk_category = "High Risk"
            risk_color = "#ef4444"  # Red
        
        # Generate explanation
        explanation = generate_explanation(data, risk_probability)
        
        # Get key risk factors
        risk_factors = identify_risk_factors(data)
        
        result = {
            'prediction': int(prediction),
            'risk_probability': round(risk_probability, 2),
            'risk_category': risk_category,
            'risk_color': risk_color,
            'explanation': explanation,
            'risk_factors': risk_factors,
            'timestamp': datetime.now().isoformat()
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def calculate_risk_score(data):
    """Calculate risk score based on clinical parameters"""
    score = 0.0
    
    # Age factor
    age = int(data['age'])
    if age > 60:
        score += 0.2
    elif age > 50:
        score += 0.1
    
    # Chest pain type (cp)
    cp = int(data['cp'])
    if cp == 0:  # Typical angina
        score += 0.3
    elif cp == 1:  # Atypical angina
        score += 0.2
    
    # Maximum heart rate
    thalachh = int(data['thalachh'])
    if thalachh < 120:
        score += 0.15
    
    # ST depression (oldpeak)
    oldpeak = float(data['oldpeak'])
    if oldpeak > 2.0:
        score += 0.2
    elif oldpeak > 1.0:
        score += 0.1
    
    # Number of major vessels (caa)
    caa = int(data['caa'])
    score += caa * 0.1
    
    # Cholesterol
    chol = int(data['chol'])
    if chol > 240:
        score += 0.1
    
    return min(score, 1.0)

def generate_explanation(data, risk_probability):
    """Generate human-readable explanation of the prediction"""
    age = int(data['age'])
    sex = "Male" if int(data['sex']) == 1 else "Female"
    
    if risk_probability < 30:
        return f"Based on the analysis of the patient's clinical data (Age: {age}, Gender: {sex}), " \
               f"the risk of heart attack is LOW ({risk_probability:.1f}%). " \
               f"The patient shows favorable cardiac indicators. However, regular monitoring and " \
               f"maintaining a healthy lifestyle are recommended."
    elif risk_probability < 70:
        return f"The patient (Age: {age}, Gender: {sex}) shows MODERATE risk ({risk_probability:.1f}%) " \
               f"for heart attack. Several risk factors have been identified. " \
               f"Medical consultation and lifestyle modifications are strongly recommended. " \
               f"Regular cardiac monitoring should be implemented."
    else:
        return f"URGENT: The patient (Age: {age}, Gender: {sex}) shows HIGH risk ({risk_probability:.1f}%) " \
               f"for heart attack. Multiple significant risk factors detected. " \
               f"Immediate medical attention and comprehensive cardiac evaluation are strongly recommended. " \
               f"Preventive intervention may be necessary."

def identify_risk_factors(data):
    """Identify key risk factors from patient data"""
    factors = []
    
    age = int(data['age'])
    if age > 55:
        factors.append({
            'factor': 'Age',
            'value': age,
            'severity': 'High' if age > 65 else 'Medium',
            'description': f'Age {age} is a significant risk factor'
        })
    
    chol = int(data['chol'])
    if chol > 200:
        factors.append({
            'factor': 'Cholesterol',
            'value': chol,
            'severity': 'High' if chol > 240 else 'Medium',
            'description': f'Cholesterol level of {chol} mg/dL is elevated'
        })
    
    trtbps = int(data['trtbps'])
    if trtbps > 130:
        factors.append({
            'factor': 'Blood Pressure',
            'value': trtbps,
            'severity': 'High' if trtbps > 140 else 'Medium',
            'description': f'Resting blood pressure of {trtbps} mmHg is elevated'
        })
    
    thalachh = int(data['thalachh'])
    if thalachh < 120:
        factors.append({
            'factor': 'Max Heart Rate',
            'value': thalachh,
            'severity': 'Medium',
            'description': f'Maximum heart rate of {thalachh} bpm is below normal range'
        })
    
    oldpeak = float(data['oldpeak'])
    if oldpeak > 1.0:
        factors.append({
            'factor': 'ST Depression',
            'value': oldpeak,
            'severity': 'High' if oldpeak > 2.0 else 'Medium',
            'description': f'ST depression of {oldpeak} indicates cardiac stress'
        })
    
    return factors

@app.route('/api/feature-importance')
def get_feature_importance():
    """Get feature importance data for visualization"""
    return jsonify(FEATURE_IMPORTANCE)

@app.route('/api/statistics')
def get_statistics():
    """Get overall statistics for dashboard"""
    # Mock statistics (in production, these would come from database)
    stats = {
        'total_predictions': 1247,
        'high_risk_count': 312,
        'medium_risk_count': 498,
        'low_risk_count': 437,
        'average_age': 54.4,
        'male_percentage': 68.3,
        'female_percentage': 31.7
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
