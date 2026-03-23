import random

def main():
    print("I'm thinking of a number between 1-100")
    number = random.randint(1,100)
    for i in range(1, 8):
        guess = int(input(f"Attempt {i}: "))
        if guess == number:
            print("You guessed the number!!!")
            break
        elif guess > number:
            print("Too high! Try lower")
        else:
            print("Too low! Try higher")
        if i == 7:
            print("Game Over!!!")
    pass

if __name__ == '__main__':
    main()