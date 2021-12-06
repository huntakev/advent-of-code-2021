SAMPLE_INPUT_FILE = "sample_input_day_5_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_5_aoc21.txt"


def input_file_to_line_points(dir_file: str) -> list:
    """
    Args:
        dir_file (str): location of .txt file to pull data from

    Returns:
        end points values in [[x1, y1], [x2, y2]] format for lines defined in input file
    """

    with open(dir_file, "r") as file:
        content = file.read().splitlines()
        l_points = []
        for row in content:
            l_points.append([[int(i) for i in row.split()[0].split(",")],
                             [int(i) for i in row.split()[2].split(",")]])
        return l_points


def line_ends_to_line_points(l_ends: list, diags: bool = False) -> list:
    """
    Args:
        l_ends: list of end points defined in [[x1, y1], [x2, y2]] format
        diags: boolean option to evaluate diagonal lines (True) or ignore (False)

    Returns:
        list of all points in [x1, y1] format that the lines cross defined by input end points
    """
    l_points = []
    for coord in l_ends:

        # y1 == y2 and x1 != x2 for horizontal lines
        if coord[0][1] == coord[1][1] and coord[0][0] != coord[1][0]:
            for x_val in range(min(coord[0][0], coord[1][0]),
                               max(coord[0][0], coord[1][0]) + 1):
                l_points.append([x_val, coord[0][1]])

        # x1 == x2 and y1 != y2 for vertical lines
        elif coord[0][0] == coord[1][0] and coord[0][1] != coord[1][1]:
            for y_val in range(min(coord[0][1], coord[1][1]),
                               max(coord[0][1], coord[1][1]) + 1):
                l_points.append([coord[0][0], y_val])

        # if evaluating diagonals, assume all remaining points represent diagonals
        elif diags:
            x_dir = 1 if coord[0][0] < coord[1][0] else -1
            y_dir = 1 if coord[0][1] < coord[1][1] else -1
            for count in range(abs(coord[0][0] - coord[1][0]) + 1):
                l_points.append([coord[0][0] + count * x_dir,
                                 coord[0][1] + count * y_dir])

        # if ignoring diagonals, return empty array
        else:
            return []

    return l_points


def line_points_to_grid(l_points: list) -> list:
    """
    Args:
        l_points: all points occupied by lines in [x1, y1] format

    Returns:
        grid where [x, y] value contains the number of lines that occupy that coordinate
    """

    # determine size of grid
    largest_x = max([i[0] for i in l_points])
    largest_y = max([i[1] for i in l_points])

    # instantiate empty grid
    grid = [[0]*(largest_x + 1) for i in range((largest_y + 1))]

    # iterate through all points and add counts to grid coordinates
    for point in l_points:
        grid[point[1]][point[0]] += 1

    return grid


def count_line_intersections(grid: list) -> int:
    """
    Args:
        grid: list where [x, y] value contains the number of lines that occupy that coordinate

    Returns:
        count of coordinates with count >=2 (where 2 or more lines intersect)
    """
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] > 1:
                count += 1

    return count


line_ends = input_file_to_line_points(PUZZLE_INPUT_FILE)
line_points = line_ends_to_line_points(line_ends, True)
point_grid = line_points_to_grid(line_points)
num_intersections = count_line_intersections(point_grid)

print(num_intersections)

