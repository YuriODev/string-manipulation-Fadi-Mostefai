
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise14(CustomTestCase):

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
        inputs = ['   Beyond the green     swelling hills of the    Mittel Land rose mighty slopes of forest   up   to the lofty steeps of the Carpathians   themselves   ']
        output = self.run_exercise(inputs)
        expected_output = 'Beyond the green swelling hills of the Mittel Land rose mighty slopes of forest up to the lofty steeps of the Carpathians themselves'
        self.assertInCustom(expected=expected_output, actual=output, input_value=inputs)

    def test_case_2(self):
        """
        The program should return the correct output for Example 2.
        """
        inputs = ['   The quick brown fox jumps over the lazy dog   .']
        output = self.run_exercise(inputs)
        expected_output = 'The quick brown fox jumps over the lazy dog.'
        self.assertInCustom(expected=expected_output, actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
