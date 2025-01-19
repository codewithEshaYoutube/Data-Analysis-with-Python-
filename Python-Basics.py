
### 1. **Introduction to Python**

```python
# Python is a high-level, interpreted programming language that is easy to learn and great for data analysis.
# It allows developers to work quickly and efficiently.

# Why Python for Data Analysis?
# Python has powerful libraries like Pandas, NumPy, and Matplotlib which are specifically designed for data analysis.

# Installing Python and Setting Up:
# You can install Python and set up an environment using Anaconda, or use Jupyter Notebooks, PyCharm, or VS Code.
```

### 2. **Basic Python Syntax**

```python
# Hello World Program
print("Hello, World!")  # Output: Hello, World!

# Single-line Comment
# This is a single-line comment

# Multi-line Comment
"""
This is a multi-line comment
It spans across multiple lines.
"""

# Indentation Example
if True:
    print("This will be printed because indentation defines code block.")
```

### 3. **Variables and Data Types**

```python
# Variables
x = 10  # Integer
name = "Esha"  # String

# Data Types
integer_var = 10  # int
float_var = 10.5  # float
string_var = "Esha"  # str
boolean_var = True  # bool

# Type Conversion
x_as_string = str(x)  # Convert integer to string
x_as_float = float(x)  # Convert integer to float
```

### 4. **Basic Operators**

```python
# Arithmetic Operators
addition = 5 + 3  # Output: 8
subtraction = 5 - 3  # Output: 2
multiplication = 5 * 3  # Output: 15
division = 5 / 3  # Output: 1.6667 (float)
integer_division = 5 // 3  # Output: 1 (floor division)
modulus = 5 % 3  # Output: 2 (remainder)
exponentiation = 5 ** 3  # Output: 125 (5 raised to the power of 3)

# Comparison Operators
is_equal = (5 == 5)  # Output: True
is_not_equal = (5 != 3)  # Output: True
greater_than = (5 > 3)  # Output: True

# Logical Operators
is_true = (5 > 3 and 10 > 5)  # Output: True
is_false = not (5 > 3)  # Output: False

# Assignment Operators
x = 5
x += 2  # x = x + 2 (x becomes 7)
```

### 5. **Control Flow**

```python
# If-Else Statements
x = 10
if x > 10:
    print("Greater")
else:
    print("Lesser or equal")  # Output: Lesser or equal

# For Loops
for i in range(5):  # Iterate through 0 to 4
    print(i)  # Output: 0 1 2 3 4

# While Loops
x = 0
while x < 5:
    print(x)  # Output: 0 1 2 3 4
    x += 1

# Break and Continue
for i in range(5):
    if i == 3:
        break  # Stop the loop if i is 3
    print(i)  # Output: 0 1 2

for i in range(5):
    if i == 3:
        continue  # Skip the iteration if i is 3
    print(i)  # Output: 0 1 2 4
```

### 6. **Functions**

```python
# Defining Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Esha"))  # Output: Hello, Esha!

# Parameters and Return Values
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)  # Output: 8

# Built-in Functions
length = len("Esha")  # Output: 4
max_value = max(1, 2, 3)  # Output: 3

# Lambda Functions
square = lambda x: x**2
print(square(4))  # Output: 16
```

### 7. **Data Structures**

```python
# Lists
my_list = [1, 2, 3, 4]
my_list.append(5)  # Adding an item to the list
my_list[0]  # Access first item (Output: 1)

# Tuples
my_tuple = (1, 2, 3)
print(my_tuple[1])  # Output: 2

# Dictionaries
my_dict = {"name": "Esha", "age": 25}
print(my_dict["name"])  # Output: Esha
my_dict["age"] = 26  # Modify value of 'age'

# Sets
my_set = {1, 2, 3}
my_set.add(4)  # Add item to set
print(my_set)  # Output: {1, 2, 3, 4}
```

### 8. **File Handling**

```python
# Reading Files
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Writing Files
with open("output.txt", "w") as file:
    file.write("Hello, World!")
```

### 9. **Error Handling**

```python
# Try-Except Blocks
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Output: Cannot divide by zero!
```

### 10. **Basic Libraries and Data Structures**

```python
# NumPy: Arrays and Mathematical Operations
import numpy as np
arr = np.array([1, 2, 3])
print(arr + 5)  # Output: [6 7 8]

# Pandas: DataFrame Basics
import pandas as pd
data = {'Name': ['Esha', 'John'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df.head())  # Output: First 5 rows of the DataFrame

# Matplotlib: Basic Plotting
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()  # Displays a line plot
```

### 11. **Object-Oriented Programming (OOP) Basics**

```python
# Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("Esha", 25)
person.greet()  # Output: Hello, my name is Esha and I am 25 years old.
```

### 12. **Basic Data Analysis Concepts**

```python
# Exploratory Data Analysis (EDA) with Pandas
import pandas as pd

# Load a dataset (you can replace this with any CSV file)
df = pd.read_csv('data.csv')

# Basic Statistics
print(df.describe())  # Summary statistics of the dataset

# Visualizing data using Matplotlib (Bar Plot)
df['column_name'].value_counts().plot(kind='bar')
plt.show()

# Basic Data Cleaning
df.isnull().sum()  # Check for missing values
df.dropna()  # Drop rows with missing values
```

---

This code covers all the basics your students need to understand when starting with Python and data analysis. Each section demonstrates the core concepts with simple examples that can be easily expanded upon.

Let me know if you'd like further elaboration or additional topics!
