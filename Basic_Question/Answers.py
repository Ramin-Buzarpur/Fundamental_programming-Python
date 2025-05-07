# Python Programming Practice - Answer Key
# ----------------------------------------
# This file contains complete solutions to all 50 Python practice problems, covering:
#     * Basic operations and variables
#     * Conditional statements
#     * Data structures (Lists, Tuples, Dictionaries, Sets)
#     * Functions and recursion
#     * Advanced topics (OOP, File I/O, Decorators)
# ----------------------------------------

# Section 1: Variable Assignment and Basic Operations (4 Questions)
# ---------------------------------------------------------------

# 1. Calculate the sum of two variables:
# a = 5
# b = 3
# print(a + b)

# 2. Compute the circumference of a circle:
# PI = 3.14
# radius = 5
# print(2 * PI * radius)

# 3. Count characters in a string without using len():
# text = "Hello"
# count = 0
# for char in text:
#     count += 1
# print(count)

# 4. Swap two variables without a temporary variable:
# x = 5
# y = 10
# x, y = y, x
# print(x, y)

# Section 2: Conditional Statements (6 Questions)
# ----------------------------------------------

# 5. Determine student status based on score:
# score = 16
# if score < 10:
#     print("Fail")
# elif 10 <= score < 15:
#     print("Needs Improvement")
# else:
#     print("Pass")

# 6. FizzBuzz problem:
# num = 15
# if num % 15 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")

# 7. Sort three numbers in descending order:
# a, b, c = 3, 1, 2
# if a > b: a, b = b, a
# if b > c: b, c = c, b
# if a > b: a, b = b, a
# print(a, b, c)

# 8. Check age and gender for access:
# age = 20
# gender = "Male"
# if age > 18 and gender == "Male":
#     print("Access Granted")

# 9. Validate if a number is within range:
# num = 150
# if 100 <= num <= 200:
#     print("Valid")

# 10. Check for leap year:
# year = 2024
# if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#     print("Leap Year")

# Section 3: Lists (8 Questions)
# -----------------------------

# 11. Sum of odd numbers in a list:
# numbers = [1, 2, 3, 4, 5]
# sum_odd = sum(num for num in numbers if num % 2 != 0)
# print(sum_odd)

# 12. Filter names starting with 'A':
# names = ["Ali", "Ahmad", "Sara"]
# a_names = [name for name in names if name.startswith("A")]
# print(a_names)

# 13. Reverse a list:
# lst = [1, 2, 3]
# print(lst[::-1])

# 14. Remove negative numbers from list:
# numbers = [1, -2, 3, -4]
# positive = [num for num in numbers if num >= 0]
# print(positive)

# 15. Find second smallest number:
# numbers = [5, 2, 8, 1]
# numbers.sort()
# print(numbers[1])

# 16. Generate all possible sums from two lists:
# list1 = [1, 2]
# list2 = [3, 4]
# combined = [x + y for x in list1 for y in list2]
# print(combined)

# 17. Remove consecutive duplicates:
# lst = [1, 2, 2, 3]
# result = [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i-1]]
# print(result)

# 18. Check if list is strictly increasing:
# lst = [1, 3, 5]
# is_increasing = all(lst[i] < lst[i+1] for i in range(len(lst)-1))
# print(is_increasing)

# Section 4: Tuples (5 Questions)
# -------------------------------

# 19. Calculate Euclidean distance from origin:
# point = (3, 4)
# distance = (point[0]**2 + point[1]**2)**0.5
# print(distance)

# 20. Attempt to modify tuple (demonstrate immutability):
# book = ("Title", "Author", 2000)
# new_book = (book[0], book[1], 2001)
# print(new_book)

# 21. Find common elements between tuples:
# t1 = (1, 2, 3)
# t2 = (2, 3, 4)
# common = [x for x in t1 if x in t2]
# print(common)

# 22. Convert tuple of digits to integer:
# digits = (1, 2, 3)
# number = int(''.join(map(str, digits)))
# print(number)

# 23. Join tuple elements with separator:
# colors = ("red", "green", "blue")
# print("|".join(colors))

# Section 5: Dictionaries (8 Questions)
# ------------------------------------

# 24. Calculate total sales from dictionary:
# sales = {"apple": 100, "banana": 200}
# print(sum(sales.values()))

# 25. Merge two dictionaries:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# merged = {**dict1, **dict2}
# print(merged)

# 26. Find student with highest average:
# grades = {"Ali": 18, "Sara": 20}
# print(max(grades, key=grades.get))

# 27. Remove empty values from dictionary:
# data = {"name": "Ali", "age": None}
# clean = {k: v for k, v in data.items() if v is not None}
# print(clean)

# 28. Simple dictionary lookup:
# dictionary = {"hello": "سلام", "goodbye": "خداحافظ"}
# word = "hello"
# print(dictionary.get(word, "Not found"))

