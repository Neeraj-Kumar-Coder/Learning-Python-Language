# # class Sample:
# #     max = 100  # This is a class variable
# #     pass


# # member_1 = Sample() # Objects of the class
# # member_2 = Sample() # Objects of the class

# # member_1.name = "Sample 1"  # These are called instance variables
# # member_2.name = "Sample 2"  # These are called instance variables

# # member_1.roll = 10  # These are called instance variables
# # member_2.roll = 11  # These are called instance variables

# # print(member_1.name, member_2.name, member_1.roll,member_2.roll, member_1.max, member_2.max)

# # Sample.max = 101  # Changing the class variable by accessing it using the class name
# # print(member_1.name, member_2.name, member_1.roll,member_2.roll, member_1.max, member_2.max)
# # print(member_1.__dict__)
# # print(member_2.__dict__)


# # # METHODS IN CLASS
# # class Employee:
# #     no_of_leaves = 8  # Class variables

# #     def printdetails(self):  # This is a method to print the details of the object of the class
# #         return f"Name: {self.name}\nRoll number: {self.roll}\nWork experience: {self.experience}\nSalary: {self.salary}\nNumber of leaves: {self.no_of_leaves}"


# # employee_1 = Employee()  # This is a instance variable
# # employee_1.name = "Neeraj"  # This is a instance variable
# # employee_1.roll = 9  # This is a instance variable
# # employee_1.experience = 1  # This is a instance variable
# # employee_1.salary = None  # This is a instance variable

# # # It takes the function argument automatically!
# # print(employee_1.printdetails())


# # USING CONSTRUCTORS IN OOPS
# class Employee:
#     # This is a constructor which handels the arguments
#     def __init__(self, aname, aroll, asalary):
#         self.name = aname  # Arguments assignment
#         self.roll = aroll  # Arguments assignment
#         self.salary = asalary  # Arguments assignment

#     def printdetails(self):
#         return f"Name = {self.name}\nRoll = {self.roll}\nSalary = {self.salary}"


# # First argument always goes automatically as the object name
# Neeraj = Employee("Neeraj Kumar", 9, None) # Arguments goes like (Neeraj, "Neeraj Kumar", 9, None)
# print(Neeraj.printdetails())


# # Class method
# class Employee:
#     number_of_leaves = 5
#     # This is a constructor which handels the arguments

#     def __init__(self, aname, aroll, asalary):
#         self.name = aname  # Arguments assignment
#         self.roll = aroll  # Arguments assignment
#         self.salary = asalary  # Arguments assignment

#     def printdetails(self):
#         return f"Name = {self.name}\nRoll = {self.roll}\nSalary = {self.salary}"

#     @classmethod
#     def changeLeaves(cls, newValue):
#         cls.number_of_leaves = newValue


# Neeraj = Employee("Neeraj", 9, 150000)
# Neeraj.changeLeaves(10)
# print(Neeraj.number_of_leaves)
# print(Employee.number_of_leaves)


# # Class methods as alternative constructors
# class Employee:
#     number_of_leaves = 8

#     def __init__(self, aname, aroll, asalary):
#         self.name = aname
#         self.roll = aroll
#         self.salary = asalary

#     def printdetails(self):
#         return f"{self.name} {self.roll} {self.salary} {self.number_of_leaves}"

#     @classmethod
#     def from_str(cls, string):
#         # param = string.split("-")
#         # return cls(param[0], param[1], param[2])
#         return cls(*string.split("-"))


# Neeraj = Employee.from_str("Neeraj-Student-100")
# print(Neeraj.printdetails())


# # staticmethod

# class Employee:
#     number_of_leaves = 8

#     def __init__(self, aname, aroll, asalary):
#         self.name = aname
#         self.roll = aroll
#         self.salary = asalary

#     def printdetails(self):
#         return f"{self.name} {self.roll} {self.salary} {self.number_of_leaves}"

#     @staticmethod
#     def printjoke(string):
#         return f"This function is a joke: {string}"

#     @classmethod
#     def from_str(cls, string):
#         return cls(*string.split("-"))


# sample = Employee.from_str("Sample-Sample-Null")
# print(sample.printjoke("Checking..."))


# class Employee:
#     number_of_leaves = 8

#     def __init__(self, aname, aroll, asalary):
#         self.name = aname
#         self.roll = aroll
#         self.salary = asalary

#     def printdetails(self):
#         return f"{self.name} {self.roll} {self.salary} {self.number_of_leaves}"

#     @staticmethod
#     def printjoke(string):
#         return f"This function is a joke: {string}"

#     @classmethod
#     def from_str(cls, string):
#         return cls(*string.split("-"))


# class Programmer(Employee):
#     def printprog(self):
#         return f"{self.name} {self.roll} {self.salary} {self.number_of_leaves}"


# # Rahul = Programmer("Rahul", "Programmer", 500)
# Rahul = Programmer.from_str("Rahul-Programmer-500")
# print(Rahul.printprog())
# print(Rahul.printdetails())


# # Multiple Inhertance

# class Employee:
#     number_of_leaves = 7

#     def __init__(self, aname, aroll, asalary):  # Constructor
#         self.name = aname
#         self.roll = aroll
#         self.salary = asalary

#     @classmethod
#     def parseFill(cls, string):
#         return cls(*string.split("-"))

#     def printdetails(self):
#         return f"{self.name} {self.roll} {self.salary} {self.number_of_leaves}"


# class Player:
#     number_of_matches = 100

#     def __init__(self, aname, aage, games_list):
#         self.name = aname
#         self.age = aage
#         self.games = games_list

#     def printTrack(self):
#         return f"{self.name} {self.age} {self.games} {self.number_of_matches}"


# class CoolProgrammer(Employee, Player):
#     degree_of_coolness = 9

#     def printCool(self):
#         return f"{self.degree_of_coolness}"


# Neeraj = CoolProgrammer("Neeraj", "Programmer", 1000)
# Neeraj.games = 900
# print(Neeraj.printdetails())
# print(Neeraj.printCool())
# print(Neeraj.games)


# # Multilevel Inhertance

# class Dad:
#     legend = 1000


# class Son(Dad):
#     programmer = 99


# class Grandson(Son):
#     magical = 10
#     programmer = 91
#     def isLog(self):
#         return f"This is the test for the log attribute in the social form {self.magical}"


# Navya = Grandson()
# Reyansh = Son()
# print(Reyansh.programmer)
# print(Navya.programmer)


# # Public, Private and Protected access specifiers

# class Test:
#     public = 1
#     _protected = 2
#     __private = 3


# TestMem = Test()
# print(TestMem.public)
# print(TestMem._protected)
# # print(TestMem.__private)
# print(TestMem._Test__private)


# # Search flow of inherited class
# class A:
#     var2 = "I am class variable of class A"

#     # def __init__(self):
#     #     self.var2 = "I am instance variable of class A"


# class B(A):
#     var2 = "I am class variable of class B"

#     # def __init__(self):
#     #     self.var2 = "I am instance variable of class B"


# instanceVariable = B()
# print(instanceVariable.var2)


# super() and overriding in classes

class A:
    var1 = 10

    def __init__(self):
        self.var2 = 90
        self.special = "I am special"


class B(A):
    var2 = 19

    def __init__(self):
        super().__init__()
        self.var2 = 70


sourav = B()
print(sourav.var2)
print(sourav.special)
