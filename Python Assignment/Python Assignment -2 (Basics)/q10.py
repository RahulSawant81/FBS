# Reverse a three-digit number

num = int(input("Enter a three-digit number: "))

x = num // 100
y = (num // 10) % 10
z = num % 10

reverse = z * 100 + y * 10 + x

print("Reversed NUmber: ", reverse)

# output:
# Enter athree-digit number: 456
# Reversed NUmber:  654