# Exercises 🏋️‍♂️

Here are the exercises for the Python Basics module. These exercises are designed to test your understanding of the concepts covered in the module. You can use the exercises to practice and improve your Python skills.

**Covered Topics:**

- Simple Input/Output in a loop
- Break and Continue
- Nested Loops
- Conditional Statements
- Loops



## Exercise 1: Double the Number - Easy 😊 (Est. Time: 5 mins | Points: 10)

**Problem:** Given a natural number, find the number formed by appending the same number to itself.

### Input:
- A natural number.

### Output:
- The number formed by appending the input number to itself.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 125    | 125125  |
| 2   | 6      | 66      |
| 3   | 1      | 11      |
| 4   | 999    | 999999  |


### Note:
The problem tests the ability to manipulate strings and integers to construct a new number.

## Exercise 2: Title Case Conversion - Easy 😊 (Est. Time: 5 mins | Points: 10)

**Problem:** Given a string, change the case of the characters in the string such that the first letter of each word is uppercase and all other letters are lowercase.

### Input:
- A string representing a sentence.

### Output:
- The sentence with each word's first letter capitalized and all other letters in lowercase.

### Examples:

| No. | Inputs                                  | Outputs                                  |
| --- | --------------------------------------- | ---------------------------------------- |
| 1   | A scandal in Bohemia                    | A Scandal In Bohemia                     |
| 2   | The adventure of the Blue Carbuncle     | The Adventure Of The Blue Carbuncle      |
| 3   | The Boscombe valley mystery             | The Boscombe Valley Mystery              |
| 4   | The Hound of the Baskervilles           | The Hound Of The Baskervilles            |
| 5   | The Sign of Four                        | The Sign Of Four                         |

### Note:
The problem tests the ability to use string manipulation functions to format text properly.



## Exercise 3: Add Twos to Number - Easy 😊 (Est. Time: 5 mins | Points: 10)

**Problem:** Given a natural number, find the number that results from appending the digit '2' to both the beginning and the end of the input number.

### Input:
- A natural number.

### Output:
- The number formed by appending '2' to both the beginning and end of the input number.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 45     | 2452    |
| 2   | 1      | 212     |
| 3   | 0      | 202     |
| 4   | 999    | 29992   |
| 5   | 1234   | 212342  |

### Note:
This problem tests string manipulation skills, focusing on modifying numerical strings by appending and prepending characters.

## Exercise 4: Letter Match - Easy 😊 (Est. Time: 5 mins | Points: 10)

**Problem:** Given two words, determine if the first word starts with the same letter that the second word ends with.

### Input:
- Two words.

### Output:
- "True" if the first word starts with the same letter the second word ends with, otherwise "False".

### Examples:

| No. | Inputs     | Outputs |
| --- | ---------- | ------- |
| 1   | Python<br>Ruby | False |
| 2   | Java<br>JavaScript | True |
| 3   | C++<br>C# | True |
| 4   | HTML<br>CSS | False |
| 5   | PHP<br>Python | True |

### Note:
The problem tests the ability to manipulate and compare string characters effectively.

## Exercise 5: Substring Check - Easy 😊 (Est. Time: 5 mins | Points: 10)

**Problem:** Given two strings that may contain spaces, print "Yes" if the first string is a substring of the second string, otherwise print "No".

### Input:
- Two strings.

### Output:
- "Yes" if the first string is a substring of the second string, otherwise "No".

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | Lords of the World<br>But who shall dwell in these worlds if they be inhabited? Are we or they Lords of the World? And how are all things made for man? | Yes |
| 2   | Python<br>Java is a general-purpose programming language that is class-based, object-oriented, and designed to have as few implementation dependencies as possible. | No |
| 3   | Hello<br>Hello, World! | Yes |
| 4   | Python<br>Python is a high-level, interpreted, interactive, and object-oriented scripting language. | Yes |
| 5   | Java<br>Java is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. | Yes |

### Note:
This problem examines the ability to work with substrings and perform string searches.

## Exercise 6: Character Content Analysis - Easy 😊 (Est. Time: 5 mins | Points: 10)

**Problem:** Write a program to check what characters a string entered by the user consists of: only digits, only letters, or both letters and digits.

### Input:
- A string.

### Output:
- A message specifying if the string contains only letters, only digits, or both.

### Examples:

| No. | Inputs     | Outputs                                   |
| --- | ---------- | ----------------------------------------- |
| 1   | abc        | Your message includes letters only.       |
| 2   | Street122  | Your message includes numbers and letters.|
| 3   | 23         | Your message includes numbers only.       |
| 4   | HelloWorld | Your message includes letters only.       |
| 5   | 12345      | Your message includes numbers only.       |

