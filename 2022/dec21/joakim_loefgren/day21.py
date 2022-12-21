OP_INVS = { 
    '*': '/',
    '/': '*',
    '+': '-',
    '-': '+',
}

def parse_input(filename):
    with open(filename) as f:
       monkeys_num = {}
       monkeys_op = {}
       for line in f:
           lsplit = line.split(':')
           left = lsplit[0]
           right = lsplit[1].strip().split()
           if len(right) == 1:
               monkeys_num[left] = right[0]
           else:
               monkeys_op[left] = right
    return monkeys_num, monkeys_op


def reduce_yells(monkeys_num, monkeys_op):
    old = 0
    new = 1
    while old != new:
        old = len(monkeys_op)
        # substitute
        for key in monkeys_op:
            op = monkeys_op[key]
            op_new = [monkeys_num.get(op[0], op[0]), op[1], monkeys_num.get(op[2], op[2])]
            monkeys_op[key] = op_new

        # evaluate
        for key in list(monkeys_op.keys()):
            op = ''.join(monkeys_op[key])
            try:
                val = eval(op)
                monkeys_num[key] = str(val)
                monkeys_op.pop(key)
            except NameError:
                pass
        new = len(monkeys_op)
        

def solve_equation(left, right):
    op = right[1]
    op_inv = OP_INVS[op] 
    if right[0].isalpha():
        var = right[0]
        val = eval(f'{left}{op_inv}{right[2]}')
    else:
        if right[1] in ['/', '-']:
            var = right[2]
            val = eval(f'{right[0]}{op}{left}')
        else:
            var = right[2]
            val = eval(f'{left}{op_inv}{right[0]}')
    return var, val
    

if __name__ == '__main__':
    # part I
    # monkeys_num, monkeys_op = parse_input('./test.txt')
    # reduce_yells(monkeys_num, monkeys_op)
    # print(int(float(monkeys_num['root'])))

    # part 2
    monkeys_num, monkeys_op = parse_input('./input.txt')
    monkeys_num.pop('humn')

    # reduce as far as possible
    reduce_yells(monkeys_num, monkeys_op)

    # solve equation for root
    left, _, right = monkeys_op['root']
    if not left.isalpha():
        left, right = right, left
        
    monkeys_num[left] = right
    # reduce as far as possible again
    reduce_yells(monkeys_num, monkeys_op)

    # solve equations
    solve_next = left
    while len(monkeys_op) > 0:
        for key in list(monkeys_op.keys()):
            if key == solve_next:
                right = monkeys_op[key]
                var, val = solve_equation(monkeys_num[solve_next], right)
                monkeys_num.update({var: val})
                monkeys_op.pop(key)
                solve_next = var
                break
            
    print(int(float(monkeys_num['humn'])))
