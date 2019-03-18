#### Defining A Function
# def say_hello():
#     print("Good Morning")
#     print("It's a lovely day")
#
#
# print("Start")
# say_hello()
# print("END")
# -----------------------------------------------------------


# # Perameters
# def say_hello(name , day_type):
#     print(f"Good morning {name}")
#     print(f"It's a {day_type} day")
#
#
# print("Start")
# say_hello("Rakib" , "lovely")
# print("END")
# -----------------------------------------------------------


# # Positinal Arguments
# def say_hello(num_1 , num_2):
#     sumaiton = num_1 + num_2
#     print(sumaiton)
#
#
# say_hello(5 , 25)
# say_hello(15 , 25)
# -----------------------------------------------------------


# # Keyword Arguments
# def say_hello(num_1 , num_2):
#     subtraction = num_1 - num_2
#     print(subtraction)
#
#
# say_hello(num_2 = 5 , num_1 = 25)
# say_hello(5 , 25)
# -----------------------------------------------------------


# # Return Statement
# def calculation(x , y):
#     return x * y
#
#
# input_value1 = input("Enter First Value: ")
# input_value2 = input("Enter Second Value: ")
# print(calculation(int(input_value1) , int(input_value2)))
# -----------------------------------------------------------

# # Reusable Function
# def emoji(line):
#     words = line.split(" ")
#     emojies = {
#         ":)" : "🙂",
#         ":(" : "🙂",
#         ":'(" : "😢",
#     }
#     output = ""
#     for sentence in words:
#         output += emojies.get(sentence , sentence) + " "
#    
#     return output
#
#
# line = input("> ")
# print(emoji(line))
# -----------------------------------------------------------
