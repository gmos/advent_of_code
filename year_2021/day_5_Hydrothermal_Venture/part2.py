from plane import Point, Line, Plane, update_plane


def run(lines: list[Line], day, name):
    """Compute the solution for part 2."""

    plane: Plane = {}

    def all_points_on_line(line: Line) -> list[Point]:
        start_point, end_point = (
            line if line.start.x < line.end.x else Line(line.end, line.start)
        )  # Always left to right

        sx, sy = start_point
        ex, ey = end_point

        if sx == ex:
            # Vertical
            sy, ey = (sy, ey) if ey > sy else (ey, sy)
            return [Point(sx, y) for y in range(sy, ey + 1)]

        if sy == ey:
            # horizontal
            return [Point(x, sy) for x in range(sx, ex + 1)]

        # diagonal
        y_step = 1 if ey > sy else -1
        return [
            Point(x, y)
            for x, y in zip(range(sx, ex + 1), range(sy, ey + y_step, y_step))
        ]

    for line in lines:
        for point in all_points_on_line(line):
            update_plane(point, plane)

    n_danger_points = len([p for p in plane.values() if p > 1])

    print(f"== Results for day {day} - {name}, part 2.")
    print(f"   {n_danger_points=}")
