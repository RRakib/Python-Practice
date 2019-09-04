############# Defining A Function
# def say_hello():
#     print("Good Morning")
#     print("It's a lovely day")
# print("Start")
# say_hello()
# print("END")

############# Perameters
# def say_hello(name , day_type):
#     print(f"Good morning {name}")
#     print(f"It's a {day_type} day")
# print("Start")
# say_hello("Rakib" , "lovely")
# print("END")

############# Positinal Arguments
# def say_hello(num_1 , num_2):
#     sumaiton = num_1 + num_2
#     print(sumaiton)
# say_hello(5 , 25)
# say_hello(15 , 25)

############# Keyword Arguments
# def say_hello(num_1 , num_2):
#     subtraction = num_1 - num_2
#     print(subtraction)
# say_hello(num_2 = 5 , num_1 = 25)
# say_hello(5 , 25)

############# Return Statement
# def calculation(x , y):
#     return x * y
# input_value1 = input("Enter First Value: ")
# input_value2 = input("Enter Second Value: ")
# print(calculation(int(input_value1) , int(input_value2)))

############# Reusable Function
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
#     return output
# line = input("> ")
# print(emoji(line))

############# Recursion Function
# def recursion_fun(data):
#     if data == 0:
#         result = 1
#     else:
#         result = data*recursion_fun(data - 1)
#     return result
# print(recursion_fun(8))

############# Lambda Function
# lambda_fun = lambda n:n**3
# print(lambda_fun(2))
### Even Odd Number
# even_odd = lambda num: 'Even' if num%2==0 else 'Odd'
# print(even_odd(5))
### Sum of 2 Number
# sum_of_2 = lambda num1,num2: num1+num2
# print(sum_of_2(2,5))
### Filter Form List
# list1 =[1,2,3,4,56,7]
# x = list(filter(lambda num: num%2 == 0, list1))
# print(x)
### Map Method
# list1 =[1,2,3,4,56,7]
# new_list = list(map(lambda num:num*2, list1))
# print(new_list)
### Reduce Method
# from functools import reduce
# list1 =[1,2,3,4,56,7]
# reduce_list = reduce(lambda num1,num2:num1+num2, list1)
# print(reduce_list)