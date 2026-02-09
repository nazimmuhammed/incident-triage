from fastapi import FastAPI
from ai_engine import analyze_incident

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Incident Triage AI is running"}

@app.post("/analyze")
def analyze(incident: dict):
    result = analyze_incident(incident)
    return result
