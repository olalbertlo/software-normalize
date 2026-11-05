def walk_points(laps: int) -> int:
    points = 0
    for _ in range(min(laps, 2)):
        points += 1
        if points == 2:
            points += 1
    return points
