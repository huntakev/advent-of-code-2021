SAMPLE_INPUT_FILE = "sample_input_day_11_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_11_aoc21.txt"
FLASH_THRESHOLD = 9
STEPS = 100


def parse_input(dir_file: str) -> list:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:
        list of lists containing the signals in the 0th index and output in the 1st index
    """

    with open(dir_file, "r") as file:
        content = file.read().splitlines()
        output = []
        for row in content:
            output.append([int(i) for i in row])
        return output


def surrounding_indices(arr: list, x: int, y: int) -> list:
    indices = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
    return [(x_i, y_i) for (x_i, y_i) in indices if 0 <= x_i < len(arr) and 0 <= y_i < len(arr[x])]


def count_flashes_by_step(arr: list, steps: int) -> int:
    step_count = 0
    flash_count = 0
    while step_count < steps:
        step_count += 1

        for row in range(len(arr)):
            for col in range(len(arr[row])):
                arr[row][col] += 1

        fully_energized = False
        while not fully_energized:
            fully_energized = True
            for row in range(len(arr)):
                for col in range(len(arr[row])):
                    if arr[row][col] > FLASH_THRESHOLD:
                        arr[row][col] = 0
                        flash_count += 1
                        for (x_ind, y_ind) in surrounding_indices(arr, row, col):
                            if arr[x_ind][y_ind] > 0:
                                arr[x_ind][y_ind] += 1
                                fully_energized = False
    return flash_count


def steps_to_synchronize(arr: list) -> int:
    num_max_flashes = len(arr) * len(arr[0])
    flash_count = 0
    step_count = 0

    while flash_count < num_max_flashes:
        flash_count = 0
        step_count += 1

        for row in range(len(arr)):
            for col in range(len(arr[row])):
                arr[row][col] += 1

        fully_energized = False
        while not fully_energized:
            fully_energized = True
            for row in range(len(arr)):
                for col in range(len(arr[row])):
                    if arr[row][col] > FLASH_THRESHOLD:
                        arr[row][col] = 0
                        flash_count += 1
                        for (x_ind, y_ind) in surrounding_indices(arr, row, col):
                            if arr[x_ind][y_ind] > 0:
                                arr[x_ind][y_ind] += 1
                                fully_energized = False
    return step_count


puzzle_input = parse_input(PUZZLE_INPUT_FILE)
puzzle_output = steps_to_synchronize(puzzle_input)
print(puzzle_output)

