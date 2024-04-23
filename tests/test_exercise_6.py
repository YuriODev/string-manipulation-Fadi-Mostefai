
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise6(CustomTestCase):

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
        The string contains only letters.
        """
        inputs = ["abc"]
        output = self.run_exercise(inputs)
        expected_output = "Your message includes letters only."
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        The string contains numbers and letters.
        """
        inputs = ["Street122"]
        output = self.run_exercise(inputs)
        expected_output = "Your message includes numbers and letters."
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        The string contains numbers only.
        """
        inputs = ["23"]
        output = self.run_exercise(inputs)
        expected_output = "Your message includes numbers only."
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        The string contains only letters.
        """
        inputs = ["HelloWorld"]
        output = self.run_exercise(inputs)
        expected_output = "Your message includes letters only."
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        The string contains numbers only.
        """
        inputs = ["12345"]
        output = self.run_exercise(inputs)
        expected_output = "Your message includes numbers only."
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
