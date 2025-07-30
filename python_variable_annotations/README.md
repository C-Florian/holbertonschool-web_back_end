# Python - Variable Annotations

## Description

This project focuses on the concept of variable annotations and type hinting in Python 3. It aims to help you understand and apply type annotations to function parameters, return types, and variables. You will also learn about duck typing and how to validate Python code with the `mypy` tool.

## Learning Objectives

At the end of this project, you should be able to:

- Understand and explain type annotations in Python 3.
- Use type annotations to specify function signatures and variable types.
- Understand and apply duck typing in Python.
- Validate Python code with `mypy`.

## Project Structure

This project contains the following tasks:

1. **Basic Annotations - add**: Write a type-annotated function `add` that takes two `float` numbers as arguments and returns their sum as a `float`.
2. **Basic Annotations - concat**: Write a type-annotated function `concat` that takes two strings and returns a concatenated string.
3. **Basic Annotations - floor**: Write a type-annotated function `floor` that takes a `float` number and returns its floor (rounded down).
4. **Basic Annotations - to string**: Write a type-annotated function `to_str` that takes a `float` and returns its string representation.
5. **Define Variables**: Define and annotate variables with appropriate types (int, float, bool, string).
6. **Complex Types - List of Floats**: Write a type-annotated function `sum_list` that takes a list of floats and returns their sum.
7. **Complex Types - Mixed List**: Write a type-annotated function `sum_mixed_list` that takes a mixed list of integers and floats and returns their sum.
8. **Complex Types - String and Int/Float to Tuple**: Write a type-annotated function `to_kv` that takes a string and a number (int or float) and returns a tuple with the string and the square of the number.
9. **Complex Types - Functions**: Write a type-annotated function `make_multiplier` that returns a multiplier function.
10. **Duck Typing an Iterable Object**: Write a function `element_length` that takes an iterable and returns a list of tuples with each element and its length.

## Installation

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/C-Florian/holbertonschool-web_back_end.git
    ```

2. Navigate to the `python_variable_annotations` directory.

    ```bash
    cd holbertonschool-web_back_end/holbertonschool-web_back_end/python_variable_annotations
    ```

3. Ensure that Python 3.9 or later is installed on your machine.

4. Install `mypy` for static type checking.

    ```bash
    pip install mypy
    ```

## Usage

You can run each task's code by executing the respective Python script file. For example, to run Task 1 (add):

```bash
python3 0-main.py
