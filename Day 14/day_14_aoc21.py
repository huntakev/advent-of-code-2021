SAMPLE_INPUT_FILE = "sample_input_day_14_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_14_aoc21.txt"
NUM_STEPS = 40

def parse_input(dir_file: str) -> tuple[str, list]:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:

    """

    with open(dir_file, "r") as file:
        content = list(filter(None, (line.strip() for line in file)))
        return content[0], [list([i.split(" -> ")[0], i.split(" -> ")[1]]) for i in content[1:]]


def polymerize(temp: str, rules: list, steps: int) -> list:
    current_polymer = temp
    # print(temp)
    for step in range(steps):
        next_polymer = ''
        for index in range(len(current_polymer) - 1):
            if current_polymer[index] + current_polymer[index+1] not in [rule[0] for rule in rules]:
                next_polymer = next_polymer + current_polymer[index]
                # print(next_polymer, 'KEEP')
            else:
                for rule in rules:
                    if current_polymer[index] + current_polymer[index+1] == rule[0]:
                        next_polymer = next_polymer + current_polymer[index] + rule[1]
                        # print(next_polymer, 'PAIR', rule[0], 'ADD', rule[1])
            if index == len(current_polymer) - 2:
                next_polymer = next_polymer + current_polymer[index + 1]
                # print(next_polymer, 'LAST')
                break
        current_polymer = next_polymer[:]

    return current_polymer


def blind_polymerize(temp: str, rules: list, steps: int) -> int:
    rule_trigger = {}
    counter = {}
    for rule in rules:
        rule_trigger[rule[0]] = 0

    for index in range(len(temp) - 1):
        for key in rule_trigger.keys():
            if temp[index] + temp[index+1] == key:
                rule_trigger[key] += 1

    for step in range(steps):


    print(rule_trigger)

def common_uncommon_difference(poly: str) -> int:
    counter = {}
    for letter in poly:
        if letter in counter.keys():
            counter[letter] += 1
        else:
            counter[letter] = 1
    # print(poly)
    # print(counter)
    return max(counter.values()) - min(counter.values())


polymer_template, pair_insertion_rules = parse_input(PUZZLE_INPUT_FILE)
polymer = blind_polymerize(polymer_template, pair_insertion_rules, NUM_STEPS)
# puzzle_output = common_uncommon_difference(polymer)

print(polymer)