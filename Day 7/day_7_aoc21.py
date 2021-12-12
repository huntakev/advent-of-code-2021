SAMPLE_INPUT_FILE = "sample_input_day_7_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_7_aoc21.txt"
NUM_DAYS = 256


def input_file_to_crab_pos_sorted(dir_file: str) -> list:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:
        list of starting position of the crab submarines, sorted in ascending order
    """

    with open(dir_file, "r") as file:
        return sorted([int(i) for i in file.read().split(",")])


def median(arr: list) -> int:
    """
    Args:
        arr: array of numbers
    Returns:
        median value of input array
    """

    n = len(arr)
    s = sorted(arr)
    return int((sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2]) if n else None


def calc_total_crab_fuel_simple(input_positions: list) -> int:
    """
    Use median value of the array to determine the minimum fuel consumption for the simple consumption method

    Args:
        input_positions: list of input crab submarine positions
    Returns:
        total fuel required for all crabs to move to the lowest total fuel position using simple calculation
    """

    pos = median(input_positions)
    fuel = 0
    for crab in input_positions:
        fuel += abs(pos - crab)

    return fuel


def calc_total_crab_fuel_complex(input_positions: list) -> int:
    """
    Determine the fuel required for each crab to move to each position and return the fuel for the minimum consumption
    position

    Args:
        input_positions: list of input crab submarine positions
    Returns:
        total fuel required for all crabs to move to the lowest total fuel position using advanced calculation
    """

    possible_positions = [0] * max(input_positions)
    for pos in range(len(possible_positions)):
        for crab in input_positions:
            dist = abs(crab - pos)
            possible_positions[pos] += int(dist * (dist + 1) / 2)

    return min(possible_positions)


puzzle_input = input_file_to_crab_pos_sorted(PUZZLE_INPUT_FILE)
puzzle_output = calc_total_crab_fuel_complex(puzzle_input)
print(puzzle_output)


