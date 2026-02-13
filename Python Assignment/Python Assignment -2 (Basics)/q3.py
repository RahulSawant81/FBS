# Convert feet & inches into meters & centimeters


feet  = int(input("Enter feet: "))
inches = int(input("Enter inches: "))


total_inches = (feet * 12) + inches
meters = total_inches * 0.0254
centimeters = total_inches * 2.54

print("Meters =", meters)
print("Centimeters =", centimeters)

# Output:
# Enter feet: 5
# Enter inches: 8
# Meters = 1.7272
# Centimeters = 172.72