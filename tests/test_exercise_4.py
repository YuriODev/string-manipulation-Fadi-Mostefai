
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise4(CustomTestCase):

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
        Test case 1:
        Description: Check if the function returns False when given inputs
        'Python' and 'Ruby'.
        Expected output: False
        """
        inputs = ['Python','Ruby']
        output = self.run_exercise(inputs)
        expected_output = "False"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case 2:
        Description: Check if the function returns True when given inputs
        'Java' and 'JavaScript'.
        Expected output: True
        """
        inputs = ['Java', 'JavaScript']
        output = self.run_exercise(inputs)
        expected_output = "True"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case 3:
        Description: Check if the function returns True when given inputs
        'C++' and 'C#'.
        Expected output: True
        """
        inputs = ['C++', 'C#']
        output = self.run_exercise(inputs)
        expected_output = "True"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case 4:
        Description: Check if the function returns False when given inputs
        'HTML' and 'CSS'.
        Expected output: False
        """
        inputs = ['HTML', 'CSS']
        output = self.run_exercise(inputs)
        expected_output = "False"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case 5:
        Description: Check if the function returns True when given inputs
        'PHP' and 'Python'.
        """
        inputs = ['PHP', 'Python']
        output = self.run_exercise(inputs)
        expected_output = "True"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
