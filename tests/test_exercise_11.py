
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise11(CustomTestCase):

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
        The program should return 'Watson' for the input 'Holmes & Watson'.
        """
        inputs = ['Holmes & Watson']
        output = self.run_exercise(inputs)
        expected_output = 'Watson'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        The program should return 'dog.' for the input 'The quick brown fox jumps over the lazy dog.'.
        """
        inputs = ['The quick brown fox jumps over the lazy dog.']
        output = self.run_exercise(inputs)
        expected_output = 'dog.'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        The program should return 'World' for the input 'Hello World'.
        """
        inputs = ['Hello World']
        output = self.run_exercise(inputs)
        expected_output = 'World'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        The program should return 'Copilot' for the input 'GitHub Copilot'.
        """
        inputs = ['GitHub Copilot']
        output = self.run_exercise(inputs)
        expected_output = 'Copilot'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        The program should return 'challenging.' for the input 'Programming is fun and challenging.'.
        """
        inputs = ['Programming is fun and challenging.']
        output = self.run_exercise(inputs)
        expected_output = 'challenging.'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_6(self):
        """
        The program should return 'Python' for the input 'Python is a programming language.'.
        """
        inputs = ['Python.']
        output = self.run_exercise(inputs)
        expected_output = 'Python'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
