from sys import maxsize
from math import ceil
from collections import namedtuple
from queue import Queue

Point = namedtuple('Point', 'x, y')

def load_points():
    points = []

    got = input()
    while got.lower() != 'end':
        coordinates = list(map(int, got.split(',')))
        point = Point(coordinates[0], coordinates[1])
        points.append(point)

        got = input()

    return points

def point_distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y)

def biggest_distance(points):
    result = 0

    for point_from in points:
        for point_to in points:
            distance = point_distance(point_from, point_to)
            result = max(result, distance)

    return result

def get_bounding_box(points):
    start = Point(maxsize, maxsize)
    end = Point(-maxsize, -maxsize)

    for point in points:
        start = Point(min(start.x, point.x), min(start.y, point.y))
        end = Point(max(end.x, point.x), max(end.y, point.y))

    return (start, end)

def offset_points(points, bounding_box, iterations):
    result = []

    offset = Point(
        - (bounding_box[0].x - iterations),
        - (bounding_box[0].y - iterations)
    )

    new_bounding_box = (
        Point(0, 0),
        Point(bounding_box[1].x + iterations + offset.x + 1, bounding_box[1].y + iterations + offset.y + 1)
    )

    for point in points:
        moved_point = Point(point.x + offset.x, point.y + offset.y)
        result.append(moved_point)

    return (result, new_bounding_box)

def in_bounds(plane, point):
    return point.x >= 0 and point.y >= 0 and point.x < len(plane[0]) and point.y < len(plane)

def bfs(start, id,  plane, distances, used):
    directions = (Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1))

    queue = Queue()
    queue.put([0, start])

    while not queue.empty():
        distance, current = queue.get()
        x = current.x
        y = current.y

        plane[y][x] = id if distances[y][x] > distance else '.'
        distances[y][x] = distance

        for direction in directions:
            new_distance = distance + 1
            new_point = Point(x + direction.x, y + direction.y)

            if in_bounds(plane, new_point) and not used[new_point.y][new_point.x] and distances[new_point.y][new_point.x] >= new_distance:
                used[new_point.y][new_point.x] = True
                queue.put([new_distance, new_point])

def get_plane(points, bounding_box):
    plane = [['.' for i in range(bounding_box[1].x)] for j in range(bounding_box[1].y)]
    distances = [[maxsize for i in range(bounding_box[1].x)] for j in range(bounding_box[1].y)]

    for i in range(len(points)):
        point = points[i]
        used = [[False for i in range(bounding_box[1].x)] for j in range(bounding_box[1].y)]
        bfs(point, chr(ord('a') + i), plane, distances, used)

    return plane

def analyze_plane(plane):
    infinite = set()
    area = {}

    for y in range(len(plane)):
        for x in range(len(plane[0])):
            char = plane[y][x]

            if char not in area:
                area[char] = 0

            area[char] += 1

            if x == 0 or y == 0 or x + 1 == len(plane[0]) or y + 1 == len(plane):
                infinite.add(char)

    area.pop('.')
    return (infinite, area)

def find_biggest_finite_area(plane):
    result = 0

    infinite, area = analyze_plane(plane)
    for char, size in area.items():
        if char not in infinite:
            result = max(result, size)

    return result

def solve():
    points = load_points()
    distance = biggest_distance(points)
    needed_iterations = ceil(distance / 2)
    bounding_box = get_bounding_box(points)
    moved_points, new_bounding_box = offset_points(points, bounding_box, needed_iterations)
    plane = get_plane(moved_points, new_bounding_box)
    result = find_biggest_finite_area(plane)
    print(result)

def get_near(points, bounding_box, limit):
    result = 0

    for y in range(bounding_box[0].y, bounding_box[1].y + 1):
        for x in range(bounding_box[0].x, bounding_box[1].x + 1):
            distance = 0

            current = Point(x, y)
            for point in points:
                distance += point_distance(current, point)

            if distance < limit:
                result += 1

    return result

def solve_bonus():
    points = load_points()
    bounding_box = get_bounding_box(points)
    result = get_near(points, bounding_box, 10000)
    print(result)

solve_bonus()
