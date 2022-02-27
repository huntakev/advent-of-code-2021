SAMPLE_INPUT_FILE = "sample_input_day_20_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_20_aoc21.txt"
NUM_ENHANCEMENTS = 3


def parse_input(dir_file: str) -> tuple[str, list]:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:

    """
    alg, im = '', []
    with open(dir_file, "r") as file:
        lines = file.read().splitlines()
        alg = lines[0]
        im = lines[2:]

    return alg, im


def convert_algorithm_to_bool(input_algorithm: str) -> str:
    output_algorithm = ""
    for character in input_algorithm:
        if character == "#":
            output_algorithm += "1"
        elif character == ".":
            output_algorithm += "0"

    return output_algorithm


def convert_image_to_bool(input_image: list) -> list:
    output_image = [[None] * len(input_image) for i in range(len(input_image[0]))]
    for index_row, row in enumerate(image):
        for index_col, col in enumerate(row):
            if col == "#":
                output_image[index_row][index_col] = 1
            elif col == ".":
                output_image[index_row][index_col] = 0

    return output_image


def binary_to_int(binary_value: str) -> int:
    return int(binary_value, 2)


def new_pixel_value(pixel_value: int, enhance_algorithm: str) -> int:
    return int(enhance_algorithm[pixel_value])


def surrounding_pixels_binary_value(arr: list, x: int, y: int) -> str:
    pixel_binary_value = ''
    indices = [(x-1, y-1), (x-1, y), (x-1, y+1),
               (x, y-1), (x, y), (x, y+1),
               (x+1, y-1), (x+1, y), (x+1, y+1)]

    for (x_i, y_i) in indices:
        if 0 <= x_i < len(arr) and 0 <= y_i < len(arr[x]):
            pixel_binary_value += str(arr[x_i][y_i])
        else:
            pixel_binary_value += "0"

    return pixel_binary_value


def create_canvas(input_image: list, num_enhance: int) -> list:
    canvas = [[0] * (len(input_image) + 2 * num_enhance) for i in range((len(input_image[0]) + 2 * num_enhance))]

    for index_row, row in enumerate(canvas):
        for index_col, col in enumerate(canvas):
            if num_enhance <= index_row < len(canvas) - num_enhance and num_enhance <= index_col < len(canvas[0]) - num_enhance:
                canvas[index_row][index_col] = input_image[index_row - num_enhance][index_col - num_enhance]

    return canvas


def enhance_image(enhance_algorithm: str, input_image: list) -> list:
    output_image = [[0] * len(input_image) for i in range(len(input_image[0]))]

    for index_row, row in enumerate(input_image):
        for index_col, col in enumerate(row):
            output_image[index_row][index_col] = new_pixel_value(binary_to_int((surrounding_pixels_binary_value(input_image, index_row, index_col))), enhance_algorithm)

    return output_image


def count_light_pixels(input_image: list) -> int:
    return sum(sum(input_image, []))


algorithm, image = parse_input(PUZZLE_INPUT_FILE)
algorithm = convert_algorithm_to_bool(algorithm)
image = convert_image_to_bool(image)
image = create_canvas(image, NUM_ENHANCEMENTS)


for i in image:
    print(i)
print()


for i in range(NUM_ENHANCEMENTS):
    image = enhance_image(algorithm, image)

    for j in image:
        print(j)
    print()
    print(count_light_pixels(image))
    print()