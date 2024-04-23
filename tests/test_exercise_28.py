
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise28(CustomTestCase):

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
        Test case 1: Do you play any sports? Yes, I like to play basketball.
        """
        inputs = ["Do you play any sports? Yes, I like to play basketball."]
        output = self.run_exercise(inputs)
        expected_output = "11"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case 2: How many siblings do you have? I have two sisters and one brother.
        """
        inputs = ["How many siblings do you have? I have two sisters and one brother."]
        output = self.run_exercise(inputs)
        expected_output = "13"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case 3: What is your favorite color? My favorite color is blue.
        """
        inputs = ["What is your favorite color? My favorite color is blue."]
        output = self.run_exercise(inputs)
        expected_output = "10"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case 4: First character is 'A' and second character is 'Z'
        """
        inputs = ["This is a test"]
        output = self.run_exercise(inputs)
        expected_output = "4"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
