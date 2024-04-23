# Examples 👨🏼‍💻

Here are some examples to get you started.

<details open>
<summary><b>Covered topics</b></summary>

| Topic Covered                                           | Code with explanations                            |
| ------------------------------------------------------- | ------------------------------------------------- |
| Repeat Last Two Characters                              | [Detailed code](./example_1.py)                   |
| Reverse Digits                                          | [Detailed code](./example_2.py)                   |
| Check Start of String                                   | [Detailed code](./example_3.py)                   |
| Number reversal                                         | [Detailed code](./example_4.py)                   |
| Palindrome String                                       | [Detailed code](./example_5.py)                   |
| Is Digit Check                                          | [Detailed code](./example_6.py)                   |
| Digits and Characters                                   | [Detailed code](./example_7.py)                   |
| The first word in a string                              | [Detailed code](./example_8.py)                   |
| Access Code Calculation                                 | [Detailed code](./example_9.py)                   |
| ASCII Characters                                        | [Detailed code](./example_10.py)                  |
| Count Words in a String                                 | [Detailed code](./example_11.py)                  |
| String Len                                              | [Detailed code](./example_12.py)                  |
| Digits and Characters Count                             | [Detailed code](./example_13.py)                  |
| Vowel and Consonant Check                               | [Detailed code](./example_14.py)                  |
| Sum of Sequence Elements Calculation                    | [Detailed code](./example_15.py)                  |
| Uppercase, Lowercase, and Space Count                   | [Detailed code](./example_16.py)                  |
| Remove Duplicate Characters                             | [Detailed code](./example_17.py)                  |
| Find and Replace Substring                              | [Detailed code](./example_18.py)                  |
| Longest Sequence of Zeros                               | [Detailed code](./example_19.py)                  |
| Can Construct                                           | [Detailed code](./example_20.py)                  |
| Check Bracket Balance                                   | [Detailed code](./example_21.py)                  |
| Evaluate Expression                                     | [Detailed code](./example_22.py)                  |
| Count String Occurrences                                | [Detailed code](./example_23py)                   |
| Format Number with Commas                               | [Detailed code](./example_24.py)                  |
| Find and Replace Substring                              | [Detailed code](./example_25.py)                  |
| Find Shortest Word and Its Length                       | [Detailed code](./example_26.py)                  | 
| Run-Length Encoding                                     | [Detailed code](./example_27.py)                  |
| Evaluate Simple Arithmetic Expression                   | [Detailed code](./example_28.py)                  |
| Find Most Frequent Letters                              | [Detailed code](./example_29.py)                  |
| Validate IP Address                                     | [Detailed code](./example_30.py)                  |

</details>

### Example 1: Repeat Last Two Characters

**Problem:** Write a program that displays a string of 5 copies of the last two characters of a user-entered string (the length of the entered string must be at least 2).

| No. | Inputs | Outputs         |
| --- | ------ | --------------- |
| 1   | emu    | mumumumumu      |
| 2   | lion   | ononononon      |
| 3   | tiger  | ererererer      |
| 4  | snake  | kekekekeke      |


 - Repeat Last Two Characters

**Problem:** Print 5 copies of the last two characters from a user-entered string on the screen (where the length of the entered string is at least 2).

<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

if len(input_string) >= 2:
    last_two = input_string[-2:]
    print(last_two * 5)
```
</details>

### Example 2: Reverse Digits

**Problem:** Given a natural number, find the number obtained by reading its digits from right to left.

| No. | Inputs   | Outputs   |
| --- | -------- | --------- |
| 1   | 98       | 89        |
| 2   | 10010010 | 01001001  |
| 3   | 1235     | 5321      |
| 4   | 1        | 1         |
| 5   | 0        | 0         |

**Problem:** Compute the number obtained by reversing the digits of a given natural number.

<details open>
<summary><b>Python Solution</b></summary>

```python
input_number = input("Enter a natural number: ")

reversed_number = input_number[::-1]

print(reversed_number)
```
</details>

### Example 3: Check Start of String

**Problem:** The user enters a string and a set of characters. Write a program that checks if the string starts with the given characters.

| No. | Inputs                      | Outputs |
| --- | --------------------------- | ------- |
| 1   | wireless router<br> route     | False   |
| 2   | python programming<br> py     | True    |
| 3   | 12345<br> 123                 | True    |
| 4   | 12345<br> 234                 | False   |
| 5   | 12345<br> 12345               | True    |

**Problem:** Verify whether a user-input string begins with the specified characters.

<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter the string: ")
prefix = input("Enter the prefix: ")

starts_with_prefix = input_string.startswith(prefix)

print(starts_with_prefix)
```
</details>



