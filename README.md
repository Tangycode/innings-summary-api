innings-summary-api
#Innings Summary API

#Overview
This API generates a complete statistical summary of a cricket innings using ball-by-ball event data. It is designed to be integration-ready for the Khel AI MVP system.

#Endpoint
POST /innings/summary

#Input Format
{
  "innings_id": "match_001_innings_1",
  "ball_events": [
    {
      "runs": 4,
      "batter": "Player A",
      "bowler": "Player X",
      "is_wicket": false,
      "extra_type": null
    }
  ]
}

#Output
- Total runs
- Wickets
- Overs
- Run rate
- Batter statistics
- Bowler statistics
- Recent balls

Improvements from Phase 1
- Removed hardcoded demo data
- Introduced service-layer logic
- Made API payload-driven
- Structured output for frontend usage
