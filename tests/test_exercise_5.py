
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise5(CustomTestCase):

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
        Test case 1: Lords of the World
        """
        inputs = ["Lords of the World", "But who shall dwell in these worlds if they be inhabited? Are we or they Lords of the World? And how are all things made for man?"]
        output = self.run_exercise(inputs)
        expected_output = "Yes"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case 2: Python and Java
        """
        inputs = ["Python", "Java is a general-purpose programming language that is class-based, object-oriented, and designed to have as few implementation dependencies as possible."]
        output = self.run_exercise(inputs)
        expected_output = "No"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case 3: Hello and Hello, World!
        """
        inputs = ["Hello", "Hello, World!"]
        output = self.run_exercise(inputs)
        expected_output = "Yes"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case 4: Python
        """
        inputs = ["Python", "Python is a high-level, interpreted, interactive, and object-oriented scripting language."]
        output = self.run_exercise(inputs)
        expected_output = "Yes"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case 5: Java
        """
        inputs = ["Java", "Java is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible."]
        output = self.run_exercise(inputs)
        expected_output = "Yes"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