## Example 4:  Number reversal

**Problem:** Given a natural number `n`. Find a number obtained by permuting its first and last digits. Consider the case of entering a single-digit number.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 1467   | 7461    |
| 2   | 5      | 5       |
| 3   | 11     | 11      |
| 4   | 12     | 21      |
| 5  | 1      | 1       |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = input("Enter the number: ")

if len(n) > 2:
    reversed_number = n[-1] + n[1:-1] + n[0]
elif len(2) == 2:
    reversed_number = n[-1] + n[0]
else:
    reversed_number = n

print(reversed_number)
```
</details>



## Example 5: Palindrome String

**Problem:** A user enters a string which can contain digits and other characters. Determine if the line is a palindrome, i.e., it reads the same from left to right and from right to left. Do not consider the case of letters. Examples of palindrome strings: racecar, 10201, Ada, Never odd or even.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | Ada    | True    |
| 2   | Able was I ere I saw Elba | True    |
| 3   | 10501  | True    |
| 4   | Origin | False   |
| 5   | 12321  | True    |

<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

input_string = input_string.replace(" ", "").lower()

is_palindrome = input_string == input_string[::-1]

print(is_palindrome)
```
</details>


## Example 6: Is Digit Check


**Problem:**  For the entered symbol, check if it is a digit. You cannot use string functions to solve the problem. The program should print the word Yes if the character is a digit, or the word No.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 7      | Yes     |
| 2   | A      | No      |
| 3   | 0      | Yes     |
| 4   | 9      | Yes     |
| 5   | h      | No      |


<details open>
<summary><b>Python Solution</b></summary>

```python
# Solution 1

symbol = input("Enter a symbol: ")


if "0" <= symbol <= "9":
    print("Yes")
else:
    print("No")

# Solution 2

digits = "0123456789"

if symbol in digits:
    print("Yes")
else:
    print("No")
```
</details>



## Example 7: Digits and Characters

**Problem:** A user enters a string in which digits and other characters alternate. The string does not contain digits at the beginning and end. Write a program that prints all the characters of the entered string in the same order, but without digits.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | H1e2l3l4o5w6o7r8l9d | Helloworld |
| 2   | i1m3p4o9r0t4 6t7h8i9s | import this |
| 3   | 1H2e3l4l5o6 7W8o9r0l1d | Hello World |
| 4   | 1a2b3c4d5e6f7g8h9i0j | abcdefghij |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

result = ""

for char in input_string:
    if not char.isdigit():
        result += char

print(result)
```
</details>

## Example 8: The first word in a string

**Problem:** Write a program that outputs the first word in a string. A word is a sequence of non-space characters bounded by spaces or the ends of a string. The input string contains an arbitrary sequence of characters. The program should print the first word of this string. Need to consider the case when the string has just one word

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | Stranger Things | Stranger |
| 2   | The Mandalorian | The |
| 3   | The Witcher | The |

<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

first_space_index = input_string.find(" ")

if first_space_index != -1:
    first_word = input_string[:first_space_index]
else:
    first_word = input_string

print(first_word)
```
</details>


## Example 9: Access Code Calculation

**Problem:** To access their account on a social network site, a user entered their login and password. Since two-factor authentication was enabled, they received a message with a string of numbers and information on how to get the access code. The message read: "Each digit greater than 5 must be divided by 2 and then all even numbers must be removed from the resulting sequence of digits." What code should the user enter for successful authorization? Write a program that takes a string of numbers from the message as input and prints the correct access code.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 5763   | 33      |
| 2   | 1977   | 33      |
| 3   | 12345  | 1       |
| 4   | 987654 | 33      |
| 5   | 123456 | 1       |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

result = ""

