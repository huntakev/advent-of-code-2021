SAMPLE_INPUT_FILE = "sample_input_day_16_aoc21.txt"
PUZZLE_INPUT_FILE = "puzzle_input_day_16_aoc21.txt"
LEN_SHORTEST_TRANSMISSION = 11
ID_LITERAL = 4


def parse_input(dir_file: str) -> str:
    """
    Args:
        dir_file (str): location of .txt file to pull data from
    Returns:

    """

    with open(dir_file, "r") as file:
        return hex_to_bin(file.read())

'''
tree = [{'id': 0,
         'parent_tree': [],
         'version': 0,
         'type_ID': 0,
         'value': 0},
        {'id': 1,
         'parent_tree': [0],
         'version': 0,
         'type_ID': 0,
         'value': 0}]
'''


def decode_transmission(transmission: str):
    packet_tree = []
    flag = False

    while not flag:
        transmission, packet_tree, flag = read_packet(transmission, packet_tree)

    #packet_tree = unflatten_packets(packet_tree)

    return packet_tree


def unflatten_packets(packets: list) -> list:
    parent_tree = []
    for packet in packets:
        packet['parent_tree'] = parent_tree[:]
        # Deal with counting current packet toward its parent
        if parent_tree:
            for parent in packets:
                remove_flag = False
                if parent['id'] == parent_tree[-1]:
                    if parent['parent_type'] == 1:
                        parent['child_counter'] += 1
                        if parent['child_counter'] == parent['value']:
                            remove_flag = True

                if parent['id'] in parent_tree:
                    if parent['parent_type'] == 0:
                        parent['child_counter'] += packet['num_bits']
                        if parent['child_counter'] >= parent['value']:
                            remove_flag = True

                if remove_flag:
                    parent_tree.remove(parent['id'])

                if not parent_tree:
                    break


                '''
                if parent['id'] == parent_tree[-1]:
                    if parent['parent_type'] == 0:
                        parent['child_counter'] += packet['num_bits']
                        if parent['value'] == parent['child_counter']:
                            parent_tree = parent_tree[:-1]
                            break
                    elif parent['parent_type'] == 1:
                        parent['child_counter'] += 1
                        if parent['value'] == parent['child_counter']:
                            parent_tree = parent_tree[:-1]
                            break
                '''

        # Deal with heirarchy of current packet
        if packet['parent_type'] != -1:
            parent_tree.append(packet['id'])

    return packets


def evaluate_expressions(packets: list) -> int:
    parent_id = max(i['id'] for i in packets)
    next_packets = packets[:]
    while len(packets) > 2:
        # print(len(packets))
        if parent_id < 0:
            parent_id = max(i['id'] for i in packets)
        child_packets = []
        for packet in packets:
            if packet['parent_tree']:
                # print(parent_id, packet['parent_tree'][-1], packet['parent_type'])
                if packet['parent_tree'][-1] == parent_id and packet['parent_type'] == -1:
                    child_packets.append(packet)
                    next_packets.remove(packet)
        if child_packets:
            parent_id = max(i['id'] for i in next_packets)
            for parent_packet in next_packets:
                if parent_packet['id'] == child_packets[0]['parent_tree'][-1]:
                    '''
                    # print(parent_packet['id'])
                    print(parent_packet)
                    for i in child_packets:
                        print(i)
                    print()
                    '''
                    if parent_packet['type_ID'] == 0:
                        parent_packet['parent_type'] = -1
                        parent_packet['value'] = sum(i['value'] for i in child_packets)
                    elif parent_packet['type_ID'] == 1:
                        parent_packet['parent_type'] = -1
                        parent_packet['value'] = 1
                        for child in child_packets:
                            parent_packet['value'] *= child['value']
                    elif parent_packet['type_ID'] == 2:
                        parent_packet['parent_type'] = -1
                        parent_packet['value'] = min(i['value'] for i in child_packets)
                    elif parent_packet['type_ID'] == 3:
                        parent_packet['parent_type'] = -1
                        parent_packet['value'] = max(i['value'] for i in child_packets)
                    elif parent_packet['type_ID'] == 5:
                        parent_packet['parent_type'] = -1
                        parent_packet['value'] = int(child_packets[0]['value'] > child_packets[1]['value'])
                    elif parent_packet['type_ID'] == 6:
                        parent_packet['parent_type'] = -1
                        parent_packet['value'] = int(child_packets[0]['value'] < child_packets[1]['value'])
                    elif parent_packet['type_ID'] == 7:
                        parent_packet['parent_type'] = -1
                        parent_packet['value'] = int(child_packets[0]['value'] == child_packets[1]['value'])
        else:
            parent_id -= 1
        packets = next_packets[:]
    print()
    return packets[0]['value']

