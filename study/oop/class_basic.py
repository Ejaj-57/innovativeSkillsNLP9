# class Student:
#     name = ""

# student1 = Student()
# student1.name = "Rasel"
# print(student1.name)

# student2 = Student()
# student2.name = "Warid"
# print(student2.name)

# constructor methos -> initialization 

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        
    def info(self):
        return self.name, self.roll


name = "Rasel"
roll= "082007"
student1 = Student(name, roll) 

name1, roll1 = student1.info()

print(name1, roll1)