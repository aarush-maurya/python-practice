# 5: Mini Calculator
print("\033[32m=== Mini Calculator ===\033[0m")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /, ^): ")
if op == '+':
    ans = num1 + num2
elif op == '-':
    ans = num1 - num2
elif op == '*':
    ans = num1 * num2
elif op == '^':
    ans = num1 ** num2
elif op == '/' and num2 == 0:
    ans = "Undefined (division by zero)"
elif op == '/':
    ans = num1 / num2
else:
    ans = "Invalid operator"
print("So your answer is:", "\033[31m", ans, "\033[0m")