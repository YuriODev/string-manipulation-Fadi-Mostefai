
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise3(CustomTestCase):

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
        Test case 1:
        Inputs: ["45"]
        Expected Output: "2452"
        """
        inputs = ["45"]
        output = self.run_exercise(inputs)
        expected_output = "2452"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case 2:
        Inputs: ["1"]
        Expected Output: "212"
        """
        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "212"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case 3:
        Inputs: ["0"]
        Expected Output: "202"
        """
        inputs = ["0"]
        output = self.run_exercise(inputs)
        expected_output = "202"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case 4:
        Inputs: ["999"]
        Expected Output: "29992"
        """
        inputs = ["999"]
        output = self.run_exercise(inputs)
        expected_output = "29992"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case 5:
        Inputs: ["1234"]
        Expected Output: "212342"
        """
        inputs = ["1234"]
        output = self.run_exercise(inputs)
        expected_output = "212342"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
