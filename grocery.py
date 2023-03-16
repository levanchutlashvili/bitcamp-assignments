Grocery_List = {}
while True:
    try:
       item = input("").title()
       if item not in Grocery_List:
           Grocery_List[item] = 1
       else:
           Grocery_List[item] += 1   
    except (EOFError, KeyError):
        break

Sorted_List = sorted(Grocery_List.items(), key=lambda x: x[0])
for item, count in Sorted_List:
    print(f"{count} {item.upper()}")    