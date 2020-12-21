
aller_in_ingredients = []
allergens = set()
ingredients = set()
with open('inputs/day21') as f:
    for line in f:
        parts = line.rstrip().split('(')
        allers = parts[1][9:-1].split(', ')
        ings = parts[0].rstrip().split(' ')

        aller_in_ingredients.append((ings, allers))
        allergens.update(allers)
        ingredients.update(ings)


ing_per_allergen = {aller: ingredients for aller in allergens}
for ings, allers in aller_in_ingredients:
    for aller in allers:
        ing_per_allergen[aller] = ing_per_allergen[aller].intersection(ings)

can_have_allergens = set().union(*list(ing_per_allergen.values()))
no_allergens = ingredients.difference(can_have_allergens)

count = 0
for ings, _ in aller_in_ingredients:
    for ingredient in ings:
        if ingredient in no_allergens:
            count += 1

print(f'a) {count}')

matched = dict()
while len(ing_per_allergen) > 0:
    assigned_allergen = None
    for ingredient, allergens in ing_per_allergen.items():
        if len(allergens) == 1:
            assigned_allergen = list(allergens)[0]
            matched[ingredient] = assigned_allergen
            break

    assert assigned_allergen is not None
    ingredients_to_delete = []
    for ingredient, allergens in ing_per_allergen.items():
        if assigned_allergen in allergens:
            allergens.remove(assigned_allergen)
            if len(allergens) == 0:
                ingredients_to_delete.append(ingredient)

    for ingredient in ingredients_to_delete:
        del ing_per_allergen[ingredient]


keys = sorted(matched.keys())
result = ''
for key in keys:
    result += ',' + matched[key]
result = result[1:]

print(f'b) {result}')
