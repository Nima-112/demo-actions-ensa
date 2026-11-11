from fastapi import FastAPI
from model import predict_square

app = FastAPI(title="Demo IA API")

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction"}

@app.get("/predict/{number}")
def predict(number: float):
    result = predict_square(number)
    return {"input": number, "prediction": result}