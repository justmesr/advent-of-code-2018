class Line:
    def __init__(self, line):
        parts = line.split()

        self.id = parts[0][1:]

        start = parts[2].split(',')
        self.start_x = int(start[0])
        self.start_y = int(start[1][:-1])

        size = parts[3].split('x')
        self.size_x = int(size[0])
        self.size_y = int(size[1])

def fill(board, line, intact):
    for i in range(line.size_y):
        for j in range(line.size_x):
            if board[line.start_y + i][line.start_x + j] != 0:
                intact.discard(line.id)
                intact.discard(board[line.start_y + i][line.start_x + j])

            board[line.start_y + i][line.start_x + j] = line.id

def solve():
    board = [[0 for i in range(1000)] for j in range(1000)]
    intact = set()

    got = input()
    while got != 'end':
        line = Line(got)
        intact.add(line.id)
        fill(board, line, intact)
        got = input()

    for result in intact:
        return result

solution = solve()
print(solution)
