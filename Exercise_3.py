# Guess The Number
guess_left = 5  # Number of trials
hidden_num = 37  # Hidden number
while(guess_left):
    guess = int(input("\nEnter your guess: "))
    guess_left = guess_left - 1
    if guess < hidden_num:
        print("The number you guessed is smaller\nTrials left =", guess_left)
    elif guess > hidden_num:
        print("The number you guessed is larger\nTrials left =", guess_left)
    else:
        print("\nCongratulations! You guessed it RIGHT!\nUnused Trials =", guess_left)
        break
if guess_left == 0:
    print("GAME OVER!")