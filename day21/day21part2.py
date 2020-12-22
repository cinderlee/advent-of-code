def find_foods_with_allergen(allergen_info_dict):
    must_have_allergen = set()

    for allergy in allergen_info_dict:
        maxi = 0
        for food, count_val in allergen_info_dict[allergy].items():
            maxi = max(count_val, maxi)

        filter_lst = []
        for food, count_val in allergen_info_dict[allergy].items():
            if count_val == maxi:
                must_have_allergen.add(food)
                filter_lst.append(food)
    
        allergen_info_dict[allergy] = filter_lst

    return must_have_allergen

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

allergen_info = {}
allergy_set = set()

for line in file:
    line = line.strip('\n')
    lst = line.split('(')
    ingredients = lst[0].strip(' ').split(' ')

    allergies = lst[1].strip(')').replace('contains ', '').split(', ')
    for allergy in allergies:
        if allergy not in allergen_info:
            allergen_info[allergy] = {}
        for ingr in ingredients:
            if ingr in allergen_info[allergy]:
                allergen_info[allergy][ingr] += 1
            else:
                allergen_info[allergy][ingr] = 1
        allergy_set.add(allergy)

file.close()

must_have_allergen = find_foods_with_allergen(allergen_info)

find_allergen_ingredient(allergen_info)

alpha_keys = sorted(list(allergen_info.keys()))
allergy_lst = []
for key in alpha_keys:
    allergy_lst.append(allergen_info[key][0])

print(','.join(allergy_lst))