### Note:
This problem helps practice string manipulation and character classification.

## Exercise 7: Replace Digits with Words - Easy 😊 (Est. Time: 5 mins | Points: 10)

**Problem:** Given a string, replace all occurrences of the digit '4' with the word "Four".

### Input:
- A string.

### Output:
- The modified string where all '4's have been replaced with "Four".

### Examples:

| No. | Inputs                                 | Outputs                                         |
| --- | -------------------------------------- | ----------------------------------------------- |
| 1   | 4 Christmases                          | Four Christmases                                |
| 2   | Fantastic 4                            | Fantastic Four                                  |
| 3   | The Nutcracker and the 4 Realms        | The Nutcracker and the Four Realms              |
| 4   | 4 score and 7 years ago                | Four score and 7 years ago                      |
| 5   | 4th of July                            | Fourth of July                                  |

### Note:
Focus on string replacement techniques for specific characters.

## Exercise 8: Uppercase Specific Letter - Easy 😊 (Est. Time: 5 mins | Points: 10)

**Problem:** Write a program that replaces all occurrences of a specified lowercase letter in a string with its uppercase counterpart. First, input the letter, then the string.

### Input:
- A character (the letter to change).
- A string.

### Output:
- The string with the specified letter changed to uppercase.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | a<br>"Curiouser and curiouser!" cried Alice (she was so much surprised that for the moment she quite forgot how to speak good English). | "Curiouser And curiouser!" cried Alice (she wAs so much surprised thAt for the moment she quite forgot how to speAk good English). |
| 2   | a<br>"The quick brown fox jumps over the lazy dog." | "The quick brown fox jumps over the lAzy dog." |
| 3   | c<br>"Coding is fun!" | "Coding is fun!" |
| 4   | a<br>"Don't worry, be happy!" | "Don't worry, be hAppy!" |

### Note:
This tests basic string manipulation and character transformation.

## Exercise 9: Swap First and Last Characters - Easy 😊 (Est. Time: 5 mins | Points: 10)

**Problem:** Write a program that swaps the first and last characters of a user-entered string.

### Input:
- A string.

### Output:
- The string with the first and last characters swapped.

### Examples:

| No. | Inputs      | Outputs      |
| --- | ----------- | ------------ |
| 1   | Hong Kong   | gong KonH    |
| 2   | Antarctica  | antarcticA   |
| 3   | Python      | nythoP       |
| 4   | GitHub      | bithuG       |
| 5   | Programming | grogramminP  |


### Note:
This exercise is great for learning about string indexing and manipulation.

## Exercise 10: Sum of Digits - Easy 😊 (Est. Time: 5 mins | Points: 10)

**Problem:** Given a positive three-digit number, find the sum of its digits. Do not use integer division or modulus operations.

### Input:
- A three-digit integer.

### Output:
- The sum of the digits.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 179    | 17      |
| 2   | 246    | 12      |
| 3   | 503    | 8       |
| 4   | 888    | 24      |
| 5   | 999    | 27      |

### Note:
Emphasizes string manipulation and conversion between data types without using direct numeric operations.

## Exercise 11: Find Last Word - Easy 😊 (Est. Time: 5 mins | Points: 10)

**Problem:** Write a program that outputs the last word in a string. A word is a sequence of non-space characters bounded by spaces or the ends of the string.

### Input:
- A string.

### Output:
- The last word in the string.

### Examples:

| No. | Inputs          | Outputs |
| --- | --------------- | ------- |
| 1   | Holmes & Watson | Watson  |
| 2   | The quick brown fox jumps over the lazy dog. | dog.    |
| 3   | Hello World     | World   |
| 4   | GitHub Copilot  | Copilot |
| 5   | Programming is fun and challenging. | challenging. |


### Note:
Focuses on string splitting and element access.


## Exercise 12: Penguin Display - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Write a program that, given a number `n` from 1 to 9, displays `n` penguins each with a corresponding number from 1 to `n`. Each penguin is 5 rows high and 9 characters wide, with an empty column of spaces between adjacent penguins. An empty column after the last penguin is also permitted. Output should be by row, not "per penguin".

### Input:
- An integer `n` (1 ≤ n ≤ 9).

### Output:
- A display of `n` penguins, each numbered sequentially.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 4      |         |

### Output for Input Example 1

<pre>
   _~_        _~_        _~_        _~_
  (o o)      (o o)      (o o)      (o o)
 /  V  \    /  V  \    /  V  \    /  V  \
