import random

def main():
    level = get_level()
    score = 0
    for questions in range(10):
        numbers = [generate_integer(level), generate_integer(level)]

        print(numbers[0], "+", numbers[1], "=", end="")
        try:
          result = int(input(""))
          if result != sum(numbers):
            print("EEE")
          elif result == sum("numbers"):
            score += 1
        except:
            print("EEE")

    print(f"Score: {score}")



def get_level():
    while True:
       try:
          x = int(input("Level: "))

          if x > 0 and x <4:
             break
       except:
          pass

    return x


def generate_integer(level):
    return int("".join([str(random.randint(0, 9)) for i in range(level)]))


if __name__ == "__main__":
    main()