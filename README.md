Purpose

Provides a reusable innings summary object for all downstream cricket analytics APIs.

Endpoint

POST /innings/summary

Input Schema
match_id (string)
innings_id (string) required
teams (list)
players (list)
ball_events (list) required
Output Schema
match_id
innings_id
total_runs
wickets
legal_balls
overs
run_rate
batters
bowlers
top_batter
top_bowler
recent_balls
Sample Request
{
  "match_id": "M001",
  "innings_id": "I001",
  "ball_events": [...]
}
Sample Response
{
  "match_id": "M001",
  "innings_id": "I001",
  "total_runs": 14,
  "wickets": 1,
  "legal_balls": 6,
  "overs": "1.0",
  "run_rate": 14.0,
  "top_batter": "C"
}
Validation Errors (400)
Missing innings_id
Missing ball_events
Empty innings
Zero legal balls
Integration Notes
Output is stable and reusable across scoreboard, momentum, and over-summary APIs
Designed for frontend-ready direct consumption
