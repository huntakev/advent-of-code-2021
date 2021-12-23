SAMPLE_INPUT_FILE = "sample_input_day_17_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_17_aoc21.txt"


def parse_input(dir_file: str) -> tuple[list, list]:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:

    """

    with open(dir_file, "r") as file:
        text = file.read()
        x = ''
        y = ''
        x_flag = False
        y_flag = False
        for index in range(1, len(text)):
            if text[index-2:index] == 'x=':
                x_flag = True
            elif text[index] == ',':
                x_flag = False
            elif text[index-2:index] == 'y=':
                y_flag = True

            if x_flag:
                x += text[index]

            elif y_flag:
                y += text[index]

        return [int(i) for i in x.split("..")], [int(j) for j in y.split("..")]


def max_peak(y_target: list) -> int:
    """
    Only works if min(y_target)<0
    Args:
        y_target:

    Returns:

    """
    vel = abs(min(y_target))-1
    height = 0
    while vel >= 0:
        height += vel
        vel -= 1
    return height


def calculate_initial_velocities(x_t: list, y_t: list) -> list:
    x_vel_max = max(x_t)
    y_vel_max = abs(min(y_target))-1
    y_vel_min = min(y_t)
    vels = []

    for x_i in range(x_vel_max + 1):
        for y_i in range(y_vel_min, y_vel_max + 1):
            x_pos = 0
            y_pos = 0
            x_vel = x_i
            y_vel = y_i

            while x_pos <= max(x_t) and y_pos >= min(y_t):
                x_pos += x_vel
                y_pos += y_vel

                if min(x_t) <= x_pos <= max(x_t) and min(y_t) <= y_pos <= max(y_t):
                    vels.append([x_i, y_i])
                    break

                if x_vel > 0:
                    x_vel -= 1
                elif x_vel < 0:
                    x_vel += 1
                y_vel -= 1

    return vels


x_target, y_target = parse_input(PUZZLE_INPUT_FILE)
print(x_target, y_target)
print(max_peak(y_target))
velocities = calculate_initial_velocities(x_target, y_target)
print(len(velocities))