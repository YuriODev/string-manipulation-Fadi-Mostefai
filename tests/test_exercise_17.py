
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise17(CustomTestCase):

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
        inputs = ["Events happened very rapidly with Francis Morgan that late spring morning"]
        output = self.run_exercise(inputs)
        expected_output = "11"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case 2: First character is '0' and second character is '9'
        """
        inputs = ["The quick brown fox jumps over the lazy dog"]
        output = self.run_exercise(inputs)
        expected_output = "9"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case 3: First character is 'a' and second character is 'z'
        """
        inputs = ["Hello, world!"]
        output = self.run_exercise(inputs)
        expected_output = "2"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case 4: First character is 'A' and second character is 'Z'
        """
        inputs = ["This is a test"]
        output = self.run_exercise(inputs)
        expected_output = "4"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
