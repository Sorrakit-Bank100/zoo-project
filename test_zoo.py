import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50) 
        self.assertEqual(self.zoo.get_ticket_price(-5),"Invalid") # < 0 
        self.assertEqual(self.zoo.get_ticket_price(12), 50)  # 0-12
        self.assertEqual(self.zoo.get_ticket_price(15),100)  # 13-20
        self.assertEqual(self.zoo.get_ticket_price(25),150)  # 21-60
        self.assertEqual(self.zoo.get_ticket_price(65),100)  # <60


    def test_BVA_Case(self):
       self.assertEqual(self.zoo.get_ticket_price(-1),"Invalid")  # class < 0 
       self.assertEqual(self.zoo.get_ticket_price(0),50)  # class 0-12  test 0
       self.assertEqual(self.zoo.get_ticket_price(12),50)  # class 0-12 test 12
       self.assertEqual(self.zoo.get_ticket_price(13),100)  # class 13-20 test 13
       self.assertEqual(self.zoo.get_ticket_price(20),100)  # class 13-20 test 20
       self.assertEqual(self.zoo.get_ticket_price(21),150)  # class 21-60 test 21
       self.assertEqual(self.zoo.get_ticket_price(60),150)  # class 21-60 test 60
       self.assertEqual(self.zoo.get_ticket_price(61),100)  # class >60 test 61


    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()