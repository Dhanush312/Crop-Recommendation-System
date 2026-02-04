from flask import Flask, request, render_template
import numpy as np
import pickle

# -------------------- Load model & scalers --------------------
model = pickle.load(open("models/model.pkl", "rb"))
minmax_scaler = pickle.load(open("models/minmaxscaler.pkl", "rb"))
standard_scaler = pickle.load(open("models/standscaler.pkl", "rb"))

# -------------------- Flask app --------------------
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # -------- Read & convert inputs --------
        nitrogen = float(request.form["nitrogen"])
        phosphorus = float(request.form["phosphorus"])
        potassium = float(request.form["potassium"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # -------- Feature array --------
        features = np.array([
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        ]).reshape(1, -1)

        # -------- Apply same preprocessing as training --------
        features_scaled = minmax_scaler.transform(features)
        features_scaled = standard_scaler.transform(features_scaled)

        # -------- Prediction --------
        prediction = model.predict(features_scaled)[0]

        # -------- Handle prediction output --------
        if isinstance(prediction, (str, np.str_)):
            crop_name = prediction
        else:
            crop_dict = {
                1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton",
                5: "Coconut", 6: "Papaya", 7: "Orange", 8: "Apple",
                9: "Muskmelon", 10: "Watermelon", 11: "Grapes",
                12: "Mango", 13: "Banana", 14: "Pomegranate",
                15: "Lentil", 16: "Blackgram", 17: "Mungbean",
                18: "Mothbeans", 19: "Pigeonpeas",
                20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
            }
            crop_name = crop_dict.get(prediction, "Unknown crop")

        result = f"{crop_name} is the best crop to be cultivated in these conditions."

        return render_template("index.html", result=result)

    except Exception as e:
        error_message = "Invalid input or prediction error. Please check your values."
        return render_template("index.html", result=error_message)


# -------------------- Run app --------------------
if __name__ == "__main__":
    app.run(debug=True)
