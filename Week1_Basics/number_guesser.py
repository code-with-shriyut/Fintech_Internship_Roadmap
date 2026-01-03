import random
# Random library helps us to pickup random numbers.
secret_number = random.randint(1,100) # Here the machine picks up the number.
print("I have chosen the number😗!!")
attempts_left = 5 # Here we are setting total number of attempts left to make the game more interesting!!
while attempts_left > 0:
    print(f"⚠ You have {attempts_left} lives left!!")
    guess_number = int(input("🤔 Guess the number... "))
    if guess_number == secret_number:
        print("You WON 🏆!")
        break # Here we break the loop because the user guessed the correct number.
    elif guess_number > secret_number: 
        print("Too HIGH 📈!!")
    else:
        print("Too LOW 📉!!")
    attempts_left = attempts_left - 1 # The number of attempts left are being caluclated here.
    
if attempts_left == 0 and guess_number != secret_number: 
    print("YOU LOST💀")
    print(f"The Secret Number was: {secret_number}")


