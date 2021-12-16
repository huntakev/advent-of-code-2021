import itertools

SAMPLE_INPUT_FILE = "sample_input_day_13_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_13_aoc21.txt"


def parse_input(dir_file: str) -> tuple[list, list]:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:

    """

    with open(dir_file, "r") as file:
        content = list(filter(None, (line.strip() for line in file)))
        dots = [list([int(i.split(",")[0]), int(i.split(",")[1])]) for i in content if i[0].isnumeric()]
        folds = [i.split()[2] for i in content if not i[0].isnumeric()]
        return dots, folds


def translate_and_reflect(coords: list, line_dir: str, line_dist: int) -> list:
    transformed_coords = []
    for coord in coords:
        if line_dir == 'y':
            if line_dist >= coord[1]:
                transformed_coords.append([coord[0], coord[1]])
            else:
                transformed_coords.append([coord[0], -(coord[1] - line_dist) + line_dist])

        elif line_dir == 'x':
            if line_dist >= coord[0]:
                transformed_coords.append([coord[0], coord[1]])
            else:
                transformed_coords.append([-(coord[0] - line_dist) + line_dist, coord[1]])

    return transformed_coords


def fold_paper(dots: list, folds: list) -> list:
    """
    Args:
        dots:
        folds:

    Returns:

    """
    for fold in folds:
        dots = translate_and_reflect(dots, fold[0], int(fold[2:]))
    dots.sort()
    return list(dots for dots,_ in itertools.groupby(dots))


def print_paper(dots: list) -> None:
    largest_x, largest_y = max([i[0] for i in dots]), max([i[1] for i in dots])
    grid = [[' ']*(largest_x + 1) for i in range((largest_y + 1))]

    for dot in dots:
        grid[dot[1]][dot[0]] = '#'

    for row in grid:
        print(row)


d, f = parse_input(PUZZLE_INPUT_FILE)
print(d, f)
puzzle_output = fold_paper(d, f)
print(puzzle_output)
print_paper(puzzle_output)