/(  1  )\  /(  2  )\  /(  3  )\  /(  4  )\
  ^^ ^^      ^^ ^^      ^^ ^^      ^^ ^^
</pre>

### Note:
The problem tests the ability to use loops and string manipulation to construct a multi-line pattern output.

This exercise challenges the programmer to not only manage multiple loops and conditional statements but also to handle string formatting and alignment carefully to ensure the penguins display correctly.


## Exercise 13: Extract Digits - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Write a program to extract all digits from a given string and form a new string from them.

### Input:
- A string that may contain any characters.

### Output:
- A new string consisting only of the digits extracted from the input string.

### Examples:

| No. | Inputs    | Outputs |
| --- | --------- | ------- |
| 1   | 3+3=6     | 336     |
| 2   | 2 * 3 = 6 | 236     |

### Note:
This exercise tests string manipulation, focusing on filtering characters.

## Exercise 14: Remove Extra Spaces - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given a string with several words separated by one or more spaces, remove all excess spaces including those at the beginning and end of the string.

### Input:
- A string containing up to 255 characters.

### Output:
- The string with all extra spaces removed.

### Examples:                             

| No. | Inputs                                                                                                        | Outputs                                                                                               |
| --- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 1   |    Beyond the green     swelling hills of the     Mittel Land rose mighty slopes of forest    up    to the lofty steeps of the Carpathians    themselves | Beyond the green swelling hills of the Mittel Land rose mighty slopes of forest up to the lofty steeps of the Carpathians themselves |
| 2   |    The quick brown fox jumps over the lazy dog     . | The quick brown fox jumps over the lazy dog. |
| 3   |    Hello , world!      | Hello, world! |
| 4   |    This is a test      | This is a test |

### Note:
The problem tests string trimming and space normalization.

## Exercise 15: Simple Expression Evaluator - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Evaluate a simple mathematical expression provided in the form 'A+B', 'A-B', or 'A*B', where A and B are integers from 0 to 1000000000.

### Input:
- A string representing a simple arithmetic expression.

### Output:
- The integer result of the expression.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 3*3    | 9       |
| 2   | 50-49  | 1       |
| 3   | 33+16  | 49      |

### Note:
This problem tests basic arithmetic operations and string parsing.

## Exercise 16: ASCII Range Printer - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given two characters, print all ASCII characters that lie between them inclusively.

### Input:
- Two characters, each on a separate line.

### Output:
- A string starting with the first and ending with the second input character, including all characters in between.

### Examples:

| No. | Inputs | Outputs    |
| --- | ------ | ---------- |
| 1   | A<br>F | ABCDEF     |
| 2   | 0<br>9 | 0123456789 |

### Note:
This exercise tests understanding of ASCII values and character ranges.

## Exercise 17: Count Words in a String - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given a string consisting of words separated by spaces, determine how many words are in the string.

### Input:
- A string.

### Output:
- The number of words in the string.

### Examples:

| No. | Inputs                                                                      | Outputs |
| --- | --------------------------------------------------------------------------- | ------- |
| 1   | Events happened very rapidly with Francis Morgan that late spring morning    | 11      |
| 2   | The quick brown fox jumps over the lazy dog                                  | 9       |
| 3   | Hello, world!                                                               | 2       |
| 4   | This is a test                                                              | 4       |

### Note:
Focuses on splitting strings and counting elements.

## Exercise 18: Multiply Digits in Sequence - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given a sequence of digits in the form p1*p2*...*pn, compute the product.

### Input:
- A string representing a sequence of digits separated by '*'.

### Output:
- The result of multiplying all the digits.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 2*5*7  | 70      |
| 2   | 3*4*6  | 72      |
| 3   | 1*9*8  | 72      |
| 4   | 2*3  | 6       |
| 5   | 4*5*6*7*8  | 6720      |
| 6   | 9*9*9*9*9*9*9  | 4782969      |


### Note:
Tests arithmetic operations on strings without using direct numeric operations.

## Exercise 19: First Decimal Digit - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given a positive real number, print the first digit to the right of the decimal point. Consider the case where the entered number is an integer.

### Input:
- A real number.

### Output:
- The first digit after the decimal point.

### Examples:

| No. | Inputs  | Outputs |
| --- | ------- | ------- |
| 1   | 1.79    | 7       |
| 2   | 100.89  | 8       |
| 3   | 6.045   | 0       |
| 4   | 3.14159 | 1       |
| 5   | 0.5     | 5       |

### Note:
This problem tests string manipulation and accessing specific character positions.

## Exercise 20: Sum of Single Digit Numbers - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Given a string of digit-only numbers without spaces, write a program to compute their sum.

