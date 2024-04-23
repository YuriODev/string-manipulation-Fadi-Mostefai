
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise16(CustomTestCase):

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
        Test case 1: First character is 'A' and second character is 'F'
        """
        inputs = ["A", "F"]
        output = self.run_exercise(inputs)
        expected_output = "ABCDEF"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case 2: First character is '0' and second character is '9'
        """
        inputs = ["0", "9"]
        output = self.run_exercise(inputs)
        expected_output = "0123456789"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case 3: First character is 'a' and second character is 'z'
        """
        inputs = ["a", "z"]
        output = self.run_exercise(inputs)
        expected_output = "abcdefghijklmnopqrstuvwxyz"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case 4: First character is 'A' and second character is 'Z'
        """
        inputs = ["A", "Z"]
        output = self.run_exercise(inputs)
        expected_output = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case 5: First character is '!' and second character is '@'
        """
        inputs = ["!", "@"]
        output = self.run_exercise(inputs)
        expected_output = "!\"#$%&'()*+,-./0123456789:;<=>?@"

        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
