
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise23(CustomTestCase):

    def test_function_usage(self):
        """
        The program should not use functions to solve the exercise.
        """
        self.assertNotUseSelfDefinedFunctions()

    def test_case_1(self):
        """
        Test case for converting the letter 'W' into Morse code.
        """
        inputs = ["W"]
        output = self.run_exercise(inputs)
        expected_output = ".--"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case for converting the number '9' into Morse code.
        """
        inputs = ["9"]
        output = self.run_exercise(inputs)
        expected_output = "----."
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case for converting the comma ',' into Morse code.
        """
        inputs = [","]
        output = self.run_exercise(inputs)
        expected_output = "--..--"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case for converting the word 'Python' into Morse code.
        """
        inputs = ["Python"]
        output = self.run_exercise(inputs)
        expected_output = ".--.-.---....----."
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case for converting the emoticon ':)' into Morse code.
        """
        inputs = [":)"]
        output = self.run_exercise(inputs)
        expected_output = "---...-.--.-"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main()
    unittest.main(testRunner=CustomTestRunner())
