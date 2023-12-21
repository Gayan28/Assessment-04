# app.py (Flask application)
from flask import Flask, request, jsonify
import numpy as np
from sklearn.your_custom_module import YourCustomModel  # Import your custom model

app = Flask(_name_)
model = MLAssesment4()  # Replace with the actual instantiation of your model

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array(data['features'])
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if _name_ == '_main_':
    app.run(port=5000)