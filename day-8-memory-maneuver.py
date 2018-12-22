# children added child_1, child_2 .. child_children value_1 value_2 .. value_added
def tree_sum(cursor, values):
    result = 0

    children = values[cursor]
    cursor += 1

    added = values[cursor]
    cursor += 1

    for _ in range(children):
        cursor, added_sum = tree_sum(cursor, values)
        result += added_sum

    for _ in range(added):
        result += values[cursor]
        cursor += 1

    return (cursor, result)

def solve():
    values = list(map(int, input().split()))
    result = tree_sum(0, values)
    print(result[1])

solve()
