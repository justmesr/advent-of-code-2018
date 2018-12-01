import requests

def load_numbers():
    numbers = []

    got = raw_input()
    while got != 'END':
        numbers.append(int(got))
        got = raw_input()

    return numbers

def find_duplicate(numbers):
    result = 0

    seen = set()
    seen.add(result)

    while True:
        for number in numbers:
            result += number

            if result in seen:
                return result

            seen.add(result)

def solve():
    numbers = load_numbers()
    result = find_duplicate(numbers)
    print(result)

solve()
