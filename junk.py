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
        
def get_shop_list_by_dishes(dishes, person_count):
    
    ings_shop_list = {}
    for dish in dishes:
        if dish in cook_book:
           for ing_dish in cook_book[dish]:
               ings = int(ing_dish['quantity'])
               ings *= person_count
               ing_dish['quantity'] = ings
               
               ings_shop_list.setdefault(ing_dish['ingredient_name'], ing_dish )
               
               pprint.pprint(ings_shop_list)

   

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

         
           
    
                 