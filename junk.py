import pprint

with open ('receip.txt', encoding = 'utf-8') as file:
    cook_book = {}
    rec_list = []
    dish = file.readline().strip()
    ing_numb = file.readline()
    n = int(ing_numb)
    ing_list = file.readlines()[0:n]
    
    for line in file:
        while True:
            if line != " ":
                for rec in ing_list:
                    rec= list(rec.split(' | '))
                    receip = {'ingredient_name': rec[0], 'quantity': rec[1], 'measure': rec[2].strip()}
                if receip not in rec_list:
                    rec_list.append(receip)
                cook_book[dish] = rec_list        
                
            else:
                break
                
pprint.pprint(cook_book)

            