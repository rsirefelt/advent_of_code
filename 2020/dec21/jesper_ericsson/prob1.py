import numpy as np
import re

regex_dish = re.compile(r'([\w ]*) \(contains ([\w, ]*)\)')

def read_allergens(filename):
    with open(filename, 'r') as f:
        data_lines = f.readlines()
        allergens_dict = {}
        allergens_dict_all = {}
        dishes = []
        for string in data_lines:
            ingredients, allergens = regex_dish.findall(string.rstrip())[0]
            ingredients = ingredients.split(' ')

            allergens = allergens.split(', ')
            dishes.append(ingredients)
            for allergen in allergens:
                if allergen in allergens_dict:
                    allergens_dict[allergen].append(ingredients)
                    allergens_dict_all[allergen].update(ingredients)
                else:
                    allergens_dict[allergen] = [ingredients]
                    allergens_dict_all[allergen] = set(ingredients)


    return allergens_dict, allergens_dict_all, dishes


def main():
    allergens, allergens_all, dishes= read_allergens('testdata.csv')
    allergens, allergens_all, dishes = read_allergens('data.csv')

    ingredient_allergen_all_remove = []
    while True:
        ingredient_allergen_remove = []
        for allergen in allergens:
            in_all_dishes = []
            for ingredient in allergens_all[allergen]:
                if all(ingredient in sublist for sublist in allergens[allergen]):
                    in_all_dishes.append(ingredient)
            if len(in_all_dishes) == 1:
                ingredient_allergen_remove.append((in_all_dishes[0], allergen))
                ingredient_allergen_all_remove.append((in_all_dishes[0], allergen))

        if ingredient_allergen_remove:
            for allergen in allergens:
                for ingredient_remove, _ in ingredient_allergen_remove:
                    if ingredient_remove in allergens_all[allergen]:
                        for dish in allergens[allergen]:
                            try:
                                dish.remove(ingredient_remove)
                            except:
                                continue

                    allergens_all[allergen].discard(ingredient_remove)
        else:
            break

    super_set = set()
    for key in allergens_all:
        super_set.update(allergens_all[key])

    ingredients_appearance = 0
    for ingredient in super_set:
        in_dishes = np.array([ingredient in sublist for sublist in dishes])
        ingredients_appearance += in_dishes.sum()
    
    print('Number of times igredients appear: %i' %ingredients_appearance)


    sorted_list = sorted(ingredient_allergen_all_remove, key=lambda x: x[1])
    # print(sorted_list)

    out_string = ''
    for ing, _ in sorted_list:
        out_string += ing + ','

    print('Dangerous ingredients: ' + out_string)



if __name__ == "__main__": main()