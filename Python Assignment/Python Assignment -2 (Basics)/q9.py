# Swap two numbers (without third variable)

a = int(input("Enter first Number: "))
b = int(input("Enter second number: "))

print("Before Swapping")
print("a: " , a)
print("b: " , b)

#  arithmatic swap
a = a + b
b = a - b
a = a - b

print("After Swapping")
print("a: " , a)
print("b: " , b)

# tupple sewap

print("tupple sewapping")
x, y = 5, 7

print("Before swapping:", x, y)

# Swapping using tuple 
x, y = y, x

print("After swapping:", x, y)

# output:
# Enter first Number: 5
# Enter second number: 7
# Before Swapping
# a:  5
# b:  7
# After Swapping
# a:  7
# b:  5
# Before swapping: 5 7
# After swapping: 7 5