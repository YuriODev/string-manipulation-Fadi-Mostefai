
import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise25(CustomTestCase):

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
        Test case for the string 'C:\\Python36\\python.exe'
        """
        inputs = ['C:\\Python36\\python.exe']
        output = self.run_exercise(inputs)
        expected_output = 'C:\nPython36\npython.exe'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_2(self):
        """
        Test case for the string 'D:\\Documents\\file.txt'
        """
        inputs = ['D:\\Documents\\file.txt']
        output = self.run_exercise(inputs)
        expected_output = 'D:\nDocuments\nfile.txt'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_3(self):
        """
        Test case for the string 'E:\\Programs\\program.exe'
        """
        inputs = ['E:\\Programs\\program.exe']
        output = self.run_exercise(inputs)
        expected_output = 'E:\nPrograms\nprogram.exe'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_4(self):
        """
        Test case for the string 'F:\\Files\\document.docx'
        """
        inputs = ['F:\\Files\\document.docx']
        output = self.run_exercise(inputs)
        expected_output = 'F:\nFiles\ndocument.docx'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)

    def test_case_5(self):
        """
        Test case for the string 'G:\\Pictures\\image.jpg'
        """
        inputs = ['G:\\Pictures\\image.jpg']
        output = self.run_exercise(inputs)
        expected_output = 'G:\nPictures\nimage.jpg'
        self.assertInCustom(expected=expected_output, actual=output,
                            input_value=inputs)


if __name__ == '__main__':
    unittest.main()
    unittest.main(testRunner=CustomTestRunner())
