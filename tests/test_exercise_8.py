
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise8(CustomTestCase):

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
        The specified letter is 'a' and the string is "Curiouser and curiouser!" cried Alice (she was so much surprised that for the moment she quite forgot how to speak good English).
        """
        inputs = ['a', '"Curiouser and curiouser!" cried Alice (she was so much surprised that for the moment she quite forgot how to speak good English).']
        output = self.run_exercise(inputs)
        expected_output = '"Curiouser And curiouser!" cried Alice (she wAs so much surprised thAt for the moment she quite forgot how to speAk good English).'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        The specified letter is 'b' and the string is "The quick brown fox jumps over the lazy dog."
        """
        inputs = ['a', "The quick brown fox jumps over the lazy dog."]
        output = self.run_exercise(inputs)
        expected_output = "The quick brown fox jumps over the lAzy dog."
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        The specified letter is 'c' and the string is "Coding is fun!"
        """
        inputs = ['c', "Coding is fun!"]
        output = self.run_exercise(inputs)
        expected_output = "Coding is fun!"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        The specified letter is 'd' and the string is "Don't worry, be happy!"
        """
        inputs = ['a', "Don't worry, be happy!"]
        output = self.run_exercise(inputs)
        expected_output = "Don't worry, be hAppy!"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        The specified letter is 'e' and the string is "Everything is awesome!"
        """
        inputs = ['e', "Everything is awesome!"]
        output = self.run_exercise(inputs)
        expected_output = "EvErything is awEsomE!"
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
