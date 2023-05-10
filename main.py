import random

user_score = 0
comp_score = 0
variations = ['rock', 'scissors', 'paper']

print("Welcome to the game!")

while True:
    user_choice = input('Type rock, paper, scissors or q for quit: ').lower()
    if user_choice == "q":
        break
    if user_choice not in variations:
        continue
    else:
        print("You choose", user_choice)
    comp_choice = random.randint(0, 2)
    print(comp_choice)
    if user_choice == 'rock' and comp_choice == 1:
        print('You won!')
        user_score += 1
    elif user_choice == 'paper' and comp_choice == 0:
        print('You won!')
        user_score += 1
    elif user_choice == 'scissors' and comp_choice == 2:
        print('You won!')
        user_score += 1
    else:
        print("You lost!")
        comp_score += 1
print(f"total score: You - {user_score}, Comp - {comp_score}")
print("see ya!")

