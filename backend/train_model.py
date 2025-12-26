"""
HeartCare AI - Model Training Script
Trains multiple ML models and selects the best performer
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
import os

# Sample heart disease dataset
def create_sample_data():
    """Create sample dataset for demonstration"""
    np.random.seed(42)
    n_samples = 303
    
    data = {
        'age': np.random.randint(29, 78, n_samples),
        'sex': np.random.randint(0, 2, n_samples),
        'cp': np.random.randint(0, 4, n_samples),
        'trtbps': np.random.randint(94, 201, n_samples),
        'chol': np.random.randint(126, 565, n_samples),
        'fbs': np.random.randint(0, 2, n_samples),
        'restecg': np.random.randint(0, 3, n_samples),
        'thalachh': np.random.randint(71, 203, n_samples),
        'exng': np.random.randint(0, 2, n_samples),
        'oldpeak': np.random.uniform(0, 6.2, n_samples),
        'slp': np.random.randint(0, 3, n_samples),
        'caa': np.random.randint(0, 5, n_samples),
        'thall': np.random.randint(0, 4, n_samples),
        'output': np.random.randint(0, 2, n_samples)
    }
    
    return pd.DataFrame(data)

def train_models():
    """Train and evaluate multiple ML models"""
    print("=" * 60)
    print("HeartCare AI - Model Training")
    print("=" * 60)
    
    # Load or create data
    print("\n[1/6] Loading data...")
    try:
        df = pd.read_csv('../data/heart.csv')
        print(f"✓ Loaded {len(df)} records from heart.csv")
    except:
        print("! heart.csv not found, creating sample data...")
        df = create_sample_data()
        # Save sample data
        os.makedirs('../data', exist_ok=True)
        df.to_csv('../data/heart.csv', index=False)
        print(f"✓ Created sample dataset with {len(df)} records")
    
    # Prepare data
    print("\n[2/6] Preparing data...")
    X = df.drop('output', axis=1)
    y = df['output']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"✓ Training set: {len(X_train)} samples")
    print(f"✓ Test set: {len(X_test)} samples")
    
    # Scale features
    print("\n[3/6] Scaling features...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("✓ Features scaled using StandardScaler")
    
    # Train multiple models
    print("\n[4/6] Training models...")
    models = {
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
        'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
        'SVM': SVC(kernel='rbf', probability=True, random_state=42)
    }
    
    results = {}
    best_model = None
    best_score = 0
    best_name = ""
    
    for name, model in models.items():
        print(f"\n  Training {name}...")
        model.fit(X_train_scaled, y_train)
        
        # Evaluate
        train_score = model.score(X_train_scaled, y_train)
        test_score = model.score(X_test_scaled, y_test)
        cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5)
        
        results[name] = {
            'model': model,
            'train_accuracy': train_score,
            'test_accuracy': test_score,
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std()
        }
        
        print(f"    Training Accuracy: {train_score:.4f}")
        print(f"    Test Accuracy: {test_score:.4f}")
        print(f"    CV Score: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
        
        if test_score > best_score:
            best_score = test_score
            best_model = model
            best_name = name
    
    # Select best model
    print(f"\n[5/6] Best Model: {best_name}")
    print(f"  Test Accuracy: {best_score:.4f}")
    
    # Detailed evaluation
    print("\n[6/6] Detailed Evaluation...")
    y_pred = best_model.predict(X_test_scaled)
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, 
                                target_names=['No Heart Attack', 'Heart Attack']))
    
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    
    # Feature importance (if available)
    if hasattr(best_model, 'feature_importances_'):
        print("\nTop 5 Important Features:")
        feature_importance = pd.DataFrame({
            'feature': X.columns,
            'importance': best_model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        for idx, row in feature_importance.head().iterrows():
            print(f"  {row['feature']}: {row['importance']:.4f}")
    
    # Save model and scaler
    print("\n" + "=" * 60)
    print("Saving model and scaler...")
    os.makedirs('../models', exist_ok=True)
    
    with open('../models/heart_attack_model.pkl', 'wb') as f:
        pickle.dump(best_model, f)
    print("✓ Model saved to models/heart_attack_model.pkl")
    
    with open('../models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    print("✓ Scaler saved to models/scaler.pkl")
    
    print("\n" + "=" * 60)
    print("Training Complete!")
    print("=" * 60)
    
    return best_model, scaler, results

if __name__ == '__main__':
    train_models()
