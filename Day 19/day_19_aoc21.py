from itertools import combinations

SAMPLE_INPUT_FILE = "sample_input_day_19_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_19_aoc21.txt"
MIN_SHARED_BEACONS = 12

def parse_input(dir_file: str) -> list:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:

    """

    with open(dir_file, "r") as file:
        data = []
        for row in file.readlines():
            if "scanner" in row:
                data.append([])
            elif len(row) > 1:
                data[-1].append(eval("[" + row + "]"))
        return data


def all_transformations(coords: list) -> list:
    coords_transformed = [[] for i in range(24)]

    for coord in coords:
        x = coord[0]
        y = coord[1]
        z = coord[2]

        coord_transformed = [[-z, y, x], [-y, -z, x], [z, -y, x], [y, z, x],
                             [z, y, -x], [-y, z, -x], [-z, -y, -x], [y, -z, -x],
                             [z, x, y], [-x, z, y], [-z, -x, y], [x, -z, y],
                             [z, -x, -y], [x, z, -y], [-z, x, -y], [-x, -z, -y],
                             [x, y, z], [-y, x, z], [-x, -y, z], [y, -x, z],
                             [y, x, -z], [-x, y, -z], [-y, -x, -z], [x, -y, -z]]

        for index, transformation in enumerate(coord_transformed):
            coords_transformed[index].append(transformation)

    return coords_transformed


def align_scans(coord_abs: list, coord_zero: list, coord_list: list) -> list:
    for index, coord in enumerate(coord_list):
        coord_list[index] = [coord[0] - coord_zero[0] + coord_abs[0],
                             coord[1] - coord_zero[1] + coord_abs[1],
                             coord[2] - coord_zero[2] + coord_abs[2]]
    return coord_list


def count_shared_beacons(ref_coords: list, check_coords: list) -> int:
    return len([coord for coord in check_coords if coord in ref_coords])


def resolve_beacons(scan_data: list) -> tuple[list, list]:
    absolute_coords = scan_data.pop(0)
    absolute_scanners = [[0, 0, 0]]

    while scan_data:
        print(len(scan_data))
        flag = False
        for index_scanner, scanner in enumerate(scan_data):
            transformed_scanner = all_transformations(scanner)
            for index_transformed, transformed in enumerate(transformed_scanner):
                for index_absolute, absolute in enumerate(absolute_coords):
                    for index_relative, relative in enumerate(transformed):
                        aligned_scans = align_scans(absolute, relative, transformed)
                        if count_shared_beacons(absolute_coords, aligned_scans) >= MIN_SHARED_BEACONS:
                            print(absolute, relative)
                            print(aligned_scans)
                            print(absolute_coords)
                            quit()
                            absolute_coords.extend(aligned_scans)

                            absolute_scanners.append(
                                [absolute[0] - relative[0],
                                 absolute[1] - relative[1],
                                 absolute[2] - relative[2]])
                            scan_data.pop(index_scanner)
                            flag = True
                            break
                    if flag:
                        break
                if flag:
                    break
            if flag:
                break

    return list(map(list, set(map(tuple, absolute_coords)))), absolute_scanners


def manhattan(coord_0: list, coord_1: list) -> int:
    return abs(coord_0[0] - coord_1[0]) + abs(coord_0[1] - coord_1[1]) + abs(coord_0[2] - coord_1[2])


relative_beacon_scans = parse_input(SAMPLE_INPUT_FILE)
absolute_beacon_scans, absolute_scanner_locations = resolve_beacons(relative_beacon_scans)
print(len(absolute_beacon_scans))
print(absolute_scanner_locations)

max_dist = 0
for x, y in combinations(absolute_scanner_locations, 2):
    dist = manhattan(x, y)
    if dist > max_dist:
        max_dist = dist

print(max_dist)