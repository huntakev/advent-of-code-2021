FILE = "day_3_aoc21.txt"
SAMPLE_INPUT = ['00100', '11110', '10110', '10111', '10101', '01111',
                '00111', '11100', '10000', '11001', '00010', '01010']


def unpack_puzzle_input(dir_file: str) -> list:
    """
    Args:
        dir_file (str): location of .txt file to pull data from

    Returns:
        list of string commands saved in .txt file
    """

    with open(dir_file, "r") as file:
        content = file.read()
        data = content.split("\n")
    return data


def measure_power_from_gamma_and_epsilon(arr: list) -> tuple[int, int, int]:
    """
    Args:
        arr: list of string formatted binary values

    Returns:
        gamma, epsilon, and power consumption values
    """
    count = [0] * len(arr[0])
    gamma = [0] * len(arr[0])
    epsilon = [0] * len(arr[0])
    for elem in arr:
        for index in range(len(elem)):
            count[index] += int(elem[index])

    for index in range(len(count)):
        gamma[index] = int(count[index] >= len(arr) - count[index])
        epsilon[index] = int(count[index] < len(arr) - count[index])

    gamma = int("".join([str(i) for i in gamma]), 2)
    epsilon = int("".join([str(i) for i in epsilon]), 2)
    power = gamma * epsilon

    return gamma, epsilon, power


def measure_life_support_from_o2_and_co2(arr: list) -> tuple[int, int, int]:
    """
    Args:
        arr: list of string formatted binary values

    Returns:
        o2, co2, and life support values
    """
    o2_arr = arr[:]
    co2_arr = arr[:]

    for pos in range(len(arr[0])):
        o2_count = [0] * len(arr[0])
        co2_count = [0] * len(arr[0])
        o2 = [0] * len(arr[0])
        co2 = [0] * len(arr[0])

        for elem in o2_arr:
            o2_count[pos] += int(elem[pos])

        for elem in co2_arr:
            co2_count[pos] += int(elem[pos])

        o2[pos] = int(o2_count[pos] >= len(o2_arr) - o2_count[pos])
        co2[pos] = int(co2_count[pos] < len(co2_arr) - co2_count[pos])

        for elem in reversed(o2_arr):
            if len(o2_arr) == 1:
                break
            if elem[pos] != o2[pos]:
                o2_arr.remove(elem)

        for elem in reversed(co2_arr):
            if len(co2_arr) == 1:
                break
            if elem[pos] != co2[pos]:
                co2_arr.remove(elem)

    o2 = int("".join([str(i) for i in o2_arr[0]]), 2)
    co2 = int("".join([str(i) for i in co2_arr[0]]), 2)
    life_support = o2 * co2

    return o2, co2, life_support


puzzle_input = unpack_puzzle_input(FILE)
print(measure_power_from_gamma_and_epsilon(puzzle_input))
print(measure_life_support_from_o2_and_co2(puzzle_input))
