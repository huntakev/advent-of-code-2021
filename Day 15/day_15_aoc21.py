"""
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""

SAMPLE_INPUT_FILE = "sample_input_day_15_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_15_aoc21.txt"
D_WEIGHT = 1.0


def parse_input(dir_file: str) -> list:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:

    """

    with open(dir_file, "r") as file:
        content = list(filter(None, (line.strip() for line in file)))
        return [list(int(i) for i in row) for row in content]


def dijkstras_algorithm(i_node_row: int, i_node_col: int, f_node_row: int, f_node_col: int, nodes: list) -> int:
    unvisited = [[float("inf")] * len(nodes) for i in range(len(nodes[0]))]
    unvisited[0][0] = 0
    visited = []
    current_row = i_node_row
    current_col = i_node_col

    while True:
        for row, col in surrounding_indices(nodes, current_row, current_col):
            if [row, col] not in visited:
                dist = unvisited[current_row][current_col] + nodes[row][col]
                if dist < unvisited[row][col]:
                    unvisited[row][col] = dist
        visited.append([current_row, current_col])

        if [f_node_row, f_node_col] in visited:
            found = True
            return int(unvisited[f_node_row][f_node_col])

        min_dist = float("inf")
        min_row = None
        min_col = None
        for row in range(len(unvisited)):
            for col in range(len(unvisited[0])):
                if [row, col] not in visited:
                    if unvisited[row][col] < min_dist:
                        min_dist = unvisited[row][col]
                        min_row = row
                        min_col = col
            current_row = min_row
            current_col = min_col


def a_star(i_node_row: int, i_node_col: int, f_node_row: int, f_node_col: int, nodes: list) -> int:
    open = [[i_node_row, i_node_col]]
    closed = []
    parent = {str([i_node_row, i_node_col]): [i_node_row, i_node_col]}
    g = [[float("inf")] * len(nodes) for i in range(len(nodes[0]))]

    # Instead of calculating h in loops, make look-up table
    h = [[0] * len(nodes) for i in range(len(nodes[0]))]
    for i in range(len(nodes)):
        for j in range(len(nodes[0])):
            h[i][j] = manhattan(i, j, f_node_row, f_node_col, D_WEIGHT)
    g[i_node_row][i_node_col] = 0

    while len(open) > 0:
        node_current = open[0]
        for node_open in open:
            if f(g, h, node_open[0], node_open[1]) < f(g, h, node_current[0], node_current[1]):
                node_current = node_open
        open.remove(node_current)
        closed.append(node_current)
        if node_current == [f_node_row, f_node_col]:
            return g[f_node_row][f_node_col]

        for row, col in surrounding_indices(nodes, node_current[0], node_current[1]):
            if [row, col] in closed:
                continue

            if [row, col] in open:
                if g[node_current[0]][node_current[1]] + nodes[row][col] < g[row][col]:
                    g[row][col] = g[node_current[0]][node_current[1]] + nodes[row][col]
                    parent[str([row, col])] = node_current
            else:
                open.append([row, col])
                g[row][col] = g[node_current[0]][node_current[1]] + nodes[row][col]
                parent[str([row, col])] = node_current


def f(g, h, row, col):
    return g[row][col] + h[row][col]


def expand_cave(input_cavern_map: list) -> list:
    output_cavern_map = []
    for row_counter in range(5):
        output_cavern_map.extend([list(i+row_counter for i in j) for j in input_cavern_map])

    for row_index in range(len(output_cavern_map)):
        row_vals = output_cavern_map[row_index][:]
        for col_counter in range(1, 5):
            output_cavern_map[row_index].extend([i+col_counter for i in row_vals])

    for row_index in range(len(output_cavern_map)):
        for col_index in range(len(output_cavern_map[0])):
            while output_cavern_map[row_index][col_index] > 9:
                output_cavern_map[row_index][col_index] -= 9

    return output_cavern_map


def min_cost_coords(coords: list, cost: list):
    lr = cost[coords[0][0]][coords[0][1]]
    mc_coords = coords[0]
    for coord in coords:
        if cost[coord[0]][coord[1]] < lr:
            lr = cost[coord[0]][coord[1]]
            mc_coords = coord
    return mc_coords


def manhattan(x: int, y: int, x_f: int, y_f: int, D: float) -> float:
    return D * (abs(x - x_f) + abs(y - y_f))


def surrounding_indices(arr: list, x: int, y: int) -> list:
    indices = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
    return [(x_i, y_i) for (x_i, y_i) in indices if 0 <= x_i < len(arr) and 0 <= y_i < len(arr[x])]


cavern_map = parse_input(PUZZLE_INPUT_FILE)
# print(len(cavern_map), len(cavern_map[0]))
# print(dijkstras_algorithm(0, 0, len(cavern_map)-1, len(cavern_map[0])-1, cavern_map))
# print(a_star(0, 0, len(cavern_map)-1, len(cavern_map[0])-1, cavern_map))
expanded_cavern_map = expand_cave(cavern_map)
print(a_star(0, 0, len(expanded_cavern_map)-1, len(expanded_cavern_map[0])-1, expanded_cavern_map))