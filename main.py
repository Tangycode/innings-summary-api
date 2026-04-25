from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import InningsRequest
from services import get_innings_summary

app = FastAPI(title="Innings Summary API")

# CORS (MANDATORY)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Innings Summary API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/innings/summary")
def innings_summary(req: InningsRequest):
    try:
        return get_innings_summary(req)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
