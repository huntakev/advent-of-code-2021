FILE = "day_2_aoc21.txt"
SAMPLE_INPUT = ['forward 5', 'down 5', 'forward 8',
                'up 3', 'down 8', 'forward 2']


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


def convert_simple_sub_commands_to_position(arr: list) -> tuple[int, int, int]:
    """
    Args:
        arr: list of strings including a simple command and magnitude separated by one space
    Returns:
        depth, horizontal, and depth * horizontal positions after parsing all simple sub commands
    """
    d = 0
    h = 0
    for elem in arr:
        command, magnitude = elem.split(' ', 1)
        if command == 'forward':
            h += int(magnitude)
        elif command == 'up':
            d -= int(magnitude)
        elif command == 'down':
            d += int(magnitude)

    return d, h, d * h


def convert_complex_sub_commands_to_position(arr: list) -> tuple[int, int, int]:
    """
    Args:
        arr: list of strings including a complex command and magnitude separated by one space
    Returns:
        depth, horizontal, and depth * horizontal positions after parsing all complex sub commands
    """
    d = 0
    h = 0
    a = 0
    for elem in arr:
        command, magnitude = elem.split(' ', 1)
        if command == 'up':
            a -= int(magnitude)
        elif command == 'down':
            a += int(magnitude)
        elif command == 'forward':
            h += int(magnitude)
            d += a * int(magnitude)
    return d, h, d * h


puzzle_input = unpack_puzzle_input(FILE)
print(convert_simple_sub_commands_to_position(puzzle_input))
print(convert_complex_sub_commands_to_position(puzzle_input))
