emojize = {
    ":1st_place_medal:" : "🥇",
    ":money_bag:" : "💰",
    ":smile_cat:" : "😸"
}

emoji = input("Input: ").split(" ")

for text in emoji:
    if text in emojize:
        print(emojize[text], end=" ")
    else:
        print(text, end=" ")

print("")            