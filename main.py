# project - (The perfect guess game)

import random
n = random.randint(1, 100)
a = -1
guesses = 0

while(a != n):
    
    a = int(input("Guess the number:"))
    if(a > n):
        print("please! Enter the Lower number")
        guesses += 1
    elif(a < n):
        print("Please! Enter the Higher number")
        guesses += 1
    
print(f"You have guessed the number {a} correctly in {guesses} attempt")