class person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
class Child(person):
    def __init__(self,name,age,school):
        super().__init__(name,age)
        self.school = school
child1 = Child("adesh",21,"ABC school")
print(child1.name)
print(child1.age)
print(child1.school)    