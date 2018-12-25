from sys import maxsize

def get_power_value(x, y, serial):
    rack_id = x + 10
    power_level = rack_id * y + serial
    hundreds_digit = ((power_level * rack_id) // 100) % 10
    return hundreds_digit - 5

def generate_grid(size, serial):
    grid = [[0 for j in range(size + 1)] for i in range(size + 1)]

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            grid[i][j] = get_power_value(j, i, serial)

    return grid

def make_prefix_grid(grid):
    prefix_grid = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            prefix_grid[i][j] = grid[i][j] + prefix_grid[i - 1][j] + prefix_grid[i][j - 1] - prefix_grid[i - 1][j - 1]

    return prefix_grid

def get_kernel_power_level(start, end, prefix_grid):
    x1, y1 = start
    x2, y2 = end
    return prefix_grid[y2][x2] - prefix_grid[y1 - 1][x2] - prefix_grid[y2][x1 - 1] + prefix_grid[y1 - 1][x1 - 1]

def find_biggest_kernel(prefix_grid):
    x, y, kernel_size = 0, 0, 1
    power_level = -maxsize

    for kernel in range(len(prefix_grid) - 1):

        for i in range(1, len(prefix_grid) - kernel):
            for j in range(1, len(prefix_grid) - kernel):

                kernel_power_level = get_kernel_power_level((j, i), (j + kernel, i + kernel), prefix_grid)
                if kernel_power_level > power_level:
                    power_level = kernel_power_level
                    x, y = j, i
                    kernel_size = kernel + 1

        print(f'{kernel / (len(prefix_grid) - 2) * 100:.1f}%')

    return (x, y, kernel_size)

def solve():
    size = 300

    serial = int(input())
    grid = generate_grid(size, serial)
    prefix_grid = make_prefix_grid(grid)
    result = find_biggest_kernel(prefix_grid)

    print(result)

solve()
