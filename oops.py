# # class car:
# #     color = "red"
# #     speed = 100
# # car1 = car()
# # print(car1.color)
# # car2 = car()
# # print(car2.speed)
# class car: 
#     def __init__(self,name):
#         self.name = name
#         self.color = "red"
#         self.speed = 100
# car1 = car("BMW")
# print(car1.name)
# print(car1.color)
# print(car1.speed)


# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# student1 = student("adesh",21)
# s2 = student("sachin",22)
# s3 = student("satyarth",23)
# print(student1.name)
# print(student1.age)
# print(s2.name)
# print(s2.age)
# print(s3.name)
# print(s3.age)

# class student:
#     def greet (self):
#         print("hello student")
# s1 = student()
# s1.greet()


class Student:

    def __init__(self,name,age,grade,marks):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = marks
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Grade:",self.grade)
        print("Marks:",self.marks)
s1 = Student("adesh",21,"21st",85)
s1.display()

# s1 = Student("adesh",21,"21st",85)
# print(s1.name)
# print(s1.age)
# print(s1.grade)
# print(s1.marks)