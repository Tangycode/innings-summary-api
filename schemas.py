from pydantic import BaseModel
from typing import List, Optional

class BallEvent(BaseModel):
    runs: int
    batter: Optional[str]
    bowler: Optional[str]
    legal: bool
    wicket: bool

class InningsRequest(BaseModel):
    match_id: Optional[str]
    innings_id: Optional[str]
    teams: Optional[List[str]]
    players: Optional[List[str]]
    ball_events: Optional[List[BallEvent]]
