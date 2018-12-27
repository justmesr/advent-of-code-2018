from collections import defaultdict

def load_configurations():
    configurations = defaultdict(lambda: '.')

    got = input()
    while got.lower() != 'end':
        configuration_parts = got.split() #...## => #
        configurations[configuration_parts[0]] = configuration_parts[2]
        got = input()

    return configurations

def load_input():
    state = input().split()[2] # initial state: ####..##.##..##..#..###..#
    input() # empty_line
    configurations = load_configurations() # ...## => #

    return (state, configurations)

def iteration(state, first_pot, configurations):
    new_state = ''
    config = '.....'

    for pot in state:
        config = config[1:] + pot
        new_state += configurations[config]
    for _ in range(4):
        config = config[1:] + '.'
        new_state += configurations[config]

    new_first_pot = first_pot + new_state.find('#') - 2
    return (new_state.strip('.'), new_first_pot)

def get_state_value(state, first_pot):
    result = 0

    for i, pot in enumerate(state):
        if pot == '#':
            result += i + first_pot

    return result

def solve():
    state, configurations = load_input()
    first_pot = 0

    for i in range(20):
        state, first_pot = iteration(state, first_pot, configurations)

    return get_state_value(state, first_pot)

result = solve()
print(result)
