user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, or 2 for Scissors: "))
if 0 <= user_choice <= 2:
    list = ["""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """, """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """, """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """]
    if user_choice == 0:
        # print("Rock")
        print(list[0])

    elif user_choice == 1:
        # print("Paper")
        print(list[1])
    else:
        # print("Scissors")
        print(list[2])
else:
    print("You typed an invalid number, you lose!")

print("Computer Chose: ")
import random

computer_choice = random.randint(0, 2)
comp_list = ["""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """, """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """, """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """]
if computer_choice == 0:
    # print("Rock")
    print(comp_list[0])
elif computer_choice == 1:
    # print("Paper")
    print(comp_list[1])
else:
    # print("Scissors")
    print(comp_list[2])

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")





