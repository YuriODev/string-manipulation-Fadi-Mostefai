
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise15(CustomTestCase):

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
# ### Input:
# - A string representing a simple arithmetic expression.

# ### Output:
# - The integer result of the expression.

# ### Examples:

# | No. | Inputs | Outputs |
# | --- | ------ | ------- |
# | 1   | 3*3    | 9       |
# | 2   | 50-49  | 1       |
# | 3   | 33+16  | 49      |
    def test_case_1(self):
        """
        The program should return the correct output for Example 1.
        """
        inputs = ['3*3']
        output = self.run_exercise(inputs)
        expected_output = '9'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        The program should return the correct output for Example 2.
        """
        inputs = ['50-49']
        output = self.run_exercise(inputs)
        expected_output = '1'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        The program should return the correct output for Example 3.
        """
        inputs = ['33+16']
        output = self.run_exercise(inputs)
        expected_output = '49'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
