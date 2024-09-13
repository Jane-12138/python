'''
11-3 雇员雇员 ：编写一个名为Employee 的类，其方法__init__() 接受名、姓和年薪，并将它们都存储在属性中。
编写一个名为give_raise() 的方法，它默认将年薪增加5000美元，但也能够接受其他的年薪增加量。

为Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_raise() 和test_give_custom_raise() 。
使用方法setUp() ，以免在每个测试方法中都创建新的雇员实例。运行这个测试用例，确认两个测试都通过了
'''

class Employee():
    def __init__(self,name,surname,salary):
        self.name=name
        self.surname=surname
        self.salary=salary

    def give_raise(self,addsalary=5000):
        if addsalary=='' or addsalary==0:
            addsalary=5000
        else:int(addsalary)
        allsalary=self.salary+addsalary
        print(self.name+self.surname+'你今年的年薪是：'+str(allsalary))
        return addsalary
            
# p1=Employee('G','先生',5000)
# p1.give_raise(5000)