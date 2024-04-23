
# ## Exercise 3: Add Twos to Number - Easy 😊 (Est. Time: 5 mins | Points: 10)

# **Problem:** Given a natural number, find the number that results from appending the digit '2' to both the beginning and the end of the input number.

# ### Input:
# - A natural number.

# ### Output:
# - The number formed by appending '2' to both the beginning and end of the input number.

# ### Examples:

# | No. | Inputs | Outputs |
# | --- | ------ | ------- |
# | 1   | 45     | 2452    |
# | 2   | 1      | 212     |
# | 3   | 0      | 202     |
# | 4   | 999    | 29992   |
# | 5   | 1234   | 212342  |

# Prompt the user to enter a number
number = input("Enter a number: ")

# Append the number to itself
result = f"2{number}2"

# Output
print(result)
