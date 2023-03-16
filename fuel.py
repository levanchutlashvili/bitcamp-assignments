
while True:
    try:
        fraction = input("Fraction: ")
        x, y = map(int, fraction.split('/'))
        if x <= 0 or y <= 0 or x > y:
            raise ValueError:
        break
    except (ValueError, ZeroDivisionError):
        print(" Please enter two positive integers separated by a slash (/).")

percentage = round(x / y * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
