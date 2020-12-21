def find_foods_with_allergen(food_count_dict):
    must_have_allergen = set()

    for allergy in food_count_dict:
        maxi = 0
        for food, count_val in food_count_dict[allergy].items():
            maxi = max(count_val, maxi)

        for food, count_val in food_count_dict[allergy].items():
            if count_val == maxi:
                must_have_allergen.add(food)

    return must_have_allergen

def find_allergy_choices(allergy_set, food_count_dict, ingred_with_allergen):
    allergy_info = {}
    for allergy in allergy_set:
        maxi = 0
        acc_lst = []
        for ingredient in food_count_dict[allergy]:
            if ingredient in ingred_with_allergen:
                maxi = max(maxi, food_count_dict[allergy][ingredient])
        
        for ingredient in food_count_dict[allergy]:
            if ingredient in ingred_with_allergen:
                if food_count_dict[allergy][ingredient] == maxi:
                    acc_lst.append(ingredient)

        allergy_info[allergy] = acc_lst

    return allergy_info

def find_allergen_ingredient(allergy_info_dict):
    found_food = set()

    while len(found_food) != len(allergy_info_dict):
        for key in allergy_info_dict:
            if len(allergy_info_dict[key]) == 1:
                found_food.add(allergy_info_dict[key][0])

        for key in allergy_info_dict:
            if len(allergy_info_dict[key]) == 1:
                continue
            for found in found_food:
                if found in allergy_info_dict[key]:
                    allergy_info_dict[key].remove(found)

file = open('day21input.txt', 'r')

food_count = {}
allergy_set = set()

for line in file:
    line = line.strip('\n')
    lst = line.split('(')
    ingredients = lst[0].strip(' ').split(' ')

    allergies = lst[1].strip(')').replace('contains ', '').split(', ')
    for allergy in allergies:
        if allergy not in food_count:
            food_count[allergy] = {}
        for ingr in ingredients:
            if ingr in food_count[allergy]:
                food_count[allergy][ingr] += 1
            else:
                food_count[allergy][ingr] = 1
        allergy_set.add(allergy)

file.close()

must_have_allergen = find_foods_with_allergen(food_count)

allergy_info = find_allergy_choices(allergy_set, food_count, must_have_allergen)

find_allergen_ingredient(allergy_info)

alpha_keys = sorted(list(allergy_info.keys()))
allergy_lst = []
for key in alpha_keys:
    allergy_lst.append(allergy_info[key][0])

print(','.join(allergy_lst))