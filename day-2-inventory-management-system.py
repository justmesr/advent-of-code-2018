def cut(word_a, word_b):
    result = ''

    for a, b in zip(word_a, word_b):
        if a == b:
            result += a

    return result

def similiar(word_a, word_b):
    one_wrong = False

    for a, b in zip(word_a, word_b):
        if a != b:
            if one_wrong:
                return False
            else:
                one_wrong = True

    return True

def find_similiar(words):
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if similiar(words[i], words[j]):
                return cut(words[i], words[j])

    return None

def load_input():
    result = []

    got = input()
    while got != 'END':
        result.append(got)
        got = input()

    return result

def solve():
    got = load_input()
    return find_similiar(got)

solution = solve()
print(solution)
