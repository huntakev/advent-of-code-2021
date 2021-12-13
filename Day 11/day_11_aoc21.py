SAMPLE_INPUT_FILE = "sample_input_day_8_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_8_aoc21.txt"


def input_file_to_signals_and_outputs(dir_file: str) -> list:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:
        list of lists containing the signals in the 0th index and output in the 1st index
    """

    with open(dir_file, "r") as file:
        content = file.read().splitlines()
        for i in range(len(content)):
            content[i] = content[i].split("|")
        return content