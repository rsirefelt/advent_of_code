import re


def mask_val(val, mask):
    masked_val = 0
    vstr = '{:b}'.format(val).zfill(len(mask))
    for i in range(len(mask)):
        if mask[-i-1] == 'X':
            masked_val += int(vstr[-i-1]) * 2**i
        else:
            masked_val += int(mask[-i-1]) * 2**i
    return masked_val


def mask_adress(adr, mask):
    masked_adr = ''
    adr = '{:b}'.format(adr).zfill(len(mask))
    for i in range(len(mask)):
        if mask[i] == '0':
            masked_adr += adr[i]
        else:
            masked_adr += mask[i]
    return masked_adr


def add_value_to_mem(mem, key, v, m):
    mem[key] = mask_val(v, m)


def add_values_to_mem_b(mem, v, adr_left, adr_right):

    if adr_right.count('X') == 0:  # decode and add to dict
        mem[int(adr_left + adr_right, 2)] = v
    else:
        for i in range(len(adr_right)):
            if adr_right[i] == 'X':
                add_values_to_mem_b(mem, v, adr_left + '1', adr_right[i+1:])
                add_values_to_mem_b(mem, v, adr_left + '0', adr_right[i+1:])
                break
            adr_left += adr_right[i]


mask = None
mem_dict = dict()
mem_dict_b = dict()
mem_exp = re.compile(r"mem\[(\d+)\] = (\d+)")
with open('inputs/day14') as f:
    for line in f:
        if line.startswith('mask'):
            mask = line.split('=')[-1].strip()
        else:
            mem_match = mem_exp.match(line)
            if mem_match is not None:
                ind = int(mem_match.groups()[0])
                val = int(mem_match.groups()[1])

                add_value_to_mem(mem_dict, ind, val, mask)
                masked_adress = mask_adress(ind, mask)
                add_values_to_mem_b(mem_dict_b, val, '', masked_adress)

print(f'a) {sum(mem_dict.values())}')
print(f'b) {sum(mem_dict_b.values())}')
