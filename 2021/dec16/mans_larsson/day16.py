import numpy as np


def decode(message, starting_pos, max_pos, max_packets):
    pos = starting_pos

    decoded_info = []
    current_message_info = {}
    mode = 0
    while pos < len(message):
        if int('0b' + message[pos:], 2) == 0:
            break

        if mode == 0:  # packet version
            current_message_info['version'] = int(message[pos:pos+3], 2)
            mode = 1
            pos += 3
        elif mode == 1:  # packet type
            current_message_info['type'] = int(message[pos:pos+3], 2)
            pos += 3
            if current_message_info['type'] == 4:
                current_message_info['number_str'] = ''
                mode = 2
            else:
                pos += 1
                if message[pos-1] == '0':
                    total_length = int(message[pos:pos+15], 2)
                    pos += 15
                    inner_max_pos = pos + total_length
                    inner_max_packets = None

                else:
                    inner_max_packets = int(message[pos:pos+11], 2)
                    pos += 11
                    inner_max_pos = None

                info, pos = decode(message, pos, max_pos=inner_max_pos, max_packets=inner_max_packets)
                current_message_info['submessages'] = info
                decoded_info.append(current_message_info)
                current_message_info = {}
                mode = 0
        elif mode == 2:
            current_message_info['number_str'] = current_message_info['number_str'] + message[pos+1:pos+5]
            if message[pos] == '0':  # this was last message
                mode = 0
                if starting_pos == 0:
                    len_so_far = 5 * len(current_message_info['number_str']) // 4 + 6
                    pos += len_so_far % 4  # padding for hex

                decoded_info.append(current_message_info)
                current_message_info = {}
            pos += 5

        if max_pos is not None and pos >= max_pos:
            break
        if max_packets is not None and len(decoded_info) >= max_packets:
            break

    return decoded_info, pos


def version_sum(transmission_info):
    this_sum = 0
    for message in transmission_info:
        this_sum += message['version']
        if 'submessages' in message:
            this_sum += version_sum(message['submessages'])
    return this_sum


def calculate(transmission_info):
    numbers = []
    for message in transmission_info:
        if 'submessages' in message:
            inner_numbers = calculate(message['submessages'])
            if message['type'] == 0:
                numbers.append(sum(inner_numbers))
            elif message['type'] == 1:
                numbers.append(np.prod(inner_numbers))
            elif message['type'] == 2:
                numbers.append(min(inner_numbers))
            elif message['type'] == 3:
                numbers.append(max(inner_numbers))
            elif message['type'] == 5:
                numbers.append(int(inner_numbers[0] > inner_numbers[1]))
            elif message['type'] == 6:
                numbers.append(int(inner_numbers[0] < inner_numbers[1]))
            elif message['type'] == 7:
                numbers.append(int(inner_numbers[0] == inner_numbers[1]))
        else:
            numbers.append(int('0b' + message['number_str'], 2))
    return numbers


with open('inputs/day16') as f:
    transmission = f.readlines()[0].rstrip()

binary_transmission = ''.join([f"{int(bin(int('0x' + c, 16))[2:]):04d}" for c in transmission])
info, last_pos = decode(binary_transmission, 0, None, None)

print(version_sum(info))
print(calculate(info))
