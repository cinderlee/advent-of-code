FILE_TEST_NM = 'day21testinput.txt'
FILE_NM = 'day21input.txt'

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

    Returns a dictionary mapping an allergen to the possible foods it could be 
    associated with.
    '''
    file = open(file_nm, 'r')

    allergen_map = {}

    for line in file:
        ingredients, allergens = line.strip('\n').split('(')
        ingredients_lst = ingredients.strip(' ').split(' ')

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

    return allergen_map

def solve(file_nm):
    '''
    Returns a string representation of the list of ingredients that contain an 
    allergen in the order of alphabetized allergens.
    '''
    allergen_map = read_foods(file_nm)
    allergen_ingredient_map = map_allergens_to_ingredients(allergen_map)

    alphabetized_allergens = sorted(list(allergen_ingredient_map.keys()))
    return ','.join([allergen_ingredient_map[allergen] for allergen in alphabetized_allergens])

def main():
    assert(solve(FILE_TEST_NM) == 'mxmxvkd,sqjhc,fvjkl')
    print(solve(FILE_NM))


main()
