from fastapi import FastAPI
from scoreboard_services import generate_innings_summary

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Innings Summary API is running"}

@app.post("/innings/summary")
def innings_summary(payload: dict):
    innings_id = payload.get("innings_id")
    ball_events = payload.get("ball_events")

    if not innings_id or not ball_events:
        return {"error": "innings_id and ball_events are required"}

    summary = generate_innings_summary(innings_id, ball_events)
    return summary
