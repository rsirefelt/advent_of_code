if __name__ == "__main__":
    with open("input") as f:
        lines = [line.rstrip() for line in f.readlines()]

    all_allergens = {}
    all_ingredients = []
    for line in lines:
        ingredients, allergens = line[:-1].split("(contains ")
        allergens = allergens.split(", ")
        ingredients = ingredients.split()

        all_ingredients.append(ingredients)
        # Remove duplicates
        ingredients = list(set(ingredients))
        for allergen in allergens:
            if allergen not in all_allergens:
                all_allergens[allergen] = ingredients
            else:
                # Only keep matches
                all_allergens[allergen] = [
                    a for a in all_allergens[allergen] if a in ingredients
                ]

    possible_allergens = set(
        val for allergen in all_allergens.values() for val in allergen
    )

    count = 0
    for ingredients in all_ingredients:
        count += sum([1 for ingr in ingredients if ingr not in possible_allergens])

    print(f"Result task 1: {count}")

    matches = [None] * len(all_allergens)
    all_allergens = sorted(all_allergens.items())
    while None in matches:
        for i, (_, ingredients) in enumerate(all_allergens):
            if len(ingredients) == 1:
                # Add match
                matches[i] = ingredients[0]
                # Remove the column_idx from matches to check.
                all_allergens = [
                    (key, [val for val in values if val != ingredients[0]])
                    for key, values in all_allergens
                ]
                break

    res2 = ",".join(matches)
    print(f"Result task 2: {res2}")
