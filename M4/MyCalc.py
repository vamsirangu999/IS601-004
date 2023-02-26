# ucid=vr76 date=25/02/2023
# Define a class named MyCalc
class MyCalc:
    # Initialize the class with an instance variable called 'ans'
    def __init__(self):
        self.ans = 0

    # ucid=vr76 date=25/02/2023
    # Summary:
    # Define a method called 'add' that takes two parameters 'a' and 'b'
    def add(self, a, b):
        # Add 'a' and 'b' and store the result in the instance variable 'ans'
        self.ans = a + b
        # print result and update ans variable
        print(f"Result: {self.ans}")

    # ucid=vr76 date=25/02/2023
    # Summary:
    # Define a method called 'subtract' that takes two parameters 'a' and 'b'
    def subtract(self, a, b):
        # Subtract 'b' from 'a' and store the result in the instance variable 'ans'
        self.ans = a - b
        # print result and update ans variable
        print(f"Result: {self.ans}")

    # ucid=vr76 date=25/02/2023
    # Summary:
    # Define a method called 'multiply' that takes two parameters 'a' and 'b'
    def multiply(self, a, b):
        # Multiply 'a' and 'b' and store the result in the instance variable 'ans'
        self.ans = a * b
        # print result and update ans variable
        print(f"Result: {self.ans}")

    # ucid=vr76 date=25/02/2023
    # Summary:
    # Define a method called 'divide' that takes two parameters 'a' and 'b'
    def divide(self, a, b):
        # Check if 'b' is 0 to avoid division by zero
        if b == 0:
            print("Cannot divide by zero")
            # Return True to indicate that a division by zero occurred
            return True
        else:
            # Divide 'a' by 'b' and store the result in the instance variable 'ans'
            self.ans = a / b
            # print result and update ans variable
            print(f"Result: {self.ans}")

    # ucid=vr76 date=25/02/2023
    # Summary:
    # Define a method called 'run' that takes a string parameter called 'user_input'
    def run(self, user_input):
        try:
            # Parse the user input into operand1, operator, and operand2
            if "ans" in user_input:
                operand1, operator, operand2 = user_input.split(" ")[0], user_input.split(" ")[1], \
                                               user_input.split(" ")[2]
                if operand1 == "ans":
                    operand1 = self.ans
                if operand2 == "ans":
                    operand2 = self.ans
                # operand = calc.ans if operand == "ans" else operand
            else:
                operand1, operator, operand2 = user_input.split(" ")[0], user_input.split(" ")[1], \
                                               user_input.split(" ")[2]
            # Convert the operands to float
            operand1 = float(operand1)
            operand2 = float(operand2)

            # Perform the calculation based on the operator
            if operator == "+":
                self.add(operand1, operand2)
            elif operator == "-":
                self.subtract(operand1, operand2)
            elif operator == "*":
                self.multiply(operand1, operand2)
            elif operator == "/":
                res = self.divide(operand1, operand2)
                if res:
                    return "Cannot divide by zero"
            else:
                print("Error: Invalid operator.")

            # Return the instance variable 'ans'
            return self.ans

        except (ValueError, IndexError):
            print("Error: Invalid input.")


if __name__ == '__main__':
    calc = MyCalc()
    # ucid=vr76 date=25/02/2023
    # Summary:
    # This code block loops infinitely, prompting the user to enter a calculation and passing that input
    # to the 'run' method of the MyCalc instance 'calc'.
    while True:
        user_input = input("Enter a calculation: ")
        calc.run(user_input=user_input)
