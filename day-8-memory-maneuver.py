# children added child_1, child_2 .. child_children value_1 value_2 .. value_added
def tree_sum(cursor, values):
    result = 0

    children = values[cursor]
    cursor += 1

    added = values[cursor]
    cursor += 1

    child = [0] * children
    for i in range(children):
        cursor, child[i] = tree_sum(cursor, values)

    for _ in range(added):
        metadata = values[cursor]

        if children == 0:
            result += metadata
        elif metadata > 0 and metadata <= children:
            result += child[metadata - 1]

        cursor += 1

    return (cursor, result)

def solve():
    values = list(map(int, input().split()))
    result = tree_sum(0, values)
    print(result[1])

solve()
