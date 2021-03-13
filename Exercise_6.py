import random
user_score = 0
cpu_score = 0


def points_calculator(input1, input2):
    global user_score
    global cpu_score
    if input1 == 1 and input2 == 1:
        print("CPU's Choice: SNAKE\nYOUR CHOICE: SNAKE")
        print(f"CPU = {cpu_score}\n{name} = {user_score}")
    elif input1 == 1 and input2 == 2:
        print("CPU's Choice: SNAKE\nYOUR CHOICE: WATER")
        user_score += 1
        print(f"CPU = {cpu_score}\n{name} = {user_score}")
    elif input1 == 1 and input2 == 3:
        print("CPU's Choice: SNAKE\nYOUR CHOICE: GUN")
        cpu_score += 1
        print(f"CPU = {cpu_score}\n{name} = {user_score}")
    elif input1 == 2 and input2 == 1:
        print("CPU's Choice: WATER\nYOUR CHOICE: SNAKE")
        user_score += 1
        print(f"CPU = {cpu_score}\n{name} = {user_score}")
    elif input1 == 2 and input2 == 2:
        print("CPU's Choice: WATER\nYOUR CHOICE: WATER")
        print(f"CPU = {cpu_score}\n{name} = {user_score}")
    elif input1 == 2 and input2 == 3:
        print("CPU's Choice: WATER\nYOUR CHOICE: GUN")
        cpu_score += 1
        print(f"CPU = {cpu_score}\n{name} = {user_score}")
    elif input1 == 3 and input2 == 1:
        print("CPU's Choice: GUN\nYOUR CHOICE: SNAKE")
        cpu_score += 1
        print(f"CPU = {cpu_score}\n{name} = {user_score}")
    elif input1 == 3 and input2 == 2:
        print("CPU's Choice: GUN\nYOUR CHOICE: WATER")
        user_score += 1
        print(f"CPU = {cpu_score}\n{name} = {user_score}")
    elif input1 == 3 and input2 == 3:
        print("CPU's Choice: GUN\nYOUR CHOICE: GUN")
        print(f"CPU = {cpu_score}\n{name} = {user_score}")
    else:
        print("Enter a valid choice!!: User score deducted for wrong input!!")
        user_score -= 1


print("##### WELCOME TO SNAKE, WATER, GUN GAME #####")
name = input("Enter your name: ")
print(f"Welcome {name}!")
number_of_rounds = int(input("How many rounds do you want to play?: "))
temp = number_of_rounds
while(number_of_rounds):
    print(f"\nROUND #{temp-number_of_rounds+1}")
    number_of_rounds -= 1
    user_choice = int(
        input("Choose one of the following:\n1. SNAKE\n2. WATER\n3. GUN\n=> "))
    cpu_choice = random.randint(1, 3)
    points_calculator(cpu_choice, user_choice)
print("\nGAME OVER!\n*************************************\n[FINAL SCORE]")
print(f"CPU : {cpu_score}\n{name} : {user_score}")
print("*************************************")
if user_score > cpu_score:
    print(f"Congratulations!! {name} Won the game")
elif user_score == cpu_score:
    print(
        f"This is a tie between {name} and CPU with {user_score} points each")
else:
    print("CPU won the game!!\nBetter luck next time xD")