for char in input_string:
    if char.isdigit() and int(char) > 5:
        result += str(int(char) // 2)
    elif char.isdigit() and int(char) % 2 != 0:
        result += char

print(result)
```
</details>


## Example 10:  ASCII Characters

**Problem:** Print all ASCII characters with codes from `n` (n > 32) to `m` (m < 127) and their codes in the following format: "character code".

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 101<br>106 | e 101<br>f 102<br>g 103<br>h 104<br>i 105<br>j 106 |
| 2   | 65<br>70   | A 65<br>B 66<br>C 67<br>D 68<br>E 69<br>F 70 |
| 3   | 33<br>40   | ! 33<br>" 34<br># 35<br>$ 36<br>% 37<br>& 38<br>' 39 |


<details open>
<summary><b>Python Solution</b></summary>

```python
start = int(input("Enter the first number: "))
end = int(input("Enter the second number: "))

for i in range(start, end + 1):
    print(chr(i), i)
```
</details>


## Example 11: Count Words in a String


**Problem:** Given a string of words separated by spaces. Determine the number of words in the string.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | Events happened very rapidly with Francis Morgan that late spring morning | 11 |
| 2   | The quick brown fox jumps over the lazy dog | 9 |
| 3   | The cat in the hat | 5 |
| 4   | The quick brown fox jumps over the lazy dog | 9 |
| 5   | The cat in the hat | 5 |


<details open>
<summary><b>Python Solution</b></summary>
    
```python
input_string = input("Enter a string: ")

if len(input_string) == 0:
    print(0)
else:
    word_count = 1
    for char in input_string.strip():
        if char == " ":
            word_count += 1

    print(word_count)
```
</details>


## Example 12: String Len

**Problem:** Write a program to calculate the length of a string without using the `len()` function. 

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | pythonguide.pp.ua | 17 |
| 2   | python | 6 |
| 3   | guide | 5 |
| 4   | pp.ua | 5 |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

length = 0

for _ in input_string:
    length += 1

print(length)
```
</details>


## Example 13: Digits and Characters Count

**Problem:** Write a program that receives a string and calculates the number of digits and letters in it.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | Andromeda, M 31, NGC 224 | Letters 13<br>Digits 5 |
| 2   | Python 3.9 | Letters 6<br>Digits 2 |
| 3   | 12345 | Letters 0<br>Digits 5 |
| 4   | 1a2b3c4d5e | Letters 5<br>Digits 5 |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

letter_count = 0
digit_count = 0

for char in input_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print(f"Letters {letter_count}")
print(f"Digits {digit_count}")
```
</details>


## Example 14: Vowel and Consonant Check

**Problem:** Write a program to check if the entered letter is a vowel or a consonant.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | F      | F is a consonant |
| 2   | e      | e is a vowel |
| 3   | a      | a is a vowel |
| 4   | b      | b is a consonant |
| 5   | c      | c is a consonant |


<details open>
<summary><b>Python Solution</b></summary>

```python
letter = input("Enter a letter: ")

if letter.lower() in "aeiou":
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant")
```
</details>

## Example 15: Sum of Sequence Elements Calculation

**Problem:** User defines a number `n` such as `n >= 2`. Calculate the sum of the following sequence: `1 x 2 + 2 x 3 + ... + (n - 1) x n`. Print the result in the format shown in the output data.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 2      | 1*2=2   |
| 2   | 4      | 1*2+2*3+3*4=20 |
| 3   | 5      | 1*2+2*3+3*4+4*5=35 |
| 4   | 6      | 1*2+2*3+3*4+4*5+5*6=56 |
| 5   | 7      | 1*2+2*3+3*4+4*5+5*6+6*7=84 |

<details open>
<summary><b>Python Solution</b></summary>

```python
n = int(input("Enter the number: "))

total = 0
output = ""

if n >= 2:
    for i in range(1, n):
        total += i * (i + 1)
        output += f"{i}*{i + 1}+"

    output = output[:-1]
    output += f"={total}"
    print(output)
else:
    print("Invalid input")
```
</details>

**Note** We assign the value `1` to the variable `factorial` because the factorial of `0` is `1`. Then, we use a `for` loop to iterate through the numbers from `1` to `n` and multiply them to the `factorial` variable. Also, we can't assign it to `0` because the multiplication of any number by `0` is `0`.



## Example 16: Uppercase, Lowercase, and Space Count

**Problem:** Write a program that reads a string entered by the user and determines the number of uppercase letters, lowercase letters, and spaces in it.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | By Red Flower Bagheera meant fire, only no creature in the jungle will call fire by its proper name. | Upper 4<br>Lower 76<br>Spaces 18 |
| 2   | The quick brown fox jumps over the lazy dog | Upper 3<br>Lower 32<br>Spaces 8 |
| 3   | The cat in the hat | Upper 1<br>Lower 12<br>Spaces 4 |
| 4   | The quick brown fox jumps over the lazy dog | Upper 3<br>Lower 32<br>Spaces 8 |
| 5   | The cat in the hat | Upper 1<br>Lower 12<br>Spaces 4 |

<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

upper_count = 0
lower_count = 0
space_count = 0

for char in input_string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isspace():
        space_count += 1

print(f"Upper {upper_count}")
```
</details>


## Example 17: Remove Duplicate Characters

**Problem:** Enter a string. Remove all duplicate characters and spaces from it.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | aa     | a       |
| 2   | a a b b c dd e | abcde |
| 3   | 12345  | 12345  |
| 4   | 123 123  | 123   |
| 5   | 1 2 3 4 5  | 12345 |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

unique_chars = ""

for char in input_string:
    if char not in unique_chars and not char.isspace():
        unique_chars += char

print(unique_chars)


```
</details>


## Example 18: Find and Replace Substring

**Problem:** Given a string, find a specified substring and replace it with a new one. The user enters the string, the substring to replace, and the new string. Consider the case of replacing all substrings. Also, consider the case when the substring to be replaced is not present (print is impossible).

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 12 45 32 567 32 109<br>32<br>0 | 12 45 0 567 0 109 |
| 2   | 12 45 32 567 32 109<br>33<br>-1 | is impossible |
| 3   | abc abc abc abc<br>abc<br>xyz | xyz xyz xyz xyz |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

substring = input("Enter the substring to replace: ")

new_substring = input("Enter the new substring: ")

# Solution 1

if substring in input_string:
    # Without using replace 
    result = ""
    i = 0
    while i < len(input_string) - len(substring) + 1:
        if input_string[i:i + len(substring)] == substring:
            result += new_substring
            i += len(substring)
        else:
            result += input_string[i]
            i += 1

    print(result)
else:
    print("is impossible")

# Solution 2

if substring in input_string:
    result = input_string.replace(substring, new_substring)
    print(result)
else:
    print("is impossible")
```

</details>

## Example 19: Longest Sequence of Zeros

**Problem:** Given a string of zeros and ones, write a program to find the longest continuous sequence of zeros in the string.

| No. | Inputs         | Outputs |
| --- | -------------- | ------- |
| 1   | 1001           | 2       |
| 2   | 100001001010   | 4       |
| 3   | 1000001        | 5       |

**Problem:** Determine the longest unbroken chain of zeros within a binary string.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Take input for the binary string
binary_string = input("Enter the binary string: ")

# Initialize variables to track the longest zero sequence and current zero count
longest_sequence = 0
current_count = 0

# Iterate over each character in the string
for char in binary_string:
    if char == '0':
        current_count += 1
    else:
        if current_count > longest_sequence:
            longest_sequence = current_count
        current_count = 0

# Check the last sequence in case the string ends with '0'
if current_count > longest_sequence:
    longest_sequence = current_count

# Print the longest sequence of zeros
print(longest_sequence)
```
</details>



## Example 20: Can Construct

**Problem:** Given two words, write a program that determines whether word B can be constructed from the letters of word A, taking into account the case sensitivity of the letters.

| No. | Inputs                | Outputs |
| --- | --------------------- | ------- |
| 1   | Python<br>not         | Yes     |
| 2   | Ruby<br>Buy           | No      |

**Problem:** Check if it is possible to construct word B using the letters from word A, considering letter case sensitivity.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Take input for word A
word_a = input("Enter word A: ")
# Take input for word B
word_b = input("Enter word B: ")

# Check if word B can be constructed from word A
can_construct = True

for char_b in word_b:
    char_b_count = 0
    char_a_count = 0
    for char in word_b:
        if char == char_b:
            char_b_count += 1
    for char in word_a:
        if char == char_b:
            char_a_count += 1
    if char_b_count > char_a_count:
        can_construct = False
        break

# Output result
print("Yes" if can_construct else "No")
```
</details>

## Example 21: Check Bracket Balance

**Problem:** Given a sequence of characters of length n (n ≥ 1), verify the balance of parentheses in the expression (each opening parenthesis must have its corresponding closing parenthesis). For example, the input `(()) ()` should result in `True`, indicating correct placement, while the input `((())` should result in `False`, indicating incorrect placement. The program should be capable of checking the balance of parentheses in arithmetic expressions, text, etc.

| No. | Inputs                              | Outputs       |
| --- | ----------------------------------- | ------------- |
| 1   | (3y + 21)(12 - (x + 5))             | True          |
| 2   | (61x + 15(y + 2)                    | False         |

**Problem:** Write a program to check the balance of parentheses in various expressions.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Take input for the expression
expression = input("Enter the expression: ")

# Initialize counter for open parentheses
balance = 0
is_balanced = True

# Iterate through each character in the expression
for char in expression:
    if char == '(':
        balance += 1
    elif char == ')':
        balance -= 1
    # If at any point there are more closing parentheses, it's unbalanced
    if balance < 0:
        is_balanced = False
        break

# If there are open parentheses left unmatched, it's unbalanced
if balance != 0:
    is_balanced = False

# Output result
print("True" if is_balanced else "False")
```

</details>

## Example 22: Evaluate Expression

**Problem:** Given a string that consists of n digits (i.e., single-digit numbers), separated by n-1 operation signs which can be either '+' or '-', calculate the value of this expression. The program should print the result of evaluating this expression.

| No. | Inputs    | Outputs |
| --- | --------- | ------- |
| 1   | 5-3+1     | 3       |
| 2   | 6+3-2     | 7       |

**Problem:** Write a program to evaluate expressions consisting of single-digit numbers separated by '+' or '-' signs.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Take input for the expression
expression = input("Enter the expression: ")

# Initialize the result with the first number (assumes expression starts with a number)
result = int(expression[0])

# Loop through the expression starting from the first operator
i = 1
while i < len(expression):
    operator = expression[i]
    digit = int(expression[i+1])
    
    if operator == '+':
        result += digit
    elif operator == '-':
        result -= digit
    
    i += 2  # Move to the next operator

# Print the final result
print(result)
```
</details>



## Example 23: Count String Occurrences

**Problem:** Two strings A and B, consisting of lowercase English letters, are given as input. Output the number of occurrences of string B in string A.

| No. | Inputs                    | Outputs |
| --- | ------------------------- | ------- |
| 1   | aaaa<br>a                 | 4       |
| 2   | ababada<br>abc            | 0       |
| 3   | abababa<br>aba            | 3       |

**Problem:** Write a program that prints the number of times string B occurs in string A using two different approaches.

<details open>
<summary><b>Solution One</b></summary>

```python
# Input string A
a = input("Enter string A: ")
# Input string B
b = input("Enter string B: ")

count = 0
# Use a loop to manually check for occurrences
for i in range(len(a) - len(b) + 1):  # Only go up to where B can fully fit in A
    if a[i:i+len(b)] == b:  # Check if the substring of A equals B
        count += 1

# Print the number of occurrences
print(count)
```
</details>

<details open>
<summary><b>Solution Two</b></summary>
 
```python
# Input string A
a = input("Enter string A: ")
# Input string B
b = input("Enter string B: ")

# Initialize the count and the starting index
count = 0
start = 0

# Loop to find occurrences of string B in string A
while True:
    start = a.find(b, start)  # Find the next occurrence of B starting from index 'start'
    if start == -1:  # No more occurrences found
        break
    count += 1
    start += 1  # Move start index to the next character after the current match

# Print the number of occurrences
print(count)
```
</details>

## Example 24: Format Number with Commas

**Problem:** The user enters a string of digits without spaces. Write a program that "breaks" this number into groups of three digits from right to left using commas. If the number contains fewer than three digits, it should be displayed without changes.

| No. | Inputs   | Outputs     |
| --- | -------- | ----------- |
| 1   | 4567     | 4,567       |
| 2   | 123      | 123         |
| 3   | 2348906  | 2,348,906   |

**Problem:** Write a program that formats a string of digits by grouping every three digits with commas from right to left.

<details open>
<summary><b>Python Solution</b></summary>

```python
# Input string of digits
number = input("Enter a string of digits: ")

# Start from the end and insert commas every three digits
formatted_number = ''
count = 0

# Reverse iterate over the number string
for i in range(len(number) - 1, -1, -1):
    formatted_number = number[i] + formatted_number
    count += 1
    if count == 3 and i != 0:  # Avoid adding a comma at the start
        formatted_number = ',' + formatted_number
        count = 0

# Print the formatted number
print(formatted_number)
```

</details>


## Example 25: Find and Replace Substring

**Problem:** Write a program that decrypts an input text using the method described.

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | Njzxwxgd Bpihjbdid, rgtpidg du iwt Gjqn egdvgpbbxcv apcvjpvt. | Yukihiro Matsumoto, creator of the Ruby programming language. |
| 2   | Wklv, qmzv, wklv, qmzv, wklv, qmzv. | This, that, this, that, this, that. |


<details open>
<summary><b>Python Solution</b></summary>

```python
# Input encrypted text
text = input("Enter encrypted text: ")

# Determine the number of letters 'k' in the longest word
k = 0
current_length = 0
max_length = 0

for char in text:
    if char.isalpha():
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
        current_length = 0

if current_length > max_length:
    max_length = current_length

k = max_length

# Decrypt the text directly in the loop
decrypted_text = ''
for char in text:
    if 'a' <= char <= 'z':  # Lowercase letters
        new_pos = (ord(char) - ord('a') - k) % 26 + ord('a')
        decrypted_text += chr(new_pos)
    elif 'A' <= char <= 'Z':  # Uppercase letters
        new_pos = (ord(char) - ord('A') - k) % 26 + ord('A')
        decrypted_text += chr(new_pos)
    else:
        decrypted_text += char  # Non-alphabet characters remain unchanged

# Output the decrypted text
print(decrypted_text)
```

</details>

## Example 26: Find Shortest Word and Its Length

**Problem:** In the given string, find the shortest word, and display this word along with its length in characters. Words may be separated by spaces, multiple spaces, punctuation marks, digits, etc. If there are multiple shortest words, only display the first one. The string of words is guaranteed to end with a period. Write a program that finds and prints the shortest word in the input text along with its length using only string operations.


| No. | Inputs                         | Outputs  |
| --- | ------------------------------ | -------- |
| 1   | He lives in house number 4.    | He 2     |
| 2   | Now is better than never.      | is 2     |
| 3   | Tom Tells the Truth.           | Tom 3    |
| 4   | The quick brown fox jumps over the lazy dog. | The 3 |
| 5   | I am a programmer.             | I 1      |


<details open>
<summary><b>Python Solution</b></summary>

```python
sentence = input("Enter a sentence ending with a period: ")

sentence = sentence[:-1]

shortest_word = ''
min_length = len(sentence)
current_word = ''

for char in sentence:

    if char.isalpha():
        current_word += char
    else:

        if current_word and (len(current_word) < min_length):
            shortest_word = current_word
            min_length = len(current_word)

        current_word = ''

if current_word and (len(current_word) < min_length):
    shortest_word = current_word
    min_length = len(current_word)

print(f'{shortest_word} {min_length}')
```
</details>


## Example 27: Run-Length Encoding

**Problem:** Implement a simple version of the run-length encoding (RLE) data compression algorithm. The algorithm receives a string containing English alphabet characters. This string is split into groups of consecutive identical characters ("runs"). Each run is characterized by the character and the number of repetitions. This information is then encoded: the length of the run of repeated characters is written first, followed by the character itself. If a run consists of only one character, the count is omitted. Write a program that outputs a run-length encoding of the input text.

| No. | Inputs                  | Outputs        |
| --- | ----------------------- | -------------- |
| 1   | aaabccccCCaB            | 3ab4c2CaB      |
| 2   | aabcccddffffffffff      | 2ab3c2d10f     |
| 3   | xyz                     | xyz            |
| 4   | pppppppppppppppp        | 16p            |
| 5   | AaAaAaAa                | 1A1a1A1a1A1a   |


<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

encoded_string = ""

count = 1
previous_char = input_string[0]

for char in input_string[1:]:
    if char == previous_char:
        count += 1
    else:
        if count > 1:
            encoded_string += str(count)
        encoded_string += previous_char
        previous_char = char
        count = 1

if count > 1:
    encoded_string += str(count)
encoded_string += previous_char

print(encoded_string)

```
</details>

## Example 28: Evaluate Simple Arithmetic Expression

**Problem:** Given a string containing one or more integers between 0 and 1,000,000,000, separated by '+' or '-' signs, calculate the value of this expression. Write a program that calculates and outputs the result of evaluating these arithmetic expressions.

| No. | Inputs       | Outputs |
| --- | ------------ | ------- |
| No. | Expression    | Result  |
| --- | ------------- | ------- |
| 1   | 12-5+3       | 10      |
| 2   | 26-14+2-1    | 13      |
| 3   | 7-0+3        | 10      |
| 4   | 100+200-50   | 250     |
| 5   | 10-5-2+8     | 11      |

<details open>
<summary><b>Python Solution</b></summary>

```python
expression = input("Enter the expression: ")

result = 0

# Initialize the first number
number = 0

# Initialize the sign to positive
sign = 1

for char in expression:
    if char.isdigit():
        number = number * 10 + int(char)
    else:
        result += sign * number
        number = 0
        if char == '+':
            sign = 1
        elif char == '-':
            sign = -1

result += sign * number

```
</details>





## Example 29: Find Most Frequent Letters

**Problem:** Given a string which may include spaces, determine which English alphabet letter(s) appear most frequently. Upper and lower case letters should be treated as the same, and non-letter characters are ignored. The program should output on the first line all letters that appear most frequently in the given string, in uppercase and alphabetical order without spaces. On the second line, output the number of times these letters appear in the string. The string must be processed in one pass without nested loops. Write a program to find and print the most frequent letters in the text.

| No. | Inputs                                                              | Outputs   |
| --- | ------------------------------------------------------------------- | --------- |
| 1   | Project Gutenberg EBook of The jungle book, by Rudyard Kipling      | EO<br>6   |
| 2   | Hello World                                                         | L<br>3    |
| 3   | GitHub Copilot is awesome                                           | O<br>3    |
| 4   | This is a test string                                               | I<br>3    |
| 5   | The quick brown fox jumps over the lazy dog                         | O<br>4    |
| 6   | The quick brown fox jumps over the lazy dog and the cat             | OTC<br>5  |

<details open>
<summary><b>Python Solution</b></summary>

```python
input_string = input("Enter a string: ")

# Initialize a string to store the most frequent letters
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Initialize a string to store the count of each letter
letter_count = ""

for letter in letters:
    current_letter_counter = 0
    for char in input_string.upper():
        if char.upper() == letter:
            current_letter_counter += 1
    letter_count += str(current_letter_counter)

max_frequency = 0

for count in letter_count:
    if int(count) > max_frequency:
        max_frequency = int(count)

for i in range(len(letters)):
    if int(letter_count[i]) == max_frequency:
        print(letters[i], end='')
print()
print(max_frequency)
```
</details>




## Example 30: Validate IP Address

**Problem:** Determine if a given string is a valid IP address. An IP address is a four-byte code typically represented as four numbers separated by dots, where each number ranges from 0 to 255. The program should output "Yes" if the string is a valid IP address format and "No" otherwise.

| No. | Inputs          | Outputs |
| --- | --------------- | ------- |
| 1   | C.E.R.N         | No      |
| 2   | 192.168.0.200   | Yes     |
| 3   | 256.0.0.255     | No      |
| 4   | 10.0.0.1        | Yes     |
| 5   | 172.16.0.0      | Yes     |
| 6   | 192.168.1.1     | Yes     |

<details open>
<summary><b>Python Solution</b></summary>

```python
# Take input for the IP address
ip = input("Enter an IP address: ")

part = ''
dot_count = 0
valid = True
part_count = 0

# Iterate over each character in the IP address
for i in range(len(ip)):
    char = ip[i]
    if char.isdigit():
        part += char  # Build the part string
    elif char == '.':
        if part == '' or int(part) > 255 or i == 0 or (i > 0 and not ip[i-1].isdigit()):
            valid = False
            break
        part_count += 1
        part = ''  # Reset part on dot
        dot_count += 1
    else:
        valid = False
        break

# Check the last part after the last dot or if no dots were found
if valid and part != '' and int(part) <= 255:
    part_count += 1
else:
    valid = False

# Must have exactly four parts and three dots to be valid
if part_count != 4 or dot_count != 3:
    valid = False

# Print the result for each IP
print("Yes" if valid else "No")
```
</details>




**Notes:** All the examples above are solved using Python. You can find the solutions in the [examples](./examples) folder. Covered with explanations and comments, these examples will help you understand the practical implementation of the concepts covered in this module. Python tests are also included to verify the correctness of the solutions.
