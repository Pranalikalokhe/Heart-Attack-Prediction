# ❤️ Heart Attack Analysis and Prediction System

**Machine Learning–based clinical decision support system for heart attack risk analysis and prediction**

![Accuracy](https://img.shields.io/badge/Accuracy-92%25-success)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-green)
![ML](https://img.shields.io/badge/ML-scikit--learn-orange)

---

## 📋 Overview

The **Heart Attack Analysis and Prediction System** is a machine learning project designed to analyze patient health data, identify key risk factors using data visualization, and predict the likelihood of a heart attack.

The project demonstrates the complete machine learning lifecycle, from exploratory data analysis (EDA) and model comparison to backend deployment for prediction.

---

## 🎯 Project Objective

- ✅ Analyze patient medical data to understand key health risk factors
- ✅ Use data visualization to identify relationships between features
- ✅ Train and compare multiple machine learning classification models
- ✅ Select the best-performing model for heart attack risk prediction
- ✅ Provide a simple application interface for prediction

---

## ✨ Key Features

- 📊 **Exploratory Data Analysis (EDA)** using graphs and correlation heatmaps
- 🤖 **Multiple ML Models Compared** for fair evaluation
- 🏆 **Best Model Selection** based on accuracy and cross-validation
- ⚡ **Real-time Prediction** using a trained ML model
- 🧩 **Clean Project Structure** separating analysis, training, and prediction

---

## 📁 Project Structure

```
Heart attack prediction/
│
├── notebooks/
│   └── HeartAttack_Analysis.ipynb   # EDA & model experimentation
│
├── backend/
│   ├── train_model.py               # Final model training & saving
│   └── app.py                       # Prediction application
│
├── templates/
│   ├── home.html
│   ├── predict.html
│   ├── dashboard.html
│   └── insights.html
│
├── static/
│   ├── css/
│   └── js/
│
├── models/
│   ├── heart_attack_model.pkl       # Saved trained model
│   └── scaler.pkl                   # Feature scaler
│
└── data/
    └── heart.csv                    # Dataset
```

---

## 📊 Exploratory Data Analysis (EDA)

EDA was performed using a Jupyter Notebook to understand the dataset and identify key relationships.

### Visualizations Used:

- **Correlation Heatmaps** – to identify strongly related features
- **Histograms & Distribution Plots** – to analyze feature spread
- **Count Plots & Bar Charts** – to compare heart attack vs non-heart attack cases

### Key Insights:

- Age, chest pain type, cholesterol, heart rate, and ECG-related features showed strong influence on heart attack risk
- EDA helped guide feature understanding and model selection

---

## 🤖 Machine Learning Models Used

The following classification models were trained and evaluated:

| Algorithm | Purpose |
|-----------|---------|
| **Logistic Regression** | Baseline binary classification |
| **Random Forest** | Tree-based ensemble learning |
| **Gradient Boosting / Boosting-based Model** | Error-focused learning |
| **Support Vector Machine (SVM)** | Optimal decision boundary |

---

## 🏆 Model Evaluation & Final Selection

### Evaluation Metrics:

- ✅ Accuracy
- ✅ Confusion Matrix
- ✅ Cross-validation score

### Final Result:

**Boosting-based model** achieved the best overall performance

**Final Accuracy Achieved: ~92%**

The boosting-based model was selected because it:
- ✅ Learns from previous misclassifications
- ✅ Handles complex feature relationships
- ✅ Shows stable performance across validation folds

---

## 🧠 Project Workflow (High-Level)

1. Data collection and preprocessing
2. Exploratory Data Analysis (EDA) using graphs
3. Model experimentation and comparison (Notebook)
4. Final model training and saving (`train_model.py`)
5. Prediction using backend application (`app.py`)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Pranalikalokhe/Heart-Attack-Prediction.git
cd Heart-Attack-Prediction
```

2. **Install dependencies**
```bash
pip install flask flask-cors pandas numpy scikit-learn matplotlib seaborn
```

3. **Train the model** (optional - pre-trained model included)
```bash
cd backend
python train_model.py
```

4. **Run the application**
```bash
python backend/app.py
```

5. **Open in browser**
```
http://localhost:5000
```

---

## 📖 Usage

### 1. Risk Assessment

1. Navigate to "Predict Risk" page
2. Enter patient clinical data (13 parameters)
3. Click "Analyze Risk"
4. View results with:
   - Risk probability (0-100%)
   - Risk category (Low/Medium/High)
   - Detailed explanation
   - Identified risk factors
   - Personalized recommendations

### 2. Dashboard Analytics

View comprehensive analytics including:
- Risk distribution across patients
- Feature importance analysis
- Age and gender demographics
- Cholesterol and blood pressure trends
- Model performance metrics

---

## 🔍 Clinical Parameters

The system analyzes 13 clinical parameters:

1. **Age** - Patient age in years
2. **Gender** - Male/Female
3. **Chest Pain Type** - 4 categories
4. **Resting Blood Pressure** - In mmHg
5. **Cholesterol** - Serum cholesterol in mg/dL
6. **Fasting Blood Sugar** - >120 mg/dL
7. **Resting ECG** - Electrocardiogram results
8. **Max Heart Rate** - Maximum heart rate achieved
9. **Exercise Induced Angina** - Yes/No
10. **ST Depression** - Oldpeak value
11. **Slope** - ST segment slope
12. **Number of Major Vessels** - 0-4
13. **Thalassemia** - Blood disorder test

---

## 🔧 Technology Stack

### Backend
- **Flask** - Python web framework
- **scikit-learn** - Machine learning library
- **pandas** - Data manipulation
- **numpy** - Numerical computing

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling with modern gradients
- **JavaScript** - Interactivity
- **Chart.js** - Data visualization

### Machine Learning
- **Boosting-based Model** - Primary classifier
- **Random Forest** - Ensemble learning
- **StandardScaler** - Feature normalization
- **Cross-validation** - Model evaluation

---

## 📌 Final Conclusion

This project successfully demonstrates how **exploratory data analysis** and **machine learning** can be combined to predict heart attack risk.

By comparing multiple models and evaluating them carefully, a **boosting-based classifier** achieved approximately **92% accuracy**, making it the most suitable model for this task.

The project highlights the importance of:
- ✅ Data understanding
- ✅ Model comparison
- ✅ Clean system design in real-world machine learning applications

---

## ⚠️ Disclaimer

This system is for **educational and research purposes only**. It is a decision support tool and should not replace professional medical advice, diagnosis, or treatment. Always consult qualified healthcare professionals for medical decisions.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.




## 🙏 Acknowledgments

- Heart disease dataset from UCI Machine Learning Repository
- Chart.js for beautiful visualizations
- scikit-learn for machine learning tools
- Flask community for excellent documentation
<img width="1366" height="541" alt="image" src="https://github.com/user-attachments/assets/3e5e211e-6cd4-4f20-a6b2-e5e517e29676" />
<img width="690" height="487" alt="image" src="https://github.com/user-attachments/assets/7c5b43eb-be4a-4f2d-bcf2-1aedd387657a" />
<img width="582" height="588" alt="image" src="https://github.com/user-attachments/assets/c0d27c52-93e5-4882-aaa6-fa4d3bb53582" />
<img width="731" height="610" alt="image" src="https://github.com/user-attachments/assets/b25e4ae1-df0a-4352-aae2-dc5d67a07b00" />
<img width="527" height="606" alt="image" src="https://github.com/user-attachments/assets/b4df44a6-2b46-401a-9e89-f7b116c65a69" />






