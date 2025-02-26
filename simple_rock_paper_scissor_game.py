import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________) '''
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list1 = [rock,paper,Scissors]
user_choice = int(input("what do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice > 2 :
    print("You Lose.Typed more than 2.")
else:
    print(f"you chose:\n{list1[user_choice]}")
    rand_choice = random.randint(0,2)
    comp_choice = list1[rand_choice]
    print(f"computer chose:\n{comp_choice}")

    if user_choice == rand_choice:
        print("Its a Draw.")
    elif user_choice > rand_choice and rand_choice==1:
        print("You Win.")
    elif user_choice > rand_choice and user_choice!=1:
        print("You Lose.")
    elif user_choice > rand_choice and user_choice==1:
        print("You Win.")
    elif rand_choice > user_choice and user_choice ==1:
        print("You Lose.")
    elif rand_choice > user_choice and rand_choice!=1:
        print("You Win .")
    elif rand_choice > user_choice and rand_choice ==1:
        print("You Lose.")
    


