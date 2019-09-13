################ Try Expect
# try:
#     age = int(input("Age: "))
#     print(age)
# except ValueError:
#     print("Only Numerical Value Allowd")
# try:
#     age = int(input("Age: "))
#     salary = 65000
#     risk = salary/age
#     print(risk)
# except ValueError:
#     print("Only Numerical Value Allowd")
# except ZeroDivisionError:
#     print("Age can not be 0")

################ Try Except Else
# try:
#     age = int(input('Enter your age: '))
# except:
#     print('You must enter a numerical value')
# else:
#     print('You have successfully registered your age', age)

################ Try Finally
# try:
#     age = int(input('Enter your age: '))
#     wrong_age = age/0
#     print(wrong_age)
# finally:
#     print('You might have some problems but it still works')

################ Logging
# import logging
# logging.error('Errors')