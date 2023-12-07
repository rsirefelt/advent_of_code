available = {'red': 12, 'green': 13, 'blue': 14}

possible_ids = []
powers = []
with open('inputs/day2') as f:
    for line in f:
        data = line.rstrip()

        min_needed = {'red': 0, 'green': 0, 'blue': 0}

        game_id = int(data.split(':')[0].split(' ')[1])
        reveals = data.split(':')[1][1:].split(';')

        game_ok = True
        for reveal in reveals:
            for color_num in reveal.split(','):
                color = color_num.strip().split(' ')[1]
                num = int(color_num.strip().split(' ')[0])
                if num > available[color]:
                    game_ok = False
                if num > min_needed[color]:
                    min_needed[color] = num

        powers.append(min_needed['red']*min_needed['green']*min_needed['blue'])
        if game_ok:
            possible_ids.append(game_id)

    print(sum(possible_ids))
    print(sum(powers))
