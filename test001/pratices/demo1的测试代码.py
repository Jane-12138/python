import unittest
import 测试demo1

class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        #创建测试对象1
        self.person1=测试demo1.Employee('G','小姐',7000)
        #创建一组测试参数
        self.addsalarys=['',0,1000]
        return super().setUp()

    def test_give_default_raise(self):
        raisesalary=self.person1.give_raise(self.addsalarys[0])
        self.assertEqual(raisesalary,5000)
        
    def test_give_0_raise(self):
        raisesalary=self.person1.give_raise(self.addsalarys[1])
        self.assertEqual(raisesalary,5000)
       
    def test_notgive_raise(self):
        raisesalary=self.person1.give_raise()
        self.assertEqual(raisesalary,5000)

    def test_give_custom_raise(self):
        raisesalary=self.person1.give_raise(self.addsalarys[-1])
        self.assertNotEqual(raisesalary,5000)

unittest.main()