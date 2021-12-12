SAMPLE_INPUT_FILE = "sample_input_day_6_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_6_aoc21.txt"
NUM_DAYS = 256


def input_file_list_of_lanternfish(dir_file: str) -> list:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:
        list of input lanternfish spawn timer
    """

    with open(dir_file, "r") as file:
        return [int(i) for i in file.read().split(",")]


def forecast_num_lanternfish(input_lanternfish: list, num_days: int) -> int:
    """
    Args:
        input_lanternfish (list): list of input lanternfish spawn timer
        num_days (int): the number of days to forecast the number of lanternfish after spawning
    Returns:
        the number of lanternfish forecasted after the specified input days
    """

    output_lanternfish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in input_lanternfish:
        output_lanternfish[fish] += 1
    for day in range(num_days):
        nf = output_lanternfish[0]
        for fish in range(len(output_lanternfish)-1):
            output_lanternfish[fish] = output_lanternfish[fish + 1] if fish != 6 else output_lanternfish[fish + 1] + nf
        output_lanternfish[8] = nf

    return sum(output_lanternfish)


puzzle_input = input_file_list_of_lanternfish(PUZZLE_INPUT_FILE)
puzzle_output = forecast_num_lanternfish(puzzle_input, NUM_DAYS)
print(puzzle_output)
