
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise20(CustomTestCase):

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
        Test case 1: First character is '1'
        """
        inputs = ["1239"]
        output = self.run_exercise(inputs)
        expected_output = "15"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case 2: First character is '8'
        """
        inputs = ["88"]
        output = self.run_exercise(inputs)
        expected_output = "16"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case 3: First character is '0'
        """
        inputs = ["01"]
        output = self.run_exercise(inputs)
        expected_output = "1"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case 4: First character is '4'
        """
        inputs = ["456"]
        output = self.run_exercise(inputs)
        expected_output = "15"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case 5: First character is '9'
        """
        inputs = ["999"]
        output = self.run_exercise(inputs)
        expected_output = "27"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
