class Student:
    def __init__(self, name = "ZD", age = 29):
        self.name = name
        self.age = age
    def say(self):
        print("Hello, My name is {0}".format(self.name))
def sayHello():
    print("saying")

print("Welcome to Pycharm!")