def sum_version_nums(packets: list) -> int:
    total = 0
    for packet in packets:
        total += packet['version']
    return total


def read_packet(trans: str, packets: list) -> tuple[str, list, bool]:
    packets.append({'id': 0 if not packets else packets[-1]['id'] + 1,
                     'version': -1,
                     'type_ID': -1,
                     'parent_type': -1,
                     'value': -1,
                     'num_bits': 6,
                     'child_counter': 0,
                     'parent_tree': []})

    while True:
        # Get packet version
        packets[-1]['version'] = int(trans[:3], 2)
        trans = trans[3:]

        # Get packet type ID
        packets[-1]['type_ID'] = int(trans[:3], 2)
        trans = trans[3:]

        # If literal, record value
        if packets[-1]['type_ID'] == ID_LITERAL:
            literal_complete = False
            literal_bin = ''
            while not literal_complete:
                literal_bin += trans[1:5]
                packets[-1]['num_bits'] += 5
                if trans[0] == '0':
                    literal_complete = True
                trans = trans[5:]
            packets[-1]['value'] = int(literal_bin, 2)
            return trans, packets, len(trans) < LEN_SHORTEST_TRANSMISSION

        else:
            packets[-1]['parent_type'] = int(trans[0])
            trans = trans[1:]
            if packets[-1]['parent_type']:
                packets[-1]['value'] = int(trans[:11], 2)
                packets[-1]['num_bits'] += 12
                trans = trans[11:]
                return trans, packets, len(trans) < LEN_SHORTEST_TRANSMISSION

            else:
                packets[-1]['value'] = int(trans[:15], 2)
                packets[-1]['num_bits'] += 16
                trans = trans[15:]
                return trans, packets, len(trans) < LEN_SHORTEST_TRANSMISSION


def hex_to_bin(hex_str: str) -> str:
    bin_str = ''
    for c in hex_str:
        if c == '0':
            bin_str += '0000'
        elif c == '1':
            bin_str += '0001'
        elif c == '1':
            bin_str += '0001'
        elif c == '2':
            bin_str += '0010'
        elif c == '3':
            bin_str += '0011'
        elif c == '4':
            bin_str += '0100'
        elif c == '5':
            bin_str += '0101'
        elif c == '6':
            bin_str += '0110'
        elif c == '7':
            bin_str += '0111'
        elif c == '8':
            bin_str += '1000'
        elif c == '9':
            bin_str += '1001'
        elif c == 'A':
            bin_str += '1010'
        elif c == 'B':
            bin_str += '1011'
        elif c == 'C':
            bin_str += '1100'
        elif c == 'D':
            bin_str += '1101'
        elif c == 'E':
            bin_str += '1110'
        elif c == 'F':
            bin_str += '1111'
    return bin_str


bin_input = parse_input(PUZZLE_INPUT_FILE)
#print(bin_input)
decoded_transmission = decode_transmission(bin_input)
structured_packets = unflatten_packets(decoded_transmission)
for i in structured_packets:
  # print(i)
  #if i['parent_type'] != -1 and i['value'] != i['child_counter']:
  #    print(i)
print(evaluate_expressions(structured_packets))

#for i in decoded_transmission:
#    print(i)
