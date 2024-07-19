import pprint

    
def get_shop_list_by_dishes(dishes, person_count):      
    ings_shop_list = {}
    for dish in dishes:
        if dish in cook_book:     
            for ing_dish in cook_book[dish]:
            
                prod = ing_dish['ingredient_name']
                ings_shop_list.setdefault(prod, [])
                ings = int(ing_dish['quantity']) * person_count
                v = {'quantity': ings, 'measure': ing_dish['measure']}        
                ings_shop_list[prod] = v
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')                
    
    pprint.pprint(ings_shop_list)
    return ings_shop_list


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
    pprint.pprint(cook_book)


   

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)

         
           
    
                 

