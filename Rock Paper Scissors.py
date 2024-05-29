import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0 , 2)

if choice == 0:
    print(rock,"\n")
    if computer_choice == 0:
        print("Computer chose:\n",rock,"\nDraw")
    elif computer_choice == 1:
        print("Computer chose:\n", paper, "\nYou loose")
    else:
        print("Computer chose:\n", scissors, "\nYou win")
elif choice == 1:
    print(paper,"\n")
    if computer_choice == 0:
        print("Computer chose:\n",rock,"\nYou win")
    elif computer_choice == 1:
        print("Computer chose:\n", paper, "\nDraw")
    else:
        print("Computer chose:\n", scissors, "\nYou loose")
elif choice == 2:
    print(scissors,"\n")
    if computer_choice == 0:
        print("Computer chose:\n",rock,"\nYou loose")
    elif computer_choice == 1:
        print("Computer chose:\n", paper, "\nYou win")
    else:
        print("Computer chose:\n", scissors, "\nDraw")

input()