# Day 21: Allergen Assessment

from copy import deepcopy

INPUT_FILE_NAME = "./inputs/day21input.txt"
TEST_FILE_NAME = "./inputs/day21testinput.txt"

def determine_ingredient(allergen_details):
    '''
    Returns the ingredient mapped to an allergen given the ingredient
    appearance counts. If an ingredient has the maximum count, it should be
    associated to the allergen unless there is another ingredient with the
    same count. If there are ingredients that have the same maximum count,
    return None.
    '''
    max_ingr_count = max(allergen_details.values())
    ingredient = None
    for ingr, count in allergen_details.items():
        if count != max_ingr_count:
            continue
        if not ingredient:
            ingredient = ingr
        else:
            return None
    return ingredient


def remove_ingredient_option(allergen_map, ingredient):
    '''
    After an ingredient has been mapped to an allergen, it needs
    to be removed as a possible mapping from the other allergen mappings.

    Sets the value of ingredient appearance count for an allergen mapping to -1.
    '''
    for allergen in allergen_map:
        if ingredient in allergen_map[allergen]:
            allergen_map[allergen][ingredient] = -1

def map_allergens_to_ingredients(allergen_map):
    '''
    Determines the ingredient associated to each allergen. 
    Returns a dictionary mapping each allergen to one ingredient.
    '''
    allergen_ingredient_map = {}

    while len(allergen_ingredient_map) != len(allergen_map):
        for allergen in allergen_map:
            if allergen in allergen_ingredient_map: 
                continue
            ingredient = determine_ingredient(allergen_map[allergen])
            if not ingredient:
                continue

            allergen_ingredient_map[allergen] = ingredient
            remove_ingredient_option(allergen_map, ingredient)
                
    return allergen_ingredient_map

def read_foods(file_nm):
    '''
    Reads through a file of foods (one per line) where each line has
    a list of ingredients and the allergens the food contains. Each allergen is 
    mapped to only one ingredient, but not all allergens are listed (maybe forgot
    to label or labelled in a different langauge).

    Returns a dictionary of how many times an ingredient appeared in all the foods
    and a dictionary mapping an allergen to the possible foods it could be 
    associated with.
    '''
    file = open(file_nm, 'r')

    allergen_map = {}
    ingredients_counts = {}

    for line in file:
        ingredients, allergens = line.strip('\n').split('(')
        ingredients_lst = ingredients.strip(' ').split(' ')

        for ingredient in ingredients_lst: 
            if ingredient in ingredients_counts:
                ingredients_counts[ingredient] += 1
            else:
                ingredients_counts[ingredient] = 1

        allergens_lst = allergens.strip(')').replace('contains ', '').split(', ')
        for allergen in allergens_lst:
            if allergen not in allergen_map:
                allergen_map[allergen] = {}
            for ingredient in ingredients_lst:
                if ingredient in allergen_map[allergen]:
                    allergen_map[allergen][ingredient] += 1
                else:
                    allergen_map[allergen][ingredient] = 1

    file.close()

    return allergen_map, ingredients_counts

def solve_part_one(allergen_map, ingredients_counts):
    '''
    Returns the amount of times the ingredients that cannot contain
    an allergen appear
    '''
    allergen_ingredient_map = map_allergens_to_ingredients(allergen_map)

    total_counts_ingredients_not_allergens = 0
    ingredients_with_allergen = allergen_ingredient_map.values()
    for ingredient in ingredients_counts:
        if ingredient not in ingredients_with_allergen:
            total_counts_ingredients_not_allergens += ingredients_counts[ingredient]
    return total_counts_ingredients_not_allergens

def solve_part_two(allergen_map):
    '''
    Returns a string representation of the list of ingredients that contain an 
    allergen in the order of alphabetized allergens.
    '''
    allergen_ingredient_map = map_allergens_to_ingredients(allergen_map)

    alphabetized_allergens = sorted(list(allergen_ingredient_map.keys()))
    return ','.join([allergen_ingredient_map[allergen] for allergen in alphabetized_allergens])

def main():
    test_allergen_map, test_ingredients_counts = read_foods(TEST_FILE_NAME)
    test_allergen_map_copy = deepcopy(test_allergen_map)
    assert(solve_part_one(test_allergen_map, test_ingredients_counts) == 5)
    assert(solve_part_two(test_allergen_map_copy) == 'mxmxvkd,sqjhc,fvjkl')
    
    allergen_map, ingredients_counts = read_foods(INPUT_FILE_NAME)
    allergen_map_copy = deepcopy(allergen_map)
    print('Part One:', solve_part_one(allergen_map, ingredients_counts))
    print('Part Two:', solve_part_two(allergen_map_copy))

main()
