SAMPLE_INPUT_FILE = "sample_input_day_10_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_10_aoc21.txt"


def input_file_puzzle_input(dir_file: str) -> list:
    """
    Args:
        dir_file (str): location of .txt file to pull data from

    Returns:
        end points values in [[x1, y1], [x2, y2]] format for lines defined in input file
    """

    with open(dir_file, "r") as file:
        content = file.read().splitlines()

        return content


def calc(i):
    # chunks = {'(': 0, '[': 0, '{': 0, '<': 0, ')': 0, ']': 0, '}': 0, '>': 0}
    open = ['(', '[', '{', '<']
    close = [')', ']', '}', '>']

    expected = ''
    for ch in i:
        if ch in open:
            expected = convert_open_to_close(ch) + expected
        elif ch == expected[0]:
            expected = expected[1:]
        else:
            return det_score(ch)
    return 0

def calc3(i):
    # chunks = {'(': 0, '[': 0, '{': 0, '<': 0, ')': 0, ']': 0, '}': 0, '>': 0}
    open = ['(', '[', '{', '<']
    close = [')', ']', '}', '>']
    expected = ''
    for ch in i:
        if ch in open:
            expected = convert_open_to_close(ch) + expected
        elif ch == expected[0]:
            if len(expected) <= 1:
                expected = ''
            else:
                expected = expected[1:]
    print(i, expected)
    return det_auto_score(expected)

def convert_open_to_close(a):

    if a == '(':
        return ')'
    if a == '[':
        return ']'
    if a == '{':
        return '}'
    if a == '<':
        return '>'

    return False

def det_score(a):
    if a == ')':
        return 3
    if a == ']':
        return 57
    if a == '}':
        return 1197
    if a == '>':
        return 25137

    return 0

def det_auto_score(a):
    score = 0
    for b in a:
        if b == ')':
            score = score * 5 + 1
        if b == ']':
            score = score * 5 + 2
        if b ==' }':
            score = score * 5 + 3
        if b == '>':
            score = score * 5 + 4
    return score

def calc2(arr):
    score = []
    for item in arr:
        output = calc3(item)
        if output:
            score.append(output)
    print(sorted(score))
    return sorted(score)[int(len(score)/2)]

sample_input = input_file_puzzle_input(SAMPLE_INPUT_FILE)
# puzzle_input = input_file_puzzle_input(PUZZLE_INPUT_FILE)
sample_output = calc2(sample_input)
# puzzle_output = calc2(puzzle_input)

print(sample_output)
# print(puzzle_output)