from collections import namedtuple

Point = namedtuple("Point", "x y")
Line = namedtuple("Line", "start end")
Plane = dict[Point, int]


def update_plane(point: Point, plane: Plane) -> None:
    """Add a point with count 0 to the sparse plane if required.
    And then increment the count for the point."""
    plane[point] = plane.get(point, 0) + 1
