class Student:
    def __init__(self, name = "ZD", age = 29):
        self.name = name
        self.age = age
    def say(self):
        print("Hello, My name is {0}".format(self.name))
def sayHello():
    print("saying")
# 建议以此判断语句作为程序的入口
if __name__ == '__main__':
    print("Welcome to Pycharm!")