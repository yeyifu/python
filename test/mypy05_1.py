#@property的用法，将方法当成属性调用
class Employee:

    @property
    def salary(self):
        print("salary running...")
        return 1000

e = Employee()
#e.salary()
print(e.salary)