# Convert time (hh, min, sec) into seconds

hh = int(input("Enter hours: "))
mm = int(input("Enter minutes: "))
ss = int(input("Enter seconds: "))

total_seconds = hh * 3600 + mm * 60 + ss

print("Total seconds =", total_seconds)

# Output:
# Enter hours: 1
# Enter minutes: 30
# Enter seconds: 20
# Total seconds = 5420