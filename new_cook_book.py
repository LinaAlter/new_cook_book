import pprint

with open ('receip.txt', encoding = 'utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ing_numb = int(file.readline())
        ing_dish = []
        for r in range(ing_numb):
            numb = file.readline().strip()
            ingredient_name, quantity, measure = numb.split(' | ')
            ing_dish.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish] = ing_dish
        file.readline()

