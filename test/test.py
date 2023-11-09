from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

# Define the data model for input
class AttackPredictionInput(BaseModel):
    src_bytes: int
    dst_bytes: int
    same_srv_rate: float
    flag: int  # Assuming flag has already been converted to a numeric representation
    dst_host_srv_count: int
    dst_host_same_srv_rate: float
    logged_in: int
    diff_srv_rate: float
    count: int
    serror_rate: float

# Load the saved model
with open("C:\\Users\\ASUS\\Desktop\\BigData\\Final Project\\CODE\\test\\random_forest_classifier.pkl", 'rb') as file:
    model = pickle.load(file)

app = FastAPI()

# Define the API endpoint for attack prediction
@app.post('/predict_attack')
def predict_attack(input_data: AttackPredictionInput):
    try:
        # Extract the data in the correct order
        data = np.array([[
            input_data.src_bytes,
            input_data.dst_bytes,
            input_data.same_srv_rate,
            input_data.flag,
            input_data.dst_host_srv_count,
            input_data.dst_host_same_srv_rate,
            input_data.logged_in,
            input_data.diff_srv_rate,
            input_data.count,
            input_data.serror_rate
        ]])
        
        # Make prediction
        prediction = model.predict(data)
        class_prediction = model.predict_proba(data)
        
        # Assuming class '0' is 'not attack' and class '1' is 'attack'
        result = {
            'is_attack': bool(prediction[0]),
            'class_probabilities': {
                'not_attack': class_prediction[0][0],
                'attack': class_prediction[0][1]
            }
        }
        return result
    except:
        raise HTTPException(status_code=400, detail="Invalid input or model error")

# The code above would be in a file named main.py
# You would run this API with a command like `uvicorn main:app --reload`

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)