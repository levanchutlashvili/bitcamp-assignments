import random

while True:
    try:
        n = input("Level: ")

        if n > 0:
           break
    except:
        pass    

number = random.randint(1, n)

while True:
    try:
        x = int(input("Guess: "))  

        if x == number:
            print("Just right!")
        elif x > number:
            print("Too large!")
        elif x < number:
            print("Too small")  
    except:
        pass          
