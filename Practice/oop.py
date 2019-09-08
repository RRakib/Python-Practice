################## Class
# class Product:
#     def __init__(self,name,product,price):
#         self.name = name
#         self.product = product
#         self.price = price
#
# product1 = vars(Product('Business','iPhone',500))
# print(product1)
### Avaerage Rating Course
# class Course:
#     def __init__(self,name,rating):
#         self.name = name
#         self.rating = rating
#     def average(self):
#         result = 0
#         for rate in self.rating:
#             result += rate
#         return result/len(self.rating)
#
# course1 = Course('Bangla',[5,5,5,5,10])
# print('Average of',course1.name,'is:', int(course1.average()))
# course2 = Course('English',[10,10,10,10,10])
# print('Average of',course2.name ,'is:', int(course2.average()))