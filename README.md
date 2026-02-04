# 🌾 Crop Recommendation System using Machine Learning

A **Flask-based Machine Learning web application** that recommends the most suitable crop to cultivate based on **soil nutrients** and **environmental conditions**.  
The system uses a trained ML model and a clean, responsive web interface to provide **real-time crop recommendations**.

---

## 📌 Project Overview

Choosing the right crop based on soil composition and climate conditions is crucial for maximizing agricultural yield.  
This project leverages **Machine Learning** to analyze key parameters such as **NPK values, temperature, humidity, pH, and rainfall**, and recommends the most appropriate crop.

The model is trained on a crop recommendation dataset and deployed using **Flask**.

---

## ✨ Features

- 🌱 Crop recommendation based on soil & climate data  
- 🧠 Machine Learning–based prediction  
- 🌐 User-friendly web interface  
- ⚡ Real-time prediction  
- 📊 Proper data preprocessing using scalers  
- 🧩 Clean and modular project structure  

---

## 🛠️ Technologies Used

- **Python**
- **Flask** – Web framework
- **Scikit-learn** – Machine learning
- **NumPy** – Numerical computations
- **Bootstrap 5** – Frontend styling
- **HTML / CSS**

---

## 📂 Project Structure

Crop-Recommendation-System/
│
├── app.py # Flask application
├── README.md # Project documentation
├── requirements.txt # Dependencies
│
├── models/ # Trained ML artifacts
│ ├── model.pkl
│ ├── minmaxscaler.pkl
│ └── standscaler.pkl
│
├── data/ # Dataset & notebook
│ ├── Crop_recommendation.csv
│ └── Crop Classification With Recommendation.ipynb
│
├── templates/ # HTML templates
│ └── index.html
│
├── static/ # Static assets
│ └── img.jpg
│
└── venv/ # Virtual environment
---

## 📊 Dataset Description
-------------------------------
The dataset contains agricultural and environmental features used for crop recommendation.

### 🔹 Input Features
- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- pH
- Rainfall (mm)

### 🎯 Target
- Crop label (Rice, Maize, Cotton, Banana, etc.)

---

## 🧠 Machine Learning Workflow

1. Data collection and exploration  
2. Feature preprocessing and scaling  
3. Model training and evaluation  
4. Saving trained model and scalers (`.pkl`)  
5. Deployment using Flask  

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone or Download the Project
```bash
git clone <repository-url>
cd Crop-Recommendation-System
```

2️⃣ Create & Activate Virtual Environment

Windows
```
python -m venv venv
venv\Scripts\activate
```

macOS / Linux
```
python3 -m venv venv
source venv/bin/activate
```
3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
4️⃣ Run the Application
```
python app.py
```

5️⃣ Open in Browser
```
http://127.0.0.1:5000
```

###  Web Application
---------------
- Enter soil and climate parameters
- Click Get Recommendation
- The system displays the recommended crop instantly

### Notes
-----------
- Ensure the model and scaler files are present in the models/ folder
- Minor scikit-learn version warnings may appear but do not affect functionality
- This project uses Flask’s development server (not for production use)

### Future Enhancements
-------------
- Add prediction confidence score
- Improve UI with animations
- Add REST API endpoint
- Deploy on cloud platforms (Render / AWS / Railway)
- Add database for prediction history

### License
---------------
This project is intended for educational and research purposes.

### Acknowledgments
---------------------
- Crop Recommendation Dataset
- Scikit-learn Documentation
- Flask Framework
