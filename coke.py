def get_coin():
    while True:
        coin = int(input("Insert coin:  "))
        if coin == 25 or coin == 10 or coin == 5:
            return coin
        else:
            print("Invalid coin.")

total = 0
while total < 50:
    total += get_coin()
    print("Amount due: {}".format(50 - total))

change = total - 50
print("Change owed: {}".format(change))
