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

file = open('day21input.txt', 'r')

food_count = {}

word_counts = {}

for line in file:
    line = line.strip('\n')
    lst = line.split('(')
    ingredients = lst[0].strip(' ').split(' ')

    # used later for counting how many times the non-allergen foods appear
    for ingr in ingredients: 
        if ingr in word_counts:
            word_counts[ingr] += 1
        else:
            word_counts[ingr] = 1

    allergies = lst[1].strip(')').replace('contains ', '').split(', ')
    for allergy in allergies:
        if allergy not in food_count:
            food_count[allergy] = {}
        for ingr in ingredients:
            if ingr in food_count[allergy]:
                food_count[allergy][ingr] += 1
            else:
                food_count[allergy][ingr] = 1

file.close()

must_have_allergen = find_foods_with_allergen(food_count)

total_counts = 0
for word in word_counts:
    if word not in must_have_allergen:
        total_counts += word_counts[word]

print(total_counts)