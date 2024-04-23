
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


def draw_penguins(n):
    output = ""
    for i in range(1, n + 1):
        output += "   _~_        "
    output += "\n"

    for i in range(1, n + 1):
        output += "  (o o)       "
    output += "\n"

    for i in range(1, n + 1):
        output += " /  V  \\      "
    output += "\n"

    for i in range(1, n + 1):
        output += f"/(  {i}  )\\     "
    output += "\n"

    for i in range(1, n + 1):
        output += "  ^^ ^^       "
    output += "\n"

    return output


class TestExercise12(CustomTestCase):

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
        inputs = ['1']
        output = self.run_exercise(inputs)
        expected_output = draw_penguins(1)
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        The program should return the correct output for Example 2.
        """
        inputs = ['2']
        output = self.run_exercise(inputs)
        expected_output = draw_penguins(2)
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        The program should return the correct output for Example 3.
        """
        inputs = ['3']
        output = self.run_exercise(inputs)
        expected_output = draw_penguins(3)
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        The program should return the correct output for Example 4.
        """
        inputs = ['4']
        output = self.run_exercise(inputs)
        expected_output = draw_penguins(4)
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        The program should return the correct output for Example 5.
        """
        inputs = ['5']
        output = self.run_exercise(inputs)
        expected_output = draw_penguins(5)
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
