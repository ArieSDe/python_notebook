class Student():
    pass

ZhangDi = Student()

class StudentPython():
    age = 18
    gender = None
    course = "Python"

    def doHomework(self):
        print("我在做作业")
        return None
# 实例化类
PanYueming = StudentPython()
print(PanYueming.age)
print(PanYueming.course)
print(PanYueming.gender)
PanYueming.doHomework()
StudentPython.age
StudentPython.doHomework()
PanYueming.age
PanYueming.doHomework()



