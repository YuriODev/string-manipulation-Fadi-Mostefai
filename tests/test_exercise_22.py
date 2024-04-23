
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise22(CustomTestCase):

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
        Test case 1
        """
        inputs = ["123          621"]
        output = self.run_exercise(inputs)
        expected_output = "No"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case 2
        """
        inputs = ["Never     odd   or        even"]
        output = self.run_exercise(inputs)
        expected_output = "Yes"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case 3
        """
        inputs = ["A man, a plan, a canal, Panama"]
        output = self.run_exercise(inputs)
        expected_output = "Yes"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case 4
        """
        inputs = ["Racecar"]
        output = self.run_exercise(inputs)
        expected_output = "Yes"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case 5
        """
        inputs = ["Hello world"]
        output = self.run_exercise(inputs)
        expected_output = "No"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main()
    unittest.main(testRunner=CustomTestRunner())
