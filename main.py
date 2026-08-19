import random
secret = random.randint(1,50)

attempts = 0
while attempts < 5:
    guess = int(input("Guess the number."))
    attempts = attempts + 1
    if abs(secret- guess) <= 5:
        print("Hot.")
    elif abs(secret- guess) <= 10:
        print("Cold.")
    elif abs(secret - guess) <= 20:
        print("Very Cold.")
    if guess != secret and attempts == 0:
        print("You lost.")
    elif guess == secret:
        print("You win!")
if attempts == 5:
    print("You lost and secret number was this:",secret)


