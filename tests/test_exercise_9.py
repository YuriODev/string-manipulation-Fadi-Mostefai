
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise9(CustomTestCase):

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
        The specified letter is 'a' and the string is "Hong Kong".
        """
        inputs = ["Hong Kong"]
        output = self.run_exercise(inputs)
        expected_output = "gong KonH"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        The specified letter is 'a' and the string is "Antarctica".
        """
        inputs = ["Antarctica"]
        output = self.run_exercise(inputs)
        expected_output = "antarcticA"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        The specified letter is 'n' and the string is "Python".
        """
        inputs = ["Python"]
        output = self.run_exercise(inputs)
        expected_output = "nythoP"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        The specified letter is 'b' and the string is "GitHub".
        """
        inputs = ["GitHub"]
        output = self.run_exercise(inputs)
        expected_output = "bitHuG"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        The specified letter is 'g' and the string is "Programming".
        """
        inputs = ["Programming"]
        output = self.run_exercise(inputs)
        expected_output = "grogramminP"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_6(self):
        """
        The specified letter is 'z' and the string is "Zebra".
        """
        inputs = ["Zebra"]
        output = self.run_exercise(inputs)
        expected_output = "aebrZ"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_7(self):
        """
        The specified letter is 'c' and the string is "C++".
        """
        inputs = ["C++"]
        output = self.run_exercise(inputs)
        expected_output = "++C"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_8(self):
        """
        The specified letter is 'a' and the string is "Ba".
        """
        inputs = ["Ba"]
        output = self.run_exercise(inputs)
        expected_output = "aB"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
