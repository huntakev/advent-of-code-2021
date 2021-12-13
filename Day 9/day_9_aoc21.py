SAMPLE_INPUT_FILE = "sample_input_day_9_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_9_aoc21.txt"


def input_file_to_heightmap(dir_file: str) -> list:
    """
    Args:
        dir_file (str): location of .txt file to pull data from

    Returns:
        list of lists in which each [row][col] value is the height at that position in the heightmap
    """

    with open(dir_file, "r") as file:
        content = file.read().splitlines()
        hm = []
        for index in range(len(content)):
            hm.append([])
            for num in content[index]:
                hm[index].append(int(num))
        return hm


def sum_risk_level_of_low_points(hm: list) -> int:
    count = 0
    for row in range(len(hm)):
        for col in range(len(hm[row])):
            if check_for_lower_adj_height(hm, row, col):
                count += hm[row][col] + 1
    return count


def check_for_lower_adj_height(arr, index_row, index_col) -> bool:
    """
    Args:
        arr: heightmap array
        index_row: row index of location to check adjacent locations for lower or equally low height
        index_col: column index of location to check adjacent locations for lower or equally low height
    Returns:
        True if check location is lower than all adjacent locations, else False
    """

    if index_row >= 1:
        if arr[index_row][index_col] >= arr[index_row-1][index_col]:
            return False

    if index_row < len(arr) - 1:
        if arr[index_row][index_col] >= arr[index_row+1][index_col]:
            return False

    if index_col >= 1:
        if arr[index_row][index_col] >= arr[index_row][index_col-1]:
            return False

    if index_col < len(arr[index_row]) - 1:
        if arr[index_row][index_col] >= arr[index_row][index_col+1]:
            return False

    return True


def find_low_points(hm: list) -> list:
    lp = []
    for row in range(len(hm)):
        for col in range(len(hm[row])):
            if check_for_lower_adj_height(hm, row, col):
                lp.append([row, col])
    return lp


def group_basins(hm: list) -> list:
    basins = [[[0, 0]]] if hm[0][0] != 9 else [[]]

    for row in range(len(hm)):
        for col in range(len(hm[row])):

            if hm[row][col] == 9:
                continue

            for basin in basins:
                try:
                    if [row, col] not in basin and [row - 1, col - 1] in basin and \
                            not(9 == hm[row-1][col] == hm[row][col-1]):
                        basin.append([row, col])
                        continue
                except Exception:
                    pass

                try:
                    if [row, col] not in basin and [row - 1, col] in basin:
                        basin.append([row, col])
                        continue
                except Exception:
                    pass

                try:
                    if [row, col] not in basin and [row - 1, col + 1] in basin and \
                            not(9 == hm[row-1][col] == hm[row][col+1]):
                        basin.append([row, col])
                        continue
                except Exception:
                    pass

                try:
                    if [row, col] not in basin and [row, col - 1] in basin:
                        basin.append([row, col])
                        continue
                except Exception:
                    pass

                try:
                    if [row, col] not in basin and [row, col + 1] in basin:
                        basin.append([row, col])
                        continue
                except Exception:
                    pass

                try:
                    if [row, col] not in basin and [row + 1, col - 1] in basin and \
                            not(9 == hm[row+1][col] == hm[row][col-1]):
                        basin.append([row, col])
                        continue
                except Exception:
                    pass

                try:
                    if [row, col] not in basin and [row + 1, col] in basin:
                        basin.append([row, col])
                        continue
                except Exception:
                    pass

                try:
                    if [row, col] not in basin and [row + 1, col + 1] in basin and \
                            not(9 == hm[row+1][col] == hm[row][col+1]):
                        basin.append([row, col])
                        continue
                except Exception:
                    pass

            if [row, col] not in [indices for basin in basins for indices in basin]:
                basins.append([[row, col]])
                continue

    return basins


def multiply_sizes_of_largest_basins(b: list) -> int:
    b_sorted = sorted(b, key=len, reverse=True)
    return len(b_sorted[0]) * len(b_sorted[1]) * len(b_sorted[2])


puzzle_input = input_file_to_heightmap(SAMPLE_INPUT_FILE)
basins = group_basins(puzzle_input)
score = multiply_sizes_of_largest_basins(basins)
print(score)