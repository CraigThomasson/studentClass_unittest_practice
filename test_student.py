import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.full_name, 'John Doe' )


    def test_alert_santa(self):
        student = Student('John', 'Doe')
        student.alert_santa()

        self.assertTrue(student.naughty_list)


    def test_eamil_has_first_name_last_name(self):
        student = Student('John', 'Doe')
        

        self.assertEqual(student.email, f'{student._first_name}.{student._last_name}@email.com')



if __name__ == '__main__':
    unittest.main()