# 29. Find most frequent number:
# freq = {1: 3, 2: 5, 3: 2}
# print(max(freq, key=freq.get))

# 30. Validate required dictionary keys:
# user = {"name": "Ali", "age": 20}
# required = ["name", "age", "email"]
# for key in required:
#     if key not in user:
#         print(f"Missing {key}")

# 31. Filter products above average price:
# products = [{"name": "A", "price": 100}, {"name": "B", "price": 200}]
# avg = sum(p["price"] for p in products) / len(products)
# above_avg = [p for p in products if p["price"] > avg]
# print(above_avg)

# Section 6: Sets (4 Questions)
# -----------------------------

# 32. Set intersection and union:
# set1 = {1, 2}
# set2 = {2, 3}
# result = {"intersection": set1 & set2, "union": set1 | set2}
# print(result)

# 33. Convert list to set and check length:
# lst = [1, 2, 2, 3]
# s = set(lst)
# print("Changed" if len(lst) != len(s) else "Not changed")

# 34. Symmetric difference of sets:
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1 ^ set2)

# 35. Identify special numbers (neither prime nor composite):
# primes = {2, 3, 5}
# composites = {4, 6}
# special = {0, 1} - primes - composites
# print(special)

# Section 7: Functions (8 Questions)
# ----------------------------------

# 36. Calculate standard deviation:
# import math
# def std_dev(numbers):
#     mean = sum(numbers)/len(numbers)
#     return math.sqrt(sum((x-mean)**2 for x in numbers)/len(numbers))
# print(std_dev([1, 2, 3]))

# 37. Recursive Fibonacci sequence:
# def fib(n):
#     return n if n <= 1 else fib(n-1) + fib(n-2)
# print([fib(i) for i in range(10)])

# 38. Sum of squares using *args:
# def sum_squares(*args):
#     return sum(x*x for x in args)
# print(sum_squares(1, 2, 3))

# 39. Filter list with condition function:
# def filter_list(lst, condition):
#     return [x for x in lst if condition(x)]
# print(filter_list([1, 2, 3], lambda x: x % 2 != 0))

# 40. Convert decimal to binary:
# def to_binary(n):
#     return bin(n)[2:]
# print(to_binary(10))

# 41. Calculate BMI:
# def bmi(weight, height):
#     return weight / (height ** 2)
# print(bmi(70, 1.75))

# 42. Check for palindrome:
# def is_palindrome(s):
#     return s == s[::-1]
# print(is_palindrome("madam"))

# 43. Calculate age from birthdate:
# from datetime import datetime
# def calculate_age(birth_date):
#     today = datetime.today()
#     return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
# print(calculate_age(datetime(1990, 5, 15)))

# Section 8: Advanced Topics (7 Questions)
# ---------------------------------------

# 44. Calculate average salary by department:
# employees = [
#     {"name": "Ali", "dept": "IT", "salary": 5000},
#     {"name": "Sara", "dept": "HR", "salary": 4000}
# ]

# dept_salaries = {}
# for emp in employees:
#     dept = emp["dept"]
#     if dept not in dept_salaries:
#         dept_salaries[dept] = []
#     dept_salaries[dept].append(emp["salary"])

# for dept, salaries in dept_salaries.items():
#     print(f"{dept}: {sum(salaries)/len(salaries)}")

# 45. Sum of main diagonal in matrix:
# matrix = [[1, 2], [3, 4]]
# print(sum(matrix[i][i] for i in range(len(matrix))))

# 46. Extract nested dictionary value:
# data = {"person": {"name": "Ali", "age": 20}}
# keys = ["person", "age"]
# result = data
# for key in keys:
#     result = result[key]
# print(result)

# 47. Create number frequency histogram from file:
# from collections import defaultdict
# def file_histogram(filename):
#     hist = defaultdict(int)
#     with open(filename) as f:
#         for line in f:
#             for num in line.split():
#                 hist[int(num)] += 1
#     return hist
# print(file_histogram("numbers.txt"))

# 48. Count sentences, words and characters:
# def text_stats(text):
#     sentences = text.count('.') + text.count('!') + text.count('?')
#     words = len(text.split())
#     chars = len(text)
#     return sentences, words, chars
# print(text_stats("Hello world. How are you?"))

# 49. Simple calculator class:
# class Calculator:
#     def add(self, a, b): return a + b
#     def subtract(self, a, b): return a - b
#     def multiply(self, a, b): return a * b
#     def divide(self, a, b): return a / b if b != 0 else "Error"

# calc = Calculator()
# print(calc.add(5, 3))

# 50. Function result caching decorator:
# def cache(func):
#     cached = {}
#     def wrapper(*args):
#         if args not in cached:
#             cached[args] = func(*args)
#         return cached[args]
#     return wrapper

# @cache
# def expensive_func(x):
#     return x * x

# print(expensive_func(5))
# print(expensive_func(5))  # Returns cached result