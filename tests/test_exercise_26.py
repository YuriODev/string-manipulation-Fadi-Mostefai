
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


def multiplication_table(a, b, c, d):
    a, b, c, d = int(a), int(b), int(c), int(d)
    table = ""
    table += "\t"
    for i in range(c, d + 1):
        table += str(i) + "\t"
    table += "\n"

    for i in range(a, b + 1):
        table += str(i) + "\t"
        for j in range(c, d + 1):
            table += str(i * j) + "\t"
        table += "\n"

    return table


class TestExercise26(CustomTestCase):

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
        Test case for the multiplication table with inputs ['1', '4', '2', '5']
        """
        inputs = ['1', '4', '2', '5']
        output = self.run_exercise(inputs)
        expected_output = multiplication_table(*inputs)
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case for the multiplication table with inputs ['2', '5', '3', '6']
        """
        inputs = ['2', '5', '3', '6']
        output = self.run_exercise(inputs)
        expected_output = multiplication_table(*inputs)
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case for the multiplication table with inputs ['0', '3', '1', '4']
        """
        inputs = ['0', '3', '1', '4']
        output = self.run_exercise(inputs)
        expected_output = multiplication_table(*inputs)
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case for the multiplication table with inputs ['5', '8', '2', '3']
        """
        inputs = ['5', '8', '2', '3']
        output = self.run_exercise(inputs)
        expected_output = multiplication_table(*inputs)
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case for the multiplication table with inputs ['1', '1', '1', '1']
        """
        inputs = ['1', '1', '1', '1']
        output = self.run_exercise(inputs)
        expected_output = multiplication_table(*inputs)
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main()
    unittest.main(testRunner=CustomTestRunner())
