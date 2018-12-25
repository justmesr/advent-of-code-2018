from tkinter import *
from time import sleep
from sys import maxsize
from math import floor

class Point:
    def __init__(self, position, velocity):
        self.x = position[0]
        self.y = position[1]
        self.speed_x = velocity[0]
        self.speed_y = velocity[1]

# position=<-30052,  -9918> ...
def parse_attribute(line):
    line = line[line.find('<') + 1:] # -30052,  -9918> ...

    comma = line.find(',')
    x = int(line[:comma]) # -30052
    line = line[comma + 1:] # -9918> ...

    close_bracket = line.find('>')
    y = int(line[:close_bracket]) # -9918
    line = line[close_bracket + 1:] # ...

    return (x, y, line)

# position=<-30052,  -9918> velocity=< 3,  1>
def parse_line(line):
    x, y, line = parse_attribute(line)
    velocity_x, velocity_y, line = parse_attribute(line)

    return ((x, y), (velocity_x, velocity_y))

def load_points():
    points = []

    got = input()
    while got.lower() != 'end':
        position, velocity = parse_line(got)
        point = Point(position, velocity)
        points.append(point)

        got = input()

    return points

def create_canvas(width, height):
    window = Tk()
    canvas = Canvas(window, bg='white', height=height, width=width)
    canvas.pack()

    image = PhotoImage(width=width, height=height)
    canvas.create_image((width / 2, height / 2), image=image, state='normal')

    return (image, canvas)

def bounding_box(points):
    min_x, min_y = maxsize, maxsize
    max_x, max_y = -maxsize, -maxsize

    for point in points:
        min_x = min(min_x, point.x)
        min_y = min(min_y, point.y)
        max_x = max(max_x, point.x)
        max_y = max(max_y, point.y)

    return ((min_x, min_y), (max_x, max_y))

def average_position(points):
    sum_x = 0
    sum_y = 0

    for point in points:
        sum_x += point.x
        sum_y += point.y

    return (sum_x / len(points), sum_y / len(points))

def get_close_to_average(points, width, height):
    average = average_position(points)

    result = []

    for point in points:
        if abs(point.x - average[0]) < (width // 2) and abs(point.y - average[1]) < (height // 2):
            result.append(point)

    return result

def update_image(points, image, canvas, width, height, iteration):
    start, end = bounding_box(points)

    image.blank()
    for point in points:
        x = floor((point.x - start[0]) / max(end[0] - start[0], 0.1) * width)
        y = floor((point.y - start[1]) / max(end[1] - start[0], 0.1) * height)

        if x >= 0 and y >= 0 and x < width and y < height:
            image.put('black', (x, y))

    canvas.update()
    if iteration > 10060:
        image.write(f'test{iteration}.png', format='png')

def step(points, image, canvas, width, height, iteration):
    filtered_points = get_close_to_average(points, width, height)
    update_image(filtered_points, image, canvas, width, height, iteration)

    for point in points:
        point.x += point.speed_x
        point.y += point.speed_y

def solve():
    width = 350
    height = 350

    points = load_points()
    image, canvas = create_canvas(width, height)

    for i in range(100000):
        step(points, image, canvas, width, height, i)

solve()
