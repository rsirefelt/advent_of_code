""" Advent of Code day 21 """


def parse_input(input_file):
    with open(input_file, "r") as fp:
        lines = fp.read().splitlines()
    foods = []
    foods_allergens = []
    for line in lines:
        lsplit = line.split(" (contains ")
        foods.append(set(lsplit[0].split()))
        foods_allergens.append(set(lsplit[1][:-1].split(", ")))

    return foods, foods_allergens


if __name__ == "__main__":
    foods, foods_allergens = parse_input("./input_day21.txt")
    nfoods = len(foods)
    ingredients = set.union(*foods)
    allergens = sorted(list(set.union(*foods_allergens)))

    # find inert ingredients
    inert = ingredients
    matches = {}
    for aller in allergens:
        possible_ingredients = set.intersection(
            *[foods[i] for i in range(nfoods) if aller in foods_allergens[i]]
        )
        matches[aller] = possible_ingredients
        inert -= possible_ingredients

    # Part I
    count = 0
    for ingr in inert:
        count += sum([1 for f in foods if ingr in f])
    print(count)

    # Part II
    # remove inert ingredients
    visited = set()
    for aller in matches:
        ingrs = matches[aller] - inert
        matches[aller] = ingrs
        if len(ingrs) == 1:
            visited.add(*ingrs)

    # find 1-to-1 matches
    while len(visited) != len(allergens):
        for aller, ingrs in matches.items():
            if len(ingrs) > 1:
                ingrs -= visited
                matches[aller] = ingrs
            elif len(ingrs) == 1:
                visited.add(*ingrs)

    canonical_list = ",".join([v.pop() for v in matches.values()])
    print(canonical_list)
