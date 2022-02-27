SAMPLE_INPUT_FILE = "sample_input_day_12_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_12_aoc21.txt"


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
            output.append(row.split("-"))
        return output


def distinct_paths(connections: list) -> int:
    count = 0
    paths = [['start']]
    while True:
        num_paths = len(paths)
        next_paths = []
        for path in paths:
            if path[-1] == 'end':
                next_paths.append(path)
                continue
            for step in possible_moves(path[-1], connections):
                if (step.islower() and step not in ['start', 'end'] and step in path) or step == 'start':
                    continue
                full_path = path + [step]
                if full_path not in next_paths:
                    next_paths.append(full_path)
        paths = next_paths[:]
        if len(paths) == num_paths:
            break
    for path in reversed(paths):
        if path[-1] != 'end':
            paths.remove(path)

    return len(paths)


def distinct_paths_one_small_cave(connections: list) -> int:
    count = 0
    paths = [['', 'start']]
    while True:
        num_paths = len(paths)
        next_paths = []
        for path in paths:
            if path[-1] == 'end':
                next_paths.append(path)
                continue
            for step in possible_moves(path[-1], connections):
                if step == 'start' or step in path[0] or (step.islower() and step in path and path[0] != ''):
                    continue
                full_path = path + [step]
                if step.islower() and full_path[0] == '' and step in path:
                    full_path[0] = step
                if full_path[1:] not in [i[1:] for i in next_paths]:
                    next_paths.append(full_path)
        paths = next_paths[:]
        if len(paths) == num_paths:
            break
    for path in reversed(paths):
        if path[-1] != 'end':
            paths.remove(path)
    return len(paths)


def possible_moves(pos: str, conns: list) -> list:
    moves = []
    for conn in conns:
        if conn[0] == pos:
            moves.append(conn[1])
        elif conn[1] == pos:
            moves.append(conn[0])

    return moves


puzzle_input = parse_input(PUZZLE_INPUT_FILE)
puzzle_output = distinct_paths_one_small_cave(puzzle_input)
print(puzzle_output)

