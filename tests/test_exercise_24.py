
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise24(CustomTestCase):

    def test_list_usage(self):
        """
        The program should not use lists to solve the exercise.
        """
        self.assertNotUsesList()

    def test_dict_usage(self):
        """
        The program should not use dictionaries to solve the exercise.
        """
        self.assertNoUsesDictionary()

    def test_function_usage(self):
        """
        The program should not use functions to solve the exercise.
        """
        self.assertNotUseSelfDefinedFunctions()

    def test_case_1(self):
        """
        Test case for the string 'Hello, Guido!'
        """
        inputs = ['Hello, Guido!']
        output = self.run_exercise(inputs)
        expected_output = '80.00\n20.00'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case for the string 'This is a Test'
        """
        inputs = ['This is a Test']
        output = self.run_exercise(inputs)
        expected_output = '81.82\n18.18'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case for the string 'PYTHON123'
        """
        inputs = ['PYTHON123']
        output = self.run_exercise(inputs)
        expected_output = '0.00\n100.00'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case for the string 'AbCdEfG'
        """
        inputs = ['AbCdEfGh']
        output = self.run_exercise(inputs)
        expected_output = '50.00\n50.00'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case for the string '1234567890'
        """
        inputs = ['1234567890']
        output = self.run_exercise(inputs)
        expected_output = '0.00\n0.00'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main()
    unittest.main(testRunner=CustomTestRunner())
