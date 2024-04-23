
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise27(CustomTestCase):

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
        Test case for the run-length encoding with input 'aaaabbbcaa'
        """
        inputs = ['aaaabbbcaa']
        output = self.run_exercise(inputs)
        expected_output = 'a4b3c1a2'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case for the run-length encoding with input 'abc'
        """
        inputs = ['abc']
        output = self.run_exercise(inputs)
        expected_output = 'a1b1c1'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case for the run-length encoding with input 'Hello'
        """
        inputs = ['Hello']
        output = self.run_exercise(inputs)
        expected_output = 'H1e1l2o1'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case for the run-length encoding with input 'abcdabcd'
        """
        inputs = ['abcdabcd']
        output = self.run_exercise(inputs)
        expected_output = 'a1b1c1d1a1b1c1d1'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case for the run-length encoding with input 'xyzxyzxyz'
        """
        inputs = ['xyzxyzxyz']
        output = self.run_exercise(inputs)
        expected_output = 'x1y1z1x1y1z1x1y1z1'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main()
    unittest.main(testRunner=CustomTestRunner())
