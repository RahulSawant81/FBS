#  Minimum number of notes

amount = int(input("Enter amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

print("Minimum number of notes required:")

for note in notes:
    count = amount // note   # how many notes of this type
    if count > 0:
        print(note, "=", count)
        amount = amount % note

# output:
# Enter amount: 123456
# Minimum number of notes required:
# 2000 = 61
# 500 = 2
# 200 = 2
# 50 = 1
# 5 = 1
# 1 = 1