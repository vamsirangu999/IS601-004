from MyCalc import MyCalc


# ucid=vr76 date=25/02/2023
def test_number_add_number():
    calc = MyCalc()

    # Defining two lists of operands and their expected results
    operand1 = ["1", "2", "4", "3"]
    operand2 = ["1", "3", "-1", "0"]
    result = [2.0, 5.0, 3.0, 3.0]

    # Summary:
    # Iterating over each pair of operands and expected results, and testing the addition operation
    for i in range(len(result)):
        assert calc.run(operand1[i] + " + " + operand2[i]) == result[i]


# ucid=vr76 date=25/02/2023
def test_ans_add_number():
    calc = MyCalc()

    # Defining two lists of operands and their expected results
    operand1 = ["ans", "ans", "ans", "ans"]
    operand2 = ["1", "3", "-3", "0"]
    result = [1.0, 4.0, 1.0, 1.0]

    # Summary:
    # Iterating over each pair of operands and expected results, and testing the addition operation
    for i in range(len(result)):
        assert calc.run(operand1[i] + " + " + operand2[i]) == result[i]


# ucid=vr76 date=25/02/2023
def test_number_sub_number():
    calc = MyCalc()

    # Defining two lists of operands and their expected results
    operand1 = ["10", "2", "4", "3"]
    operand2 = ["1", "3", "-1", "0"]
    result = [9.0, -1.0, 5.0, 3.0]

    # Summary:
    # Iterating over each pair of operands and expected results, and testing the addition operation
    for i in range(len(result)):
        assert calc.run(operand1[i] + " - " + operand2[i]) == result[i]


# ucid=vr76 date=25/02/2023
def test_ans_sum_number():
    calc = MyCalc()

    # Defining two lists of operands and their expected results
    operand1 = ["ans", "ans", "ans", "ans"]
    operand2 = ["1", "3", "-3", "0"]
    result = [-1.0, -4.0, -1.0, -1.0]

    # Summary:
    # Iterating over each pair of operands and expected results, and testing the addition operation
    for i in range(len(result)):
        assert calc.run(operand1[i] + " - " + operand2[i]) == result[i]


# ucid=vr76 date=25/02/2023
def test_number_mult_number():
    calc = MyCalc()

    # Defining two lists of operands and their expected results
    operand1 = ["-1", "2", "-4", "3"]
    operand2 = ["1", "3", "-1", "0"]
    result = [-1.0, 6.0, 4.0, 0.0]

    # Summary:
    # Iterating over each pair of operands and expected results, and testing the addition operation
    for i in range(len(result)):
        assert calc.run(operand1[i] + " * " + operand2[i]) == result[i]


# ucid=vr76 date=25/02/2023
def test_ans_mult_number():
    calc = MyCalc()

    # Defining two lists of operands and their expected results
    operand1 = ["1", "ans", "ans", "ans"]
    operand2 = ["1", "3", "-3", "0"]
    result = [1.0, 3.0, -9.0, 0.0]

    # Summary:
    # Iterating over each pair of operands and expected results, and testing the addition operation
    for i in range(len(result)):
        assert calc.run(operand1[i] + " * " + operand2[i]) == result[i]


# ucid=vr76 date=25/02/2023
def test_number_div_number():
    calc = MyCalc()

    # Defining two lists of operands and their expected results
    operand1 = ["1", "3", "9", "3"]
    operand2 = ["1", "2", "-2", "0"]
    result = [1.0, 1.5, -4.5, "Cannot divide by zero"]

    # Summary:
    # Iterating over each pair of operands and expected results, and testing the addition operation
    for i in range(len(result)):
        assert calc.run(operand1[i] + " / " + operand2[i]) == result[i]


# ucid=vr76 date=25/02/2023
def test_ans_div_number():
    calc = MyCalc()

    # Defining two lists of operands and their expected results
    operand1 = ["1", "ans", "ans", "ans"]
    operand2 = ["10", "0.1", "2", "0"]
    result = [0.1, 1.0, 0.5, "Cannot divide by zero"]

    # Summary:
    # Iterating over each pair of operands and expected results, and testing the addition operation
    for i in range(len(result)):
        assert calc.run(operand1[i] + " / " + operand2[i]) == result[i]
