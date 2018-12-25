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

def get_kernel_power_level(y, x, kernel_size, grid):
    result = 0

    for i in range(kernel_size):
        for j in range(kernel_size):
            result += grid[y + i][x + j]

    return result

def find_biggest_kernel(grid, kernel_size):
    x, y = 0, 0
    power_level = -maxsize

    for i in range(1, len(grid) - kernel_size + 1):
        for j in range(1, len(grid[0]) - kernel_size + 1):
            kernel_power_level = get_kernel_power_level(i, j, kernel_size, grid)
            if kernel_power_level > power_level:
                power_level = kernel_power_level
                x, y = j, i

    return (x, y)

def solve():
    size = 300
    kernel_size = 3

    serial = int(input())
    grid = generate_grid(size, serial)
    result = find_biggest_kernel(grid, kernel_size)

    print(result)

solve()
