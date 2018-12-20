# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
# [1518-11-02 00:50] wakes up
# [1518-11-03 00:05] Guard #10 begins shift
# [1518-11-03 00:24] falls asleep
# [1518-11-03 00:29] wakes up
# [1518-11-04 00:02] Guard #99 begins shift
# [1518-11-04 00:36] falls asleep
# [1518-11-04 00:46] wakes up
# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up

from collections import namedtuple
from functools import cmp_to_key

Line = namedtuple('Line', ['date', 'time', 'command'])

# [1518-11-01 00:00] Guard #10 begins shift
def parse_line(line):
    line = line[1:] # [

    first_space = line.find(' ')
    date = line[:first_space] # 1518-11-01
    line = line[first_space + 1:]

    last_bracket = line.find(']')
    time = line[:last_bracket] # 00:00
    line = line[last_bracket + 2:]

    command = line # Guard #10 begins shift

    return Line(date, time, command)

def load_input():
    lines = []

    got = input()
    while got.lower() != 'end':
        lines.append(parse_line(got))
        got = input()

    return lines

def sort_by_timestamp(lines):
    def compare(line1, line2):
        if line1.date < line2.date:
            return -1
        if line1.date > line2.date:
            return 1

        if line1.time < line2.time:
            return -1
        else:
            return 1

    return sorted(lines, key=cmp_to_key(compare))

# Guard #10 begins shift
def parse_guard_id(command):
    sharp = command.find('#')
    command = command[sharp + 1:] # 10 begins shift

    space = command.find(' ')
    command = command[:space] # 10

    return int(command)

def group_by_id(lines):
    groups = {}

    guard_id = -1
    for line in lines:

        if line.command.startswith('Guard'):
            guard_id = parse_guard_id(line.command)

        if guard_id not in groups:
            groups[guard_id] = []

        groups[guard_id].append(line)

    return groups

def slept_during_shift(slept, lines):
    current_minute = 0

    for line in lines:
        time_parts = line.time.split(':')
        minute = int(time_parts[1])

        if line.command.startswith('falls'):
            current_minute = minute

        elif line.command.startswith('wakes'):
            for minute in range(current_minute, minute):
                slept[minute] += 1

def slept_by_guard(groups):
    result = {}

    for guard_id, lines in groups.items():
        if guard_id not in result:
            result[guard_id] = [0] * 60

        slept = result[guard_id]
        slept_during_shift(slept, lines)

    return result

def get_slept_during(slept_times):
    result = 0

    for i in range(len(slept_times)):
        if slept_times[i] > slept_times[result]:
            result = i

    return result

def get_most_slept(slept):
    most_slept = 0
    slept_during = 0
    guard = 0

    for guard_id, slept_times in slept.items():
        currently_slept = sum(slept_times)
        if currently_slept > most_slept:
            most_slept = currently_slept
            guard = guard_id
            slept_during = get_slept_during(slept_times)

    return slept_during, guard

def solve():
    lines = load_input()
    ordered = sort_by_timestamp(lines)
    grouped = group_by_id(ordered)
    slept = slept_by_guard(grouped)
    sleeper, minute_slept = get_most_slept(slept)

    print(f'id: {sleeper}, minute: {minute_slept}')
    print(sleeper * minute_slept)

solve()
