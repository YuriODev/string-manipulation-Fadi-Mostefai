
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise13(CustomTestCase):

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
        The program should return the correct output for Example 1.
        """
        inputs = ['3+3=6']
        output = self.run_exercise(inputs)
        expected_output = '336'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        The program should return the correct output for Example 2.
        """
        inputs = ['2 * 3 = 6']
        output = self.run_exercise(inputs)
        expected_output = '236'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        The program should return the correct output for Example 3.
        """
        inputs = ['abc123def456']
        output = self.run_exercise(inputs)
        expected_output = '123456'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        The program should return the correct output for Example 4.
        """
        inputs = ['!@#$%^&*()']
        output = self.run_exercise(inputs)
        expected_output = ''
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        The program should return the correct output for Example 5.
        """
        inputs = ['9876543210']
        output = self.run_exercise(inputs)
        expected_output = '9876543210'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
