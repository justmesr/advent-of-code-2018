def solve():
    words = input().split()
    players = int(words[0])
    marbles = int(words[6])

    score = [0] * players

    circle = [0]
    position = 0
    for i in range(1, marbles + 1):
        position = (position + 2) % len(circle)
        if position == 0:
            position = len(circle)

        if i % 23 != 0:
            circle.insert(position, i)

        else:
            player = (i - 1) % players
            score[player] += i

            position = position - 9
            if position < 0:
                position = len(circle) + position
            score[player] += circle[position]
            circle.pop(position)

    return max(score)

result = solve()
print(result)
