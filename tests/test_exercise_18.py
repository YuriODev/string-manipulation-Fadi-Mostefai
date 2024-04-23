
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise18(CustomTestCase):

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
        Test case 1: First character is '2' and second character is '5'
        """
        inputs = ["2*5*7"]
        output = self.run_exercise(inputs)
        expected_output = "70"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case 2: First character is '3' and second character is '4'
        """
        inputs = ["3*4*6"]
        output = self.run_exercise(inputs)
        expected_output = "72"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case 3: First character is '1' and second character is '9'
        """
        inputs = ["1*9*8"]
        output = self.run_exercise(inputs)
        expected_output = "72"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case 4: First character is '2' and second character is '3'
        """
        inputs = ["2*3"]
        output = self.run_exercise(inputs)
        expected_output = "6"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case 5: First character is '4' and second character is '5'
        """
        inputs = ["4*5*6*7*8"]
        output = self.run_exercise(inputs)
        expected_output = "6720"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_6(self):
        """
        Test case 6: First character is '9' and second character is '9'
        """
        inputs = ["9*9*9*9*9*9*9"]
        output = self.run_exercise(inputs)
        expected_output = "4782969"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
