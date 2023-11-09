from flask import Flask, request, jsonify
import pickle
import numpy as np
app = Flask(__name__)

# Load the model and label encoder
with open("C:\\Users\\ASUS\\Desktop\\BigData\\Final Project\\CODE\\test\\logistic_regression_model.pkl", 'rb') as model_file:
    model = pickle.load(model_file)

with open("C:\\Users\\ASUS\\Desktop\\BigData\\Final Project\\CODE\\test\\label_encoder.pkl", 'rb') as encoder_file:
    label_encoder = pickle.load(encoder_file)

# Define the API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON from the POST request
    data = request.get_json()

    # Validate and transform the input data
    # In a production environment, you should add proper validation here
    input_data = np.array([[
        data['flag_S0'],
        data['flag_SF'],
        data['src_bytes'],
        data['dst_bytes'],
        data['logged_in'],
        data['count'],
        data['serror_rate'],
        data['srv_serror_rate'],
        data['dst_host_srv_count'],
        data['dst_host_same_srv_rate'],
        data['dst_host_diff_srv_rate'],
        data['dst_host_same_src_port_rate'],
        data['dst_host_serror_rate'],
        data['dst_host_srv_serror_rate']
    ]])

    # Make prediction
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    # Convert prediction to label
    attack_label = label_encoder.inverse_transform(prediction)

    # Create response data
    response = {
        'probability_of_attack': prediction_proba.max(),
        'type_of_attack': attack_label[0]
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)