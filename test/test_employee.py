import unittest
from unittest.mock import patch
from classmethod import Employee

class Testemployee(unittest.TestCase):

    # Setup class is also a function that pulls down info 
    # for functions that you will need a paramete for but not to run always

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee('Bio', "Okafor", 50000)
        self.emp_2 = Employee('Dexter', "Okafor", 60000)

    def tearDown(self) -> None:
        print('tearDown \n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Bio.Okafor@gmail.com')
        self.assertEqual(self.emp_2.email, 'Dexter.Okafor@gmail.com')

        self.emp_1.first = "Ifeanyi"
        self.emp_2.first = "Odera"

        self.assertNotEqual(self.emp_1.email, 'Bio.Okafor@gmail.com')
        self.assertNotEqual(self.emp_2.email, 'Dexter.Okafor@gmail.com')

        self.assertEqual(self.emp_1.email, 'Ifeanyi.Okafor@gmail.com')
        self.assertEqual(self.emp_2.email, 'Odera.Okafor@gmail.com')

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, "Bio Okafor")
        self.assertEqual(self.emp_2.fullname, "Dexter Okafor")

        self.emp_1.first = "Ifeanyi"
        self.emp_2.first = "Odera"

        self.assertNotEqual(self.emp_1.fullname, 'Bio Okafor')
        self.assertNotEqual(self.emp_2.fullname, 'Dexter Okafor')

        self.assertEqual(self.emp_1.fullname, 'Ifeanyi Okafor')
        self.assertEqual(self.emp_2.fullname, 'Odera Okafor')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertNotEqual(self.emp_1.pay, 50000)
        self.assertNotEqual(self.emp_2.pay, 60000)

        self.assertEqual(self.emp_1.pay, 50000*1.04)
        self.assertEqual(self.emp_2.pay, 60000*1.04)

    def test_monthly_schedule(self):
        with patch('classmethod.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Okafor/May')
            self.assertEqual(schedule, "Success")

if __name__ == "__main__":
    unittest.main()