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
#         return sum(self.rating)/len(self.rating)
#
# course1 = Course('Bangla',[5,5,5,5,10])
# print('Average of',course1.name,'is:', int(course1.average()))
# course2 = Course('English',[10,10,10,10,10])
# print('Average of',course2.name ,'is:', int(course2.average()))
### Inner Class
# class Car:
#     class Engin:
#         def __init__(self):
#             print('Engine Started')
# car1 = Car()
# car1.Engin()
################## Encapsulation
# class Student:
#     def __init__(self):
#         self.__id = 16103030
#         self.__name = 'Rakib Uddin'
#     def student_details(self):
#         return self.__id,self.__name
# student1 = Student()
# print(student1.student_details())
# print(student1._Student__id)
### Setter and Getter
# class Student:
#     def setId(self,id):
#         self.id = id
#     def getId(self):
#         print(self.id)
#     def setName(self,name):
#         self.name = name
#     def getName(self):
#         print(self.name)
# student1 = Student()
# student1.setId(16103030)
# student1.setName('Rakib Uddin')
# student1.getId()
# student1.getName()
################## Inheritence
# class Vehical:
#     def __init__(self, tire,wheel,type):
#         self.tire = tire
#         self.wheel = wheel
#         self.type= type
#     def drive(self):
#         print('Driving a', self.type)
# class Car(Vehical):
#     def __init__(self,brand,model,tire,wheel):
#         Vehical.__init__(self,tire,wheel)
#         self.brand = brand
#         self.model = model
# class Bike(Vehical):
#     def __init__(self,price,tire,wheel,type):
#         Vehical.__init__(self,tire,wheel,type)
#         self.price = price
# suzuki = Bike(200000,140,'No','Bike')
# suzuki.drive()
# print(vars(suzuki))