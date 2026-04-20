def generate_innings_summary(innings_id, ball_events):
    total_runs = 0
    wickets = 0
    legal_balls = 0

    batters = {}
    bowlers = {}

    recent_balls = ball_events[-6:]

    for ball in ball_events:
        runs = ball.get("runs", 0)
        batter = ball.get("batter")
        bowler = ball.get("bowler")
        is_wicket = ball.get("is_wicket", False)
        extra_type = ball.get("extra_type")

        total_runs += runs

        if not extra_type:  # legal delivery
            legal_balls += 1

        if is_wicket:
            wickets += 1

        # Batter stats
        if batter not in batters:
            batters[batter] = {"runs": 0, "balls": 0}

        batters[batter]["runs"] += runs
        if not extra_type:
            batters[batter]["balls"] += 1

        # Bowler stats
        if bowler not in bowlers:
            bowlers[bowler] = {"runs_conceded": 0, "balls": 0, "wickets": 0}

        bowlers[bowler]["runs_conceded"] += runs
        if not extra_type:
            bowlers[bowler]["balls"] += 1
        if is_wicket:
            bowlers[bowler]["wickets"] += 1

    overs = f"{legal_balls // 6}.{legal_balls % 6}"
    run_rate = round((total_runs / legal_balls) * 6, 2) if legal_balls > 0 else 0

    return {
        "innings_id": innings_id,
        "total_runs": total_runs,
        "wickets": wickets,
        "overs": overs,
        "run_rate": run_rate,
        "batters": batters,
        "bowlers": bowlers,
        "recent_balls": recent_balls
    }
