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
    randon_number = random.randint(0, 2)
    comp_choice = variations[randon_number]

    if user_choice == 'rock' and comp_choice == 'scissors':
        print('You won!')
        user_score += 1
    elif user_choice == 'paper' and comp_choice == 'rock':
        print('You won!')
        user_score += 1
    elif user_choice == 'scissors' and comp_choice == 'paper':
        print('You won!')
        user_score += 1
    else:
        print("You lost!")
        comp_score += 1
print(f"total score: You - {user_score}, Comp - {comp_score}")
print("See ya!")

