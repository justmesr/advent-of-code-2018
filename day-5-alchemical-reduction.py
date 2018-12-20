from sys import maxsize

def solve():
    polymer = input()
    signs = set(polymer.lower())

    result = maxsize
    for sign in signs:
        stack = []
        for char in polymer:
            if char.lower() == sign:
                continue

            if len(stack) == 0 or abs(ord(stack[-1]) - ord(char)) != abs(ord('A') - ord('a')):
                stack.append(char)
            else:
                stack.pop()

        result = min(result, len(stack))

    print(result)

solve()
