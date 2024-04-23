import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise2(CustomTestCase):

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

    def provided_soltuion_usage(self):
        """
        The program should not use the provided solution to solve the exercise.
        """

        self.assertNotUsingProvidedSolution()

    def test_case_1(self):
        """
        The input is 'A scandal in Bohemia', the output should be 'A Scandal In Bohemia'
        """
        inputs = ['A scandal in Bohemia']
        output = self.run_exercise(inputs)
        expected_output = 'A Scandal In Bohemia'
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_2(self):
        """
        The input is 'The adventure of the Blue Carbuncle', the output should be 'The Adventure Of The Blue Carbuncle'
        """
        inputs = ['The adventure of the Blue Carbuncle']
        output = self.run_exercise(inputs)
        expected_output = 'The Adventure Of The Blue Carbuncle'
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_3(self):
        """
        The input is 'The Boscombe valley mystery', the output should be 'The Boscombe Valley Mystery'
        """
        inputs = ['The Boscombe valley mystery']
        output = self.run_exercise(inputs)
        expected_output = 'The Boscombe Valley Mystery'
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_4(self):
        """
        The input is 'The Hound of the Baskervilles', the output should be 'The Hound Of The Baskervilles'
        """
        inputs = ['The Hound of the Baskervilles']
        output = self.run_exercise(inputs)
        expected_output = 'The Hound Of The Baskervilles'
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_case_5(self):
        """
        The input is 'The Sign of Four', the output should be 'The Sign Of Four'
        """
        inputs = ['The Sign of Four']
        output = self.run_exercise(inputs)
        expected_output = 'The Sign Of Four'
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
