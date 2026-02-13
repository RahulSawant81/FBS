# Sum of three-digit number

num = int(input("Enter a three-digit number: "))

digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10

total_sum = digit1 + digit2 + digit3
print("Sum of the digits =", total_sum)

# Output:
# Enter a three-digit number: 123
# Sum of the digits = 6