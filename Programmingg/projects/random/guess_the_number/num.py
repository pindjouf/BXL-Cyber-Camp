import random
import os

solution = random.randrange(0, 100)
answer = int(input("Enter the number: "))
tries = 5

print(solution)

while answer != solution and tries > 0:
    print(tries, "tries left")
    tries -= 1
    answer = int(input("Enter the number: "))
    os.system('clear')
    if (answer == solution):
        print("GG bro :D")
    else:
        print("dumbass")
