camel_case = input("camelcase: ")
snake_case = ""

for character in camel_case:
    if character.isupper():
        snake_case += "_" + character.lower()

print(f"snake_case: {snake_case}")