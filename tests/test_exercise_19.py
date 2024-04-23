
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise19(CustomTestCase):

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
        Test case 1: First character is '7'
        """
        inputs = ["1.79"]
        output = self.run_exercise(inputs)
        expected_output = "7"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case 2: First character is '8'
        """
        inputs = ["100.89"]
        output = self.run_exercise(inputs)
        expected_output = "8"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case 3: First character is '0'
        """
        inputs = ["6.045"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case 4: First character is '4'
        """
        inputs = ["3.14159"]
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case 5: First character is '5'
        """
        inputs = ["0.5"]
        output = self.run_exercise(inputs)
        expected_output = "5"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_6(self):
        """
        Test case 6: First character is '0'
        """
        inputs = ["12"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
