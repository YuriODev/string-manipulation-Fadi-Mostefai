
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise10(CustomTestCase):

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
        The three-digit integer is 179.
        """
        inputs = ['179']
        output = self.run_exercise(inputs)
        expected_output = '17'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        The three-digit integer is 246.
        """
        inputs = ['246']
        output = self.run_exercise(inputs)
        expected_output = '12'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        The three-digit integer is 503.
        """
        inputs = ['503']
        output = self.run_exercise(inputs)
        expected_output = '8'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        The three-digit integer is 888.
        """
        inputs = ['888']
        output = self.run_exercise(inputs)
        expected_output = '24'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        The three-digit integer is 999.
        """
        inputs = ['999']
        output = self.run_exercise(inputs)
        expected_output = '27'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
