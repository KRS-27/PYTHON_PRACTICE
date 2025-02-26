print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island. ")
print("Your mission is to find your treasure. ")
choice_1 = input('you are at a cross road. where do you want to go?\n   Type "left" or "right"\n ')
if (choice_1 == "left") :
    choice_2 =  input("you come to a lake. There is an island in middle.\n   Type 'wait' or 'swim'\n" )
    if choice_2 == "wait" :
        choice_3 = input("There are 3 doors what do you like to open: red, yellow, blue?")
        if choice_3 == "yellow":
            print("you won. Treasure is yours.")
        elif choice_3 == "red" :
            print("You stepped into fire.Game over.")
        elif choice_3 == "blue" :
            print("You eaten by Lion. Game over.")
        else :
            print("You typed something wrong. Game over.")
    elif choice_2 == "swim":
        print("game over")
    else:
        print("You typed something wrong. Game over.")
    
elif choice_1 == "right":
    print("game over.")

else:
    print("You typed something wrong. Game over.")