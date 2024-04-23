import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise1(CustomTestCase):

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

    def provided_soltuion_usage(self):
        """
        The program should not use the provided solution to solve the exercise.
        """

        self.assertNotUsingProvidedSolution()

    def test_case_1(self):
        """
        The input is 125, the output should be 125125
        """
        inputs = ['125']
        output = self.run_exercise(inputs)
        expected_output = "125125"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        The input is 6, the output should be 66
        """
        inputs = ['6']
        output = self.run_exercise(inputs)
        expected_output = "66"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        The input is 1, the output should be 11
        """
        inputs = ['1']
        output = self.run_exercise(inputs)
        expected_output = "11"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        The input is 999, the output should be 999999
        """
        inputs = ['999']
        output = self.run_exercise(inputs)
        expected_output = "999999"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        The input is 10, the output should be 1010
        """
        inputs = ['10']
        output = self.run_exercise(inputs)
        expected_output = "1010"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
