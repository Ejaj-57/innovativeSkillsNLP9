'''
-> Inheritacne is creating a parent-child realtionship between two classes, where the child class will access variables and methods of the base/parent class automatically.

-> inheritance helps the code to be reusable
-> we use inheritance to increase reusability of codes
'''

class Software_developer:
    def __init__(self, exp_level):
        self.exp = exp_level
    
    def Cal_salary(self):
        base_salary = 10000
        actual_salary = base_salary * self.exp
        print(actual_salary)

class Intern(Software_developer):
    pass
class Mid_level(Software_developer):
    pass
class Senior(Software_developer):
    pass

intern1 = Intern(1)
mid_level1 = Mid_level(2)
senior1 = Senior(3)

intern1.Cal_salary()
mid_level1.Cal_salary()
senior1.Cal_salary()

'''
-> Types of Inheritance
1. single 
2. Multi-level
3. Hierarchical
4. Multiple

Single Inheritance: One Base Class and One derived or child class
'''




        