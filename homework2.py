I’m creating the notebook file for you as a proper Jupyter notebook using the cleaned homework content.



## Jupyter notebook content

The notebook creation tool did not complete, so here is the exact content to paste into a new Jupyter notebook file named `homework.ipynb`.

```python
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Homework 2\\n",
    "\\n",
    "**Subject matter:**\\n",
    "\\n",
    "functions, parameters, return values\\n",
    "\\n",
    "**Instructions:**\\n",
    "\\n",
    "Be sure to run each code block after you edit it to make sure it runs as expected. When you are done, we strongly recommend you run all the code from scratch (Runtime menu -> Restart and Run all) to make sure your current code works for all problems.\\n",
    "\\n",
    "If your code raises an exception when run from scratch, it will interfere with the auto-grader process causing you to lose some or all points for this homework. Please ask for help on Piazza, attend office hours or schedule an appointment with your learning facilitator if you get stuck.\\n",
    "\\n",
    "**Warning against using generative AI:**\\n",
    "\\n",
    "We recommend *in the strongest terms* against using generative AI in solving any homework assignment in this module. The goal of these assignments is for you to learn the fundamental concepts about programming: syntax, correctness, problem decomposition, and skepticism. While we know that generative AI can solve all of these problems, you will not be learning anything and will get confused as this module progresses.\\n",
    "\\n",
    "While we encourage you to use AI to generate practice problems, you should try to solve these problems with the help of the sample problems, and examples on blackboard and experimentation.\\n",
    "\\n",
    "**Solution:**\\n",
    "\\n",
    "For each problem description, a sample output has been included to show what the expected output should look like.\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problem 1 (Review)**\\n",
    "\\n",
    "**Concept:** *Review of variables and arithmetic.*\\n",
    "\\n",
    "**Task:**\\n",
    "\\n",
    "Create a variable named `sum_of_primes` that stores the sum of the first four prime numbers. Assign the numbers directly, there is no need for coding logic of finding first four prime numbers.\\n",
    "\\n",
    "After computing the sum, print a message that clearly states what the value represents.\\n",
    "\\n",
    "**Sample Output:**\\n",
    "\\n",
    "```the sum of the first four primes is 10```\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sum_of_primes = 2 + 3 + 5 + 7\\n",
    "print(\\\"the sum of the first four primes is\\\", sum_of_primes)\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problem 2 (Review)**\\n",
    "\\n",
    "**Concept:** *Review of arithmetic and list indexing.*\\n",
    "\\n",
    "**Task:**\\n",
    "Given a numeric value x and a list of three numbers representing coefficients, compute the value of a quadratic polynomial of the form:\\n",
    "\\n",
    "$ax^2 + bx + c$\\n",
    "\\n",
    "Use list indexing to extract the coefficients, calculate the result, store it in a variable y, and print the value of y.\\n",
    "\\n",
    "**Sample Output:**\\n",
    "\\n",
    "```y = 20```\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# starter code\\n",
    "x = 4\\n",
    "coefficients = [2, 3, 4]\\n",
    "\\n",
    "# TO DO: WRITE YOUR CODE/SOLUTION BELOW\\n",
    "y = coefficients[0] * x ** 2 + coefficients[1] * x + coefficients[2]\\n",
    "print(\\\"y =\\\", y)\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problem 3 (Review)**\\n",
    "\\n",
    "**Concept:** *Review of extracting substrings using string slicing.*\\n",
    "\\n",
    "**Task:**\\n",
    "\\n",
    "Initialize a variable called `date` as 31st January 2026 in dd-mm-yyyy format.\\n",
    "\\n",
    "Extract the year as `year`, month as `month` and date as `day`.\\n",
    "\\n",
    "Print a message that clearly states the separated variables.\\n",
    "\\n",
    "**Sample Output:**\\n",
    "\\n",
    "```The year is 2026 and month is 05 and day is 22```\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TO DO: WRITE YOUR CODE/SOLUTION BELOW\\n",
    "date = \\\"31-01-2026\\\"\\n",
    "\\n",
    "year = date[6:10]\\n",
    "month = date[3:5]\\n",
    "day = date[0:2]\\n",
    "\\n",
    "print(\\\"The year is\\\", year, \\\"and month is\\\", month, \\\"and day is\\\", day)\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problem 4**\\n",
    "\\n",
    "**Concept:** *Functions with numeric parameters.*\\n",
    "\\n",
    "**Task:**\\n",
    "\\n",
    "Write two functions using the exact names below:\\n",
    "\\n",
    "1) `my_sum(a, b)`\\n",
    "    \\n",
    "    Returns the sum of a and b.\\n",
    "\\n",
    "2) `my_diff(a, b)`\\n",
    "\\n",
    "    Returns the difference of a minus b.\\n",
    "\\n",
    "Use the provided test cases to verify your functions.\\n",
    "\\n",
    "**Sample Output:**\\n",
    "\\n",
    "```\\n",
    "my_sum(3,4) returned 7\\n",
    "my_diff(3,4) returned -1\\n",
    "```\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TO DO: WRITE YOUR CODE/SOLUTION BELOW\\n",
    "def my_sum(a, b):\\n",
    "    return a + b\\n",
    "\\n",
    "def my_diff(a, b):\\n",
    "    return a - b\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Test cases for problem 4**\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# test cases for your functions\\n",
    "print('my_sum(3, 4) returned', my_sum(3, 4))\\n",
    "print('my_diff(3, 4) returned', my_diff(3, 4))\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problem 5**\\n",
    "\\n",
    "**Concept:** *Function with numeric parameters.*\\n",
    "\\n",
    "**Task:**\\n",
    "\\n",
    "Write the following two functions using exactly these names and parameters:\\n",
    "\\n",
    "1. `calculate(a, b, c)`\\n",
    "\\n",
    "    Returns the value of the expression:\\n",
    "\\n",
    "    7a + 6b + 5c + 4\\n",
    "\\n",
    "2. `mystery(a, b, c)`\\n",
    "\\n",
    "    Returns the value of the expression:\\n",
    "\\n",
    "> $7a - 6b^2 + 5c^4$\\n",
    "\\n",
    "Use the provided test cases to check your results.\\n",
    "\\n",
    "**Sample Output:**\\n",
    "\\n",
    "```\\n",
    "calculate(3, 4, 5) returned 74\\n",
    "mystery(3, 4, 5) returned 3050\\n",
    "```\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TO DO: WRITE YOUR CODE/SOLUTION BELOW\\n",
    "def calculate(a, b, c):\\n",
    "    return 7 * a + 6 * b + 5 * c + 4\\n",
    "\\n",
    "def mystery(a, b, c):\\n",
    "    return 7 * a - 6 * b ** 2 + 5 * c ** 4\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Test cases for problem 5**\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# test cases for your functions\\n",
    "print('calculate(3, 4, 5) returned', calculate(3, 4, 5))\\n",
    "print('mystery(3, 4, 5) returned', mystery(3, 4, 5))\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problem 6**\\n",
    "\\n",
    "**Concept:** *Function with string parameters*\\n",
    "\\n",
    "**Task:**\\n",
    "\\n",
    "Write a function named `initials(first, last)` that:\\n",
    "\\n",
    "Takes two string parameters: first and last\\n",
    "\\n",
    "Returns a string containing the first character of first followed by the first character of last\\n",
    "\\n",
    "Test your function using the provided examples.\\n",
    "\\n",
    "**Sample Output:**\\n",
    "\\n",
    "```\\n",
    "initials(\\\"john\\\", \\\"lennon\\\") returned jl\\n",
    "initials(\\\"paul\\\", \\\"mccartney\\\") returned pm\\n",
    "```\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TO DO: WRITE YOUR CODE/SOLUTION BELOW\\n",
    "def initials(first, last):\\n",
    "    return first[0] + last[0]\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Test cases for problem 6**\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print('initials(\\\"john\\\", \\\"lennon\\\") returned', initials(\\\"john\\\", \\\"lennon\\\"))\\n",
    "print('initials(\\\"paul\\\", \\\"mccartney\\\") returned', initials(\\\"paul\\\", \\\"mccartney\\\"))\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problem 7**\\n",
    "\\n",
    "**Concept:** *Function with a list as parameter.*\\n",
    "\\n",
    "**Task:**\\n",
    "\\n",
    "Write two functions with the exact names below:\\n",
    "\\n",
    "1) `first_and_last(numbers)`\\n",
    "\\n",
    "    Returns the sum of the first and last elements in the list numbers.\\n",
    "\\n",
    "2) `mean_of_list(numbers)`\\n",
    "\\n",
    "    Returns the mean (average) of all values in the list numbers.\\n",
    "\\n",
    "Use the provided test cases.\\n",
    "\\n",
    "**Sample Output:**\\n",
    "\\n",
    "```\\n",
    "first_and_last([6,1,7,3,5,8,2,3,6,1]) = 7\\n",
    "mean_of_list([6,1,7,3,5,8,2,3,6,1]) = 4.2\\n",
    "```\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TO DO: WRITE YOUR CODE/SOLUTION BELOW\\n",
    "def first_and_last(numbers):\\n",
    "    return numbers[0] + numbers[-1]\\n",
    "\\n",
    "def mean_of_list(numbers):\\n",
    "    return sum(numbers) / len(numbers)\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Test cases for problem 7**\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# test cases for your functions:\\n",
    "print('first_and_last([6,1,7,3,5,8,2,3,6,1]) =', first_and_last([6,1,7,3,5,8,2,3,6,1]))\\n",
    "print('mean_of_list([6,1,7,3,5,8,2,3,6,1]) =', mean_of_list([6,1,7,3,5,8,2,3,6,1]))\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problem 8**\\n",
    "\\n",
    "**Concept:** *Function with a list as parameter.*\\n",
    "\\n",
    "**Task:**\\n",
    "\\n",
    "Write a function named `polynomial(x, coefficients)` that:\\n",
    "\\n",
    "* Takes a number `x`\\n",
    "* Takes a list named `coefficients` containing exactly four values\\n",
    "* Computes the polynomial:\\n",
    "\\n",
    "  $a x^3 + b x^2 + c x + d$\\n",
    "\\n",
    "Use list indexing to access the coefficients.\\n",
    "\\n",
    "**Sample Output:**\\n",
    "\\n",
    "```\\n",
    "polynomial(1, [2, 3, 4, 5]) = 14\\n",
    "polynomial(2, [2, 3, 4, 6]) = 42\\n",
    "```\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TO DO: WRITE YOUR CODE/SOLUTION BELOW\\n",
    "def polynomial(x, coefficients):\\n",
    "    a = coefficients[0]\\n",
    "    b = coefficients[1]\\n",
    "    c = coefficients[2]\\n",
    "    d = coefficients[3]\\n",
    "    return a * x ** 3 + b * x ** 2 + c * x + d\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Test cases for problem 8**\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# test cases for your function:\\n",
    "print('polynomial(1, [2, 3, 4, 5]) =', polynomial(1, [2, 3, 4, 5]))\\n",
    "print('polynomial(2, [2, 3, 4, 6]) =', polynomial(2, [2, 3, 4, 6]))\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problem 9**\\n",
    "\\n",
    "**Concept:** *Function with a parameter which is a list of strings.*\\n",
    "\\n",
    "**Task:**\\n",
    "\\n",
    "Write a function named `make_initials(names)` that:\\n",
    "\\n",
    "* Takes a list named `names` containing exactly three strings\\n",
    "(first, middle, last)\\n",
    "\\n",
    "* Returns a string consisting of the first character of each name\\n",
    "\\n",
    "**Sample Output:**\\n",
    "\\n",
    "```\\n",
    "make_initials([\\\"john\\\", \\\"winston\\\", \\\"lennon\\\"]) = jwl\\n",
    "make_initials([\\\"james\\\", \\\"paul\\\", \\\"mccartney\\\"]) = jpm\\n",
    "```\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TO DO: WRITE YOUR CODE/SOLUTION BELOW\\n",
    "def make_initials(names):\\n",
    "    return names[0][0] + names[1][0] + names[2][0]\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Test cases for problem 9**\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# test cases for your function\\n",
    "print('make_initials([\\\"john\\\", \\\"winston\\\", \\\"lennon\\\"]) =', make_initials([\\\"john\\\", \\\"winston\\\", \\\"lennon\\\"]))\\n",
    "print('make_initials([\\\"james\\\", \\\"paul\\\", \\\"mccartney\\\"]) =', make_initials([\\\"james\\\", \\\"paul\\\", \\\"mccartney\\\"]))\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problem 10**\\n",
    "\\n",
    "**Concept:** *Function that returns a list.*\\n",
    "\\n",
    "**Task:**\\n",
    "\\n",
    "Write a function named `first_mid_last(my_list)` that:\\n",
    "\\n",
    "* Takes a list named `my_list`\\n",
    "* Returns a new list containing:\\n",
    "    * First element\\n",
    "    * Middle element\\n",
    "    * Last element\\n",
    "\\n",
    "**Note:**\\n",
    "\\n",
    "For lists with even number of elements, you should return the second middle element. See sample test cases for details.\\n",
    "\\n",
    "**Sample Output:**\\n",
    "\\n",
    "```\\n",
    "first_mid_last([1, 2, 3, 4, 5]) = [1, 3, 5]\\n",
    "first_mid_last([6,1,7,3,5,8,2,3,6,1]) = [6, 8, 1]\\n",
    "```\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TO DO: WRITE YOUR CODE/SOLUTION BELOW\\n",
    "def first_mid_last(my_list):\\n",
    "    mid = len(my_list) // 2\\n",
    "    return [my_list[0], my_list[mid], my_list[-1]]\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Test cases for problem 10**\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print('first_mid_last([1, 2, 3, 4, 5]) =', first_mid_last([1, 2, 3, 4, 5]))\\n",
    "print('first_mid_last([6,1,7,3,5,8,2,3,6,1]) =', first_mid_last([6,1,7,3,5,8,2,3,6,1]))\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Problem 11**\\n",
    "\\n",
    "**Concept:** *Function that returns a list.*\\n",
    "\\n",
    "**Task:**\\n",
    "\\n",
    "Write a function named `change_from_a_dollar(price)` that:\\n",
    "\\n",
    "* Takes an integer `price` (in cents, less than 100)\\n",
    "* Calculates how much change is needed from one dollar (100 cents)\\n",
    "* Returns a list in the following order:\\n",
    "    1. Number of quarters (1 quarter = 25 cents)\\n",
    "    2. Number of dimes (1 dime = 10 cents)\\n",
    "    3. Number of nickels (1 nickel = 5 cents)\\n",
    "    4. Number of pennies (1 penny = 1 cent)\\n",
    "\\n",
    "**Sample Output:**\\n",
    "\\n",
    "```\\n",
    "change_from_a_dollar(22) returned [3, 0, 0, 3]\\n",
    "change_from_a_dollar(42) returned [2, 0, 1, 3]\\n",
    "```\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# TO DO: WRITE YOUR CODE/SOLUTION BELOW\\n",
    "def change_from_a_dollar(price):\\n",
    "    change = 100 - price\\n",
    "    quarters = change // 25\\n",
    "    change = change % 25\\n",
    "    dimes = change // 10\\n",
    "    change = change % 10\\n",
    "    nickels = change // 5\\n",
    "    pennies = change % 5\\n",
    "    return [quarters, dimes, nickels, pennies]\\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Test cases for problem 11**\\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\\\"change_from_a_dollar(22) returned\\\", change_from_a_dollar(22))\\n",
    "print(\\\"change_from_a_dollar(42) returned\\\", change_from_a_dollar(42))\\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

If you want, I can also give you the same notebook as a plain `.py` script version.