from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

stroke_model = joblib.load("model.joblib")

def predict_input(single_input):
    input_df = pd.DataFrame([single_input])
    encoded_cols, numeric_cols = stroke_model["encoded_cols"], stroke_model["numeric_cols"]
    preprocessor = stroke_model["preprocessor"]
    input_df[encoded_cols] = preprocessor.transform(input_df)
    X = input_df[numeric_cols + encoded_cols]
    prediction = stroke_model['model'].predict(X)
    return prediction


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/data", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        single_input = {
            "gender": data["gender"].lower(),
            "age": int(data["age"]),
            "hypertension": int(data["hypertension"]),
            "heart_disease": int(data["heart_disease"]),
            "ever_married": data["ever_married"].lower(),
            "work_type": data["work_type"],
            "Residence_type": data["residence_type"],
            "avg_glucose_level": float(data["avg_glucose_level"]),
            "bmi": float(data["bmi"]),
            "smoking_status": data["smoking_status"].lower(),
        }

        prediction = predict_input(single_input)
        result = "High Risk" if prediction[0] == 1 else "Low Risk"

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0")
#    serve(app, host="0.0.0.0", port=5000)