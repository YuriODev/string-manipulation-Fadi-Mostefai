
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise30(CustomTestCase):

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
        Test case 1: Converting 'MMMCMXCIX' should result in 3999.
        """
        inputs = ['MMMCMXCIX']
        output = self.run_exercise(inputs)
        expected_output = '3999'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case 2: Converting 'IV' should result in 4.
        """
        inputs = ['IV']
        output = self.run_exercise(inputs)
        expected_output = '4'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case 3: Converting 'XXI' should result in 21.
        """
        inputs = ['XXI']
        output = self.run_exercise(inputs)
        expected_output = '21'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case 4: Converting 'XLV' should result in 45.
        """
        inputs = ['XLV']
        output = self.run_exercise(inputs)
        expected_output = '45'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case 5: Converting 'CXXV' should result in 125.
        """
        inputs = ['CXXV']
        output = self.run_exercise(inputs)
        expected_output = '125'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
