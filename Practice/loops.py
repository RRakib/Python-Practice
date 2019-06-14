########## While Loop
# i = 1
# while i < 10:
#     print(i)
#     i += 1
# testVariable = 1
# while testVariable == 1:
#     store = int(input("Enter a number: " ))
#     print("You entered: ", store)
# print("One entry taken")
# -----------------------------------------------------------
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
# started = False
# while True:
#     game = input("Command > ")
#     if game == "Start" or game == "start":
#         if started:
#             print("Car is already started!!")
#         else:
#             started = True
#             print("Car started. Get READY")
#     elif game == "Stop" or game == "stop":
#         if started:
#             started = False
#             print("Car stopping...")
#         else:    
#             print("Car already stopped!!")
#     elif game == "Quit" or game == "quit":
#         print("Quitting the game")
#         break
#     elif game == "Help" or game == "help":
#         print("""
#                 Start - to start the game 
#                 Stop - to stop the game
#                 Quit - to quit the game 
#             """)
#     else:
#         print("Command not found. Please write 'Help' to get instructions")
# -----------------------------------------------------------

########## For Loop
# for char in ["Python" , "React" , "Node"]:
# print(char)
# -----------------------------------------------------------
# for char in "Python":
#     print(char)
# -----------------------------------------------------------
# for nums in range(10):
#     print(nums)
# -----------------------------------------------------------
# for nums in range(10 , 20):
#     print(nums)
# -----------------------------------------------------------
# for nums in range(10 ,22 ,2):
#     print(nums)
# -----------------------------------------------------------
# for a in list(range(5)):
#     print(a)
# -----------------------------------------------------------
# for a in tuple(range(5)):
#     print(a)
# -----------------------------------------------------------
# for letter in 'Python':
#     print(letter)
# -----------------------------------------------------------
# user_input = int(input("Enter a nunber: "))
# tuple = (1, 2, 3, 4, 5)
# for number in tuple:
#     if user_input == number:
#         print("Number Found")
#         break
# else:
#     print("Number not found")
# -----------------------------------------------------------
# for letter in "Python":
#     if letter == "o":
#         break
#     print(letter)
# -----------------------------------------------------------
# for letter in "Python":
#     if letter == "t":
#         continue
#     print(letter)

########## Exercise 1
# total = 0
# all_items = [55 , 100 , 125]
# for item_cost in all_items:
#     total += item_cost
# print(f"Total : {total}")
# -----------------------------------------------------------
# all_items = input("Enter price: ")
# items_cost = all_items.split()
# sumV = 0
# for items in items_cost:
#     sumV += int(items)
# print(sumV)
# -----------------------------------------------------------

########## Exercise 2
# F_Shape = [ 5 , 2 , 5 , 2 , 2]
# for items in F_Shape:
#     x = 0
#     print("")
#     while x < items:
#         print("X" , end="")
#         x += 1
# -----------------------------------------------------------
# F_Shape = [ 1 , 1 , 1 , 5]
# for items in F_Shape:
#     output = ""
#     for numbers in range(items):
#         output += "X"
#     print(output)
# -----------------------------------------------------------

