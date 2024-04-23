
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise21(CustomTestCase):

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
        Convert date format from '12/29/2022' to 'December 29, 2022'
        """
        inputs = ["12/29/2022"]
        output = self.run_exercise(inputs)
        expected_output = "December 29, 2022"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Convert date format from '03/04/2025' to 'March 04, 2025'
        """
        inputs = ["03/04/2025"]
        output = self.run_exercise(inputs)
        expected_output = "March 04, 2025"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Convert date format from '06/15/2030' to 'June 15, 2030'
        """
        inputs = ["06/15/2030"]
        output = self.run_exercise(inputs)
        expected_output = "June 15, 2030"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Convert date format from '09/01/2023' to 'September 01, 2023'
        """
        inputs = ["09/01/2023"]
        output = self.run_exercise(inputs)
        expected_output = "September 01, 2023"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Convert date format from '12/31/2024' to 'December 31, 2024'
        """
        inputs = ["12/31/2024"]
        output = self.run_exercise(inputs)
        expected_output = "December 31, 2024"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main()
    unittest.main(testRunner=CustomTestRunner())
