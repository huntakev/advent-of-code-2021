SAMPLE_INPUT_FILE = "sample_input_day_8_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_8_aoc21.txt"


def input_file_to_signals_and_outputs(dir_file: str) -> list:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:
        list of lists containing the signals in the 0th index and output in the 1st index
    """

    with open(dir_file, "r") as file:
        content = file.read().splitlines()
        for i in range(len(content)):
            content[i] = content[i].split("|")
        return content


def count_ones_fours_sevens_eights(signals_and_outputs: list) -> int:
    """
    Use length of output string to determine how many ones (2 segments), fours (4 segments), sevens (3 segments), and
    eights (seven segments) there are

    Args:
        signals_and_outputs (list): input signals and outputs of seven segment displays
    Returns:
        the count of output digits that are 1, 4, 7, or 8
    """
    count = 0
    for pattern in signals_and_outputs:
        output = pattern[1].split(" ")
        for segments in output:
            if len(segments) in [2, 3, 4, 7]:
                count += 1
    return count


def decode_outputs_from_signals(signals_and_outputs) -> int:
    """
    Use signals to decode seven segment wiring and calculate puzzle output

    Args:
        signals_and_outputs (list): input signals and outputs of seven segment displays
    Returns:
        sum of all decoded output numbers
    """

    numbers = ['', '', '', '', '', '', '', '', 'abcdefg', '']
    count = 0
    for pattern in signals_and_outputs:
        output_row = ''

        # 1s, 4s, 7s, and 8s can be determined by length of strings
        for signal in pattern[0].split(" "):
            if len(signal) == 2:
                numbers[1] = signal
            elif len(signal) == 3:
                numbers[7] = signal
            elif len(signal) == 4:
                numbers[4] = signal

        # 0s, 2s, 3s, 5s, 6s, and 9s can be determined by comparing known values
        for signal in pattern[0].split(" "):
            if len(signal) == 5:
                if sum(i in signal for i in numbers[4]) == 2:
                    numbers[2] = signal
                elif sum(i in signal for i in numbers[7]) == 3:
                    numbers[3] = signal
                else:
                    numbers[5] = signal

            if len(signal) == 6:
                if sum(i in signal for i in numbers[1]) == 2 and sum(i in signal for i in numbers[4]) == 3:
                    numbers[0] = signal
                elif sum(i in signal for i in numbers[1]) == 1:
                    numbers[6] = signal
                else:
                    numbers[9] = signal

        # decode and count up outputs
        for output in pattern[1].split(" "):
            for num in range(len(numbers)):
                if all(i in output for i in numbers[num]) and len(output) == len(numbers[num]):
                    output_row = output_row + str(num)
        count += int(output_row)

    return count


puzzle_input = input_file_to_signals_and_outputs(PUZZLE_INPUT_FILE)
print(decode_outputs_from_signals(puzzle_input))
