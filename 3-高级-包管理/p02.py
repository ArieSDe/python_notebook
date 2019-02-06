import p01#导入的同时，相当于被导入的代码先全部运行一遍
s = p01.Student("Pan", 30)
s.say()
p01.sayHello()

#借助于importlib包可以实现导入以数字开头的模块名称
import importlib
#导入了一个叫01的模块并把导入模块赋值给了tuling，这个包的名改为tuling
tuling = importlib.import_module("01")
stu = tuling.Student()
stu.say()
tuling.sayHello()
