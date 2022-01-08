from math import floor, ceil
from itertools import permutations

SAMPLE_INPUT_FILE = "sample_input_day_18_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_18_aoc21.txt"
NUM_UNCLOSED_BRACKETS_TO_EXPLODE = 5
NUM_MAX_REGULAR_FOR_SPLIT = 10


def parse_input(dir_file: str) -> list:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:

    """

    with open(dir_file, "r") as file:
        # return [eval(i) for i in file.read().split()]
        return file.read().split()


def add_snailfish_numbers(sf_nums: list) -> str:

    for counter in range(len(sf_nums)-1):
        # print(sf_nums[0])
        sf_nums[0] = reduce("[" + sf_nums[0] + "," + sf_nums[1] + "]")
        sf_nums.pop(1)

    return sf_nums[0]


def reduce(to_reduce: str) -> str:
    while True:
        flag = True
        num_unclosed_brackets = 0
        value = ''
        # print(to_reduce)
        for char_index in range(len(to_reduce)):
            if to_reduce[char_index] == "[":
                num_unclosed_brackets += 1
            elif to_reduce[char_index] == "]":
                num_unclosed_brackets -= 1

            if num_unclosed_brackets >= NUM_UNCLOSED_BRACKETS_TO_EXPLODE:
                to_reduce = snailfish_explode(to_reduce, char_index)
                flag = False
                # print("EXPLODE")
                break

        if flag:
            for char_index in range(len(to_reduce)):
                if to_reduce[char_index].isnumeric():
                    value += to_reduce[char_index]

                if int(value if value else 0) >= NUM_MAX_REGULAR_FOR_SPLIT and not to_reduce[char_index].isnumeric():
                    to_reduce = snailfish_split(to_reduce, char_index - len(value), value)
                    flag = False
                    # print("SPLIT")
                    break

                if value != '' and not to_reduce[char_index].isnumeric():
                    value = ''

        if flag:
            return to_reduce


def snailfish_explode(num: str, index: int) -> str:
    left_index = index
    right_index = index + num[left_index:].index("]")
    pair = eval(num[left_index:right_index + 1])
    num = num[:left_index] + '0' + num[right_index+1:]

    right_index = left_index + 1
    right_val = ''
    left_index -= 1
    left_val = ''

    while right_index < len(num):
        if num[right_index].isnumeric():
            right_val = right_val + num[right_index]
        elif right_val != '':
            break
        right_index += 1

    if right_val:
        num = num[:right_index-len(right_val)] + str(int(right_val) + pair[1]) + num[right_index:]

    while left_index >= 0:
        if num[left_index].isnumeric():
            left_val = num[left_index] + left_val
        elif left_val != '':
            break
        left_index -= 1

    if left_val:
        num = num[:left_index+1] + str(int(left_val) + pair[0]) + num[left_index+len(left_val)+1:]

    return num


def snailfish_split(num: str, index: int, val: str) -> str:
    left_val = int(floor(float(val) / 2.0))
    right_val = int(ceil(float(val) / 2.0))
    new_pair = "[" + str(left_val) + "," + str(right_val) + "]"
    num = num[:index] + new_pair + num[index+len(val):]

    return num


def score_nums(num: list) -> int:
    num_score = 0
    while isinstance(num, list):
        num = magnitude(num)
    return num


def magnitude(num: list) -> int:
    for index, value in enumerate(num):
        if isinstance(value, list):
            num[index] = magnitude(num[index])
        elif len(num) > 1 and not isinstance(num[0], list) and not isinstance(num[1], list):
            num = num[0] * 3 + num[1] * 2
            return num
    return num


def largest_magnitude(num: list) -> tuple[list, int]:
    mag = []
    for x, y in permutations(num, 2):
        nums = eval(add_snailfish_numbers([x, y]))
        mag.append(score_nums(nums))

    return max(mag)




snailfish_hw_numbers = parse_input(PUZZLE_INPUT_FILE)
# added_snailfish_numbers = add_snailfish_numbers((snailfish_hw_numbers))
print(largest_magnitude(snailfish_hw_numbers))