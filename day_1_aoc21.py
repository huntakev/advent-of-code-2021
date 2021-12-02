FILE = "C:/Users/hunta/Desktop/data.txt.txt"
x = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def txt_to_list(dir_file: str):
    '''
    Args:
        dir_file (str): Location of file to pull data from
    Returns:
        list of numeric values saved in .txt file
    '''
    with open(dir_file, "r") as file:
        content = file.read()
        data = content.split("\n")
    return list(map(int, data))

def count_sequential_elem_increases(arr: list):
    '''
    Args:
        arr (list): List of numeric values
    Returns:
        count of the number of times that a value increases from the previous array entry
    '''
    return sum(arr[i-1] < arr[i] for i in range(1, len(arr)))

def count_sequential_window_increases(arr: list):
    '''
    Args:
        arr (list): List of numeric values
    Returns:
        count of number of times that the sum of a rolling 3 element window is larger than
        the previous adjacent 3 element window
    '''
    return sum(sum(arr[i-4:i-1]) < sum(arr[i-3:i])
               for i in range(3, len(arr)))

data = txt_to_list(FILE)
print(count_sequential_elem_increases(data)
print(count_sequential_window_increases(data)
