
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise7(CustomTestCase):

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
        Example 1: 4 Christmases
        """
        inputs = ["4 Christmases"]
        output = self.run_exercise(inputs)
        expected_output = "Four Christmases"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Example 2: Fantastic 4
        """
        inputs = ["Fantastic 4"]
        output = self.run_exercise(inputs)
        expected_output = "Fantastic Four"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Example 3: The Nutcracker and the 4 Realms
        """
        inputs = ["The Nutcracker and the 4 Realms"]
        output = self.run_exercise(inputs)
        expected_output = "The Nutcracker and the Four Realms"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Example 4: 4 score and 7 years ago
        """
        inputs = ["4 score and 7 years ago"]
        output = self.run_exercise(inputs)
        expected_output = "Four score and 7 years ago"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Example 5: 4th of July
        """
        inputs = ["4th of July"]
        output = self.run_exercise(inputs)
        expected_output = "Fourth of July"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