### Input:
- A string of digits.

### Output:
- The sum of the digits.

### Examples:
| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1239   | 15      |
| 2   | 88     | 16      |
| 3   | 01     | 1       |
| 4   | 456    | 15      |
| 5   | 999    | 27      |

### Note:
Focuses on character iteration and integer conversion.

## Exercise 21: Convert Date Format - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Read a user-input string containing a date in the form mm/dd/yyyy and print the date in the format Month Day, Year.

### Input:
- A string representing a date.

### Output:
- The date in the format "Month Day, Year".

### Examples:

| No. | Inputs     | Outputs                |
| --- | ---------- | ---------------------- |
| 1   | 12/29/2022 | December 29, 2022      |
| 2   | 03/04/2025 | March 04, 2025         |
| 3   | 06/15/2030 | June 15, 2030          |
| 4   | 09/01/2023 | September 01, 2023     |

### Note:
Tests string manipulation and understanding of date formats.

## Exercise 22: Check Palindrome - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Enter a string. Remove all spaces from it and then determine if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

### Input:
- A string.

### Output:
- "Yes" if the string is a palindrome, "No" otherwise.

### Examples:

| No. | Inputs                                           | Outputs |
| --- | ------------------------------------------------ | ------- |
| 1   | 123          621                                 | No      |
| 2   | Never     odd   or        even                   | Yes     |
| 3   | A man, a plan, a canal, Panama                   | Yes     |
| 4   | Racecar                                         | Yes     |
| 5   | Hello world                                     | No      |

### Note:
Tests string manipulation and palindrome checking.

## Exercise 23: Convert to Morse Code - Medium 🔥 (Est. Time: 10-15 mins | Points: 20)

**Problem:** Write a program that converts a user-entered string into Morse code. Use an online Morse code table for reference. No restrictions on using dictionaries or lists.

### Input:
- A string.

### Output:
- The string translated into Morse code.

### Examples:

| No. | Inputs | Outputs                   |
| --- | ------ | ------------------------- |
| 1   | W      | .--                       |
| 2   | 9      | ----.                     |
| 3   | ,      | --..--                    |
| 4   | Python | .--.-.---....----.        |
| 5   | :)     | ---...-.--.-              |

### Note:
Focuses on string manipulation and applying encoding schemes.

## Exercise 24: Letter Case Frequency - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

**Problem:** Write a program to determine the percentage of uppercase and lowercase letters in a string. Ignore spaces and punctuation.

### Input:
- A string which may contain spaces and punctuation.

### Output:
- The percentage of lowercase letters followed by the percentage of uppercase letters in the string.

### Examples:

| No. | Inputs        | Outputs     |
| --- | ------------- | ----------- |
| 1   | Hello, Guido! | 80.00<br>20.00 |
| 2   | This is a Test | 81.82<br>18.18 |
| 3   | PYTHON123     | 0.00<br>100.09 |
| 4   | AbCdEfG       | 50.00<br>50.00 |
| 5   | 1234567890    | 0.00<br>0.00 |

### Note:
This exercise tests string analysis and percentage calculation skills.

## Exercise 25: Windows Path Decomposition - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

**Problem:** Given a Windows file path, decompose it into its constituent parts without using any modules.

### Input:
- A string representing a Windows file path.

### Output:
- The drive letter and each directory name as separate lines.

### Examples:

| No. | Inputs               | Outputs     |
| --- | -------------------- | ----------- |
| 1   | C:\\Python36\\python.exe | C:<br>Python36<br>python.exe |
| 2   | D:\\Documents\\file.txt | D:<br>Documents<br>file.txt |
| 3   | E:\\Programs\\program.exe | E:<br>Programs<br>program.exe |

### Note:
Tests string splitting and manipulation skills with specific focus on handling escape characters.

## Exercise 26: Multiplication Table - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

**Problem:** Print a part of the multiplication table for numbers in the range [a, b] across [c, d].

### Input:
- Four integers a, b, c, and d defining the ranges.

### Output:
- A formatted multiplication table.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1<br>4<br>2<br>5 | Output 1         |

### Output for Input Example 1

<pre>	2	3	4	5
1	2	3	4	5
2	4	6	8	10
3	6	9	12	15
4	8	12	16	20</pre>



### Note:
Focuses on loops for generating and formatting a matrix-like output.

## Exercise 27: Run-Length Encoding - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

**Problem:** Encode a string by replacing groups of identical characters with the character followed by its count.

### Input:
- A string.

### Output:
- The encoded string.

### Examples:

