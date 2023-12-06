import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle as pkl
import requests
import os

def main():
    st.title("Iris Species Prediction")
    sepal_length = st.slider("Sepal Length", 0.0, 10.0, 5.0)
    sepal_width = st.slider("Sepal Width", 0.0, 10.0, 5.0)
    petal_length = st.slider("Petal Length", 0.0, 10.0, 5.0)
    petal_width = st.slider("Petal Width", 0.0, 10.0, 5.0)

    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    use_api = st.checkbox("Use API")

    if st.button("Predict"):
        predict(features, use_api)


def get_api_url():
    api_url = os.environ.get("API_URL", None)
    if api_url is None:
        raise ValueError("API_URL environment variable is not set")
    return api_url


def predict(features, use_api):
    if use_api:
        api_url = get_api_url()
        response = requests.post(api_url, json=features)
        data = response.json()
        species = data["species"]
    else:
        model = load_model()
        encoder = load_encoder()
        prediction = model.predict(features)
        species = encoder.inverse_transform(prediction)[0]
    st.success(f"Predicted Species: {species}")


def load_model():
    with open("model.pkl", "rb") as f:
        model: RandomForestClassifier = pkl.load(f)
    return model


def load_encoder():
    with open("encoder.pkl", "rb") as f:
        encoder: LabelEncoder = pkl.load(f)
    return encoder


if __name__ == "__main__":
    main()
