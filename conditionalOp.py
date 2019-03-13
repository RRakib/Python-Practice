#### Exercise 1
# good_credit = False
# house_price = 1000000
# if good_credit:
#     down = (house_price / 100) * 10
#     print(f"Buyer will get {down}$ off")
# else:
#     down = (house_price / 100) * 20
#     print(f"Buyer will get {down}$ off")

#### Exercise 2
# name = input("Enter your name: " )
# if len(name) < 3:
#     print("Your name is too short")
# elif len(name) > 10:
#     print("Maximum character size is 10")
# else:
#     print("Name looks good")


#### Exercise 3
# weight = input("Weight: ")
# typ = input("(l)poubd or (k)kg? ")
# if typ == "l" or typ == "L":
#     wight = int(weight) * .45359237
#     print(f"You are {wight}kg")
# elif typ == "k" or typ == "K":
#     wight = int(weight) / .45359237
#     print(f"You are {wight}pound")
# else:
#     print(" Please input l for pound k for kg ")
# -----------------------------------------------------------


#### If Else , ElseIF(elif) Condition
# is_hot = True
# is_cold = True
# if is_hot :
#     print("It's a hot day. Drink more water")
# elif is_cold:
#     print("It's cold outside. Wear warm cloths")
# -----------------------------------------------------------
# temp = 35
# if temp > 30:
#     print("It's a hot day")
# elif temp < 15:
#     print("It's a cold day")
# else:
#     print("It's a lovely day") 
# -----------------------------------------------------------


#### Loop
# # While Loop
# i = 1
# while i < 10:
#     print(i)
#     i += 1
# -----------------------------------------------------------
# # While Loop Guess Number Game ****************************
# print("Guess the number between 0-9")
# attempt = 3
# startig_point = 1
# correct_guess = 9
# while startig_point <= attempt:
#     guess = input("Guess: ")
#     if int(guess) != correct_guess:
#         print(f"Better luck next time. (Attempt left: {attempt - startig_point })")
#         startig_point += 1
#     else:
#         print("You got it!!!!!")
#         break
# else:
#     print("You failed...")
# -----------------------------------------------------------
# # While Loop Car Game
game = ""
while game != "Quit":
    game = input("Command > ")
    if game == "Start" or game == "start":
        print("Car started. Get READY!")
    elif game == "Stop" or game == "stop":
        print("Stopping the car")
    elif game == "Quit" or game == "quit":
        print("Quitting the game")
        break
    elif game == "Help" or game == "help":
        print("""
                Start - to start the game 
                Stop - to stop the game
                Quit - to quit the game 
            """)
    else:
        print("Command not found. Please write 'Help' to get instructions")




#### Logical Operator
# # Logical "and"
# val_1 = True
# val_2 = True
# if val_1 and val_2:
#     print("Working")
# -----------------------------------------------------------
# # Logical "and not"
# val_1 = True
# val_2 = False
# if val_1 and not val_2:
#     print("Working")
# -----------------------------------------------------------
# # Logical "or"
# val_1 = True
# val_2 = False
# if val_1 or val_2:
#     print("Working")
# -----------------------------------------------------------