def validate_request(req):
    if not req.innings_id:
        raise ValueError("Missing innings_id")

    if req.ball_events is None:
        raise ValueError("ball_events must be provided")

    if len(req.ball_events) == 0:
        raise ValueError("Empty innings: no ball events")

def calculate_total_runs(balls):
    return sum(b.runs for b in balls)

def calculate_wickets(balls):
    return sum(1 for b in balls if b.wicket)

def calculate_legal_balls(balls):
    return sum(1 for b in balls if b.legal)

def calculate_overs(legal_balls):
    return f"{legal_balls // 6}.{legal_balls % 6}"

def calculate_run_rate(total_runs, legal_balls):
    return round(total_runs / (legal_balls / 6), 2) if legal_balls else 0

def group_by_batter(balls):
    result = {}
    for b in balls:
        if not b.batter:
            continue
        result.setdefault(b.batter, {"runs": 0})
        result[b.batter]["runs"] += b.runs
    return result

def group_by_bowler(balls):
    result = {}
    for b in balls:
        if not b.bowler:
            continue
        result.setdefault(b.bowler, {"runs": 0, "wickets": 0})
        result[b.bowler]["runs"] += b.runs
        if b.wicket:
            result[b.bowler]["wickets"] += 1
    return result

def get_top_batter(batters):
    return max(batters, key=lambda x: batters[x]["runs"]) if batters else None

def get_top_bowler(bowlers):
    return max(bowlers, key=lambda x: bowlers[x]["wickets"]) if bowlers else None

def get_recent_balls(balls):
    return balls[-6:]

def get_innings_summary(req):
    validate_request(req)

    balls = req.ball_events

    total_runs = calculate_total_runs(balls)
    wickets = calculate_wickets(balls)
    legal_balls = calculate_legal_balls(balls)

    if legal_balls == 0:
        raise ValueError("Invalid innings: zero legal balls")

    overs = calculate_overs(legal_balls)
    run_rate = calculate_run_rate(total_runs, legal_balls)

    batters = group_by_batter(balls)
    bowlers = group_by_bowler(balls)

    return {
        "match_id": req.match_id,
        "innings_id": req.innings_id,
        "total_runs": total_runs,
        "wickets": wickets,
        "legal_balls": legal_balls,
        "overs": overs,
        "run_rate": run_rate,
        "batters": batters,
        "bowlers": bowlers,
        "top_batter": get_top_batter(batters),
        "top_bowler": get_top_bowler(bowlers),
        "recent_balls": get_recent_balls(balls)
    }