| No. | Inputs      | Outputs   |
| --- | ----------- | --------- |
| 1   | aaaabbbcaa  | a4b3c1a2  |
| 2   | abc         | a1b1c1    |
| 3   | Hello       | H1e1l2o1  |
| 4   | abcdabcd    | a1b1c1d1a1b1c1d1 |
| 5   | xyzxyzxyz   | x1y1z1x1y1z1x1y1z1 |

### Note:
Tests string iteration and conditional counting for encoding patterns.

## Exercise 28: Word Count in a String - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

**Problem:** Count the number of words in a string, where a word is a sequence of consecutive English letters.

### Input:
- A string.

### Output:
- The number of words in the string.

### Examples:

| No. | Inputs                                                         | Outputs |
| --- | -------------------------------------------------------------- | ------- |
| 1   | Do you play any sports? Yes, I like to play basketball.        | 11      |
| 2   | How many siblings do you have? I have two sisters and one brother. | 13      |
| 3   | What is your favorite color? My favorite color is blue.        | 10       |

### Note:
Challenges string processing and word counting without using lists.

## Exercise 29: Caesar Cipher - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

**Problem:** Encrypt a string using the Caesar cipher, shifting letters by a specified number of places in the alphabet.

### Input:
- An integer for the shift amount and a string to encrypt.

### Output:
- The encrypted string.

### Examples:


| No. | Inputs         | Outputs |
| --- | -------------- | ------- |
| 1   | 1<br>abc       | bcd     |
| 2   | 26<br>abc      | abc     |
| 3   | 1<br>Python    | Qzuipo  |
| 4   | 3<br>Python    | Sbwkrq  |


### Note:
Tests understanding of character manipulation within strings and conditional wrapping for alphabets.

## Exercise 30: Roman to Integer Conversion - Hard 🥵 (Est. Time: 15-20 mins | Points: 30)

**Problem:** Convert a Roman numeral to an integer.

### Input:
- A string representing a Roman numeral.

### Output:
- The integer value of the Roman numeral.

### Examples:

| No. | Inputs   | Outputs |
| --- | -------- | ------- |
| 1   | MMMCMXCIX | 3999    |
| 2   | IV        | 4       |
| 3   | XXI       | 21      |
| 4   | XLV       | 45      |
| 5   | CXXV      | 125     |

### Note:
Challenges understanding and implementing the conversion of Roman numerals to integers, focusing on string processing and pattern recognition.




# Problems in Order of Difficulty According to ChatGPT

The exercises provided range from understanding conditional statements to implementing complex branching logic. Here's a summary of the exercises ordered by difficulty, starting with the easiest and moving to more challenging problems.

## Easy 😊
Total: 11

## Medium 🔥
Total: 12

## Hard 🥵
Total: 7

Each exercise is designed to challenge different aspects of problem-solving, from simple arithmetic to complex logical reasoning. The estimated completion time for the exercises ranges from 5 minutes for the simplest tasks to 25 minutes for the most complex ones. This gives an average expected time of approximately 10-15 minutes per exercise, depending on the student's prior knowledge and experience.


# Checking Your Score with Autograder 📝

GitHub Classroom's autograder provides immediate feedback on your exercises. Each exercise is worth points based on its complexity, with a total of `90` points available across all exercises. 

When you commit and push your solution, GitHub Actions will run tests on your code. If all tests for an exercise pass, you will be awarded the full points for that exercise. If some tests fail, partial points may be awarded. 

The workflow will run all tests, even if some fail. The total score will be shown in the workflow output as `points scored/total points available`. For example, if you see `10/90`, it means you've successfully completed the first problem worth `10` points.

Please note that the workflow will show as failed if any test fails, even if you've successfully solved some problems. Look for the points tally in the output to see your score.

Remember, practice makes perfect! If you don't pass all tests the first time, review your code, make improvements, and try again. You can push new changes as many times as you need.

# Running Your Code and Tests Locally 🖥️

To run your code and tests locally, you can use the following commands:

1. Run the code:
```bash
python exercises/exercise_1.py
```

2. Run the tests:

To run the tests for an exercise, you'll use the pytest framework. First, make sure you have pytest installed: 

```bash
pip install pytest
```

Then, you can run the tests for a specific exercise using the following command:

```bash
python -m unittest tests/test_exercise_1.py
```

And for more beautiful output, you can use:

```bash
pytest --color=yes -vv tests/test_exercise_1.py
```

or to run only failed test from a specific file:

```bash
pytest --color=yes --failed-first -x tests/test_exercise_1.py
```

Replace `exercise_1` with the exercise you're working on (e.g., `exercise_2`, `exercise_3`, etc.) and `test_exercise_1` with the corresponding test file.





