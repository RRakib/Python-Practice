#### Exercise 1
# numbers = [ 15 , 20 , 5 , 25 , 6]
# maxNumber = numbers[0]
# for number in numbers:
#     if number > maxNumber:
#         maxNumber = number
# print(maxNumber)
# -----------------------------------------------------------


#### 2D List
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in matrix:
#     for column in row:
#         print(chr(column))
# -----------------------------------------------------------


#### List Methods
# # Append
# numbers = [ 1 , 2 , 3 , 10]
# numbers.append(50)
# print(numbers)
# -----------------------------------------------------------
# # Insert
# numbers = [ 1 , 2 , 3 , 10]
# numbers.insert(2 , 50)
# print(numbers)
# -----------------------------------------------------------
# # Remove
# numbers = [ 1 , 2 , 3 , 10 , 10]
# numbers.remove(10)
# print(numbers)
# -----------------------------------------------------------
# # Clear
# numbers = [ 1 , 2 , 3 , 10]
# numbers.clear()
# print(numbers)
# -----------------------------------------------------------
# # Pop
# numbers = [ 1 , 2 , 3 , 10]
# numbers.pop()
# print(numbers)
# -----------------------------------------------------------
# # Index
# numbers = [ 1 , 2 , 3 , 10]
# print(numbers.index(10))
# -----------------------------------------------------------
# # In
# numbers = [ 1 , 2 , 3 , 10]
# print(50 in numbers)
# -----------------------------------------------------------
# # Count
# numbers = [ 1 , 2 , 2 , 3 , 10]
# print(numbers.count(2))
# -----------------------------------------------------------
# # Sort
# numbers = [ 1 , 2 , 2 , 3 , 10 , 4 , 6]
# numbers.sort()
# print(numbers)
# -----------------------------------------------------------
# # Reverse
# numbers = [ 1 , 2 , 2 , 3 , 10 , 4 , 6]
# numbers.sort()
# numbers.reverse()
# print(numbers)
# -----------------------------------------------------------
# # Copy
# numbers = [ 1 , 2 , 2 , 3 , 10 , 4 , 6]
# numbers2 = numbers.copy()
# numbers2.append(15)
# print(numbers)
# print(numbers2)
# -----------------------------------------------------------
#### Exercise 2
# numbers = [ 1 , 2 , 2 , 3 , 10 , 4 , 6 , 10 , 4 , 6 , 10]
# for number in numbers:
#     if numbers.count(number) > 1:
#         numbers.remove(number)
# print(numbers)
# # # # # # # # # # # # # # # # # # # # # # # # OR OR OR OR OR
# numbers = [ 1 , 2 , 2 , 3 , 10 , 4 , 6 , 10 , 4 , 6 , 10]
# numbers2 = []
# for number in numbers:
#     if number not in numbers2:
#         numbers2.append(number)
# print(numbers2)
# -----------------------------------------------------------


#### Basic
# names = ["Rakib" , "Nayan" , "Aulad"]
# for name in names:
#     print(name)
# -----------------------------------------------------------