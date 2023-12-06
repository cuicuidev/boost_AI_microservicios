from fastapi import FastAPI
from pydantic import BaseModel
import pickle as pkl
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

class RequestForm(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class PredictionForm(BaseModel):
    species: str
    
def get_prediction(data: RequestForm):
    model = load_model()
    prediction = model.predict([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    encoder = load_encoder()
    prediction = encoder.inverse_transform(prediction)[0]
    return prediction

def load_model():
    with open('model.pkl', 'rb') as f:
        model: RandomForestClassifier = pkl.load(f)
    return model

def load_encoder():
    with open('encoder.pkl', 'rb') as f:
        encoder: LabelEncoder = pkl.load(f)
    return encoder

###############################################################################################################

app = FastAPI()

@app.post("/predict")
async def predict(data: RequestForm):
    prediction = get_prediction(data)
    response = PredictionForm(species=prediction)
    return response