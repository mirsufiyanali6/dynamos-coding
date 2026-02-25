tutorials = [

    {
        "section": "Python Fundamentals",
        "slug": "introduction",
        "title": "Introduction to Python",
        "content": """Python is a high-level, interpreted programming language.
It is beginner-friendly and widely used in web development, AI, automation, and data science.

Example:
print("Hello, World!")

Python executes code line by line.
No compilation is required.
""",
        "practice_question": "Write a Python program that prints: Welcome to Dynamos Coding",
        "practice_solution": 'print("Welcome to Dynamos Coding")'
    },

    {
        "section": "Python Fundamentals",
        "slug": "variables",
        "title": "Variables & Data Types",
        "content": """Variables store data.

x = 10
name = "Dynamos"

Common data types:
• int
• float
• str
• bool

Python automatically detects type.
""",
        "practice_question": "Create a variable age with value 25 and print it.",
        "practice_solution": "age = 25\nprint(age)"
    },

    {
        "section": "Python Fundamentals",
        "slug": "input-output",
        "title": "Input & Output",
        "content": """Use print() to display output.
Use input() to take user input.

name = input("Enter your name: ")
print("Hello", name)

Input always returns string.
""",
        "practice_question": "Write a program that asks the user for their name and prints Hello <name>.",
        "practice_solution": 'name = input("Enter your name: ")\nprint("Hello", name)'
    },

    {
        "section": "Python Fundamentals",
        "slug": "type-casting",
        "title": "Type Casting",
        "content": """Convert data types using:

int()
float()
str()

Example:
num = int("5")
print(num + 2)
""",
        "practice_question": "Take a number as input and convert it to integer before printing it.",
        "practice_solution": 'num = int(input("Enter number: "))\nprint(num)'
    },

    {
        "section": "Python Fundamentals",
        "slug": "comments",
        "title": "Comments in Python",
        "content": """Comments explain code.

Single-line comment:
# This is a comment

Multi-line:
\"\"\"
This is
multi-line comment
\"\"\"
""",
        "practice_question": "Write a program with a comment explaining what it does.",
        "practice_solution": "# This program prints Hello\nprint('Hello')"
    },

    {
        "section": "Control Flow",
        "slug": "if-else",
        "title": "If / Else Statements",
        "content": """Conditional statements execute code based on conditions.

age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
""",
        "practice_question": "Write a program to check if a number is positive or negative.",
        "practice_solution": "num = int(input())\nif num >= 0:\n    print('Positive')\nelse:\n    print('Negative')"
    },

    {
        "section": "Control Flow",
        "slug": "nested-conditions",
        "title": "Nested Conditions",
        "content": """You can place if inside another if.

num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
""",
        "practice_question": "Check if a number is positive and even.",
        "practice_solution": "num = int(input())\nif num > 0:\n    if num % 2 == 0:\n        print('Positive Even')"
    },

    {
        "section": "Control Flow",
        "slug": "for-loop",
        "title": "For Loop",
        "content": """For loop repeats fixed number of times.

for i in range(5):
    print(i)

range(start, stop, step)
""",
        "practice_question": "Print numbers from 1 to 5 using a for loop.",
        "practice_solution": "for i in range(1, 6):\n    print(i)"
    },

    {
        "section": "Control Flow",
        "slug": "while-loop",
        "title": "While Loop",
        "content": """While loop runs while condition is true.

i = 1

while i <= 5:
    print(i)
    i += 1
""",
        "practice_question": "Print numbers from 1 to 5 using a while loop.",
        "practice_solution": "i = 1\nwhile i <= 5:\n    print(i)\n    i += 1"
    },

    {
        "section": "Control Flow",
        "slug": "break-continue",
        "title": "Break & Continue",
        "content": """Break exits loop immediately.
Continue skips current iteration.

for i in range(5):
    if i == 3:
        break
    print(i)
""",
        "practice_question": "Write a loop that stops when number 3 is reached.",
        "practice_solution": "for i in range(10):\n    if i == 3:\n        break\n    print(i)"
    }

]