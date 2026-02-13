# Total Salary Calculation
# WAP to calculate total salary of employee based on basic, 
# da=10% of basic, 
# ta=12% of basic, 
# hra=15% of basic.

basic = float(input("Enter basic salary: "))
da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

print("DA =", da)
print("TA =", ta)
print("HRA =", hra)

total_salary = basic + da + ta + hra

print("Total Salary =", total_salary)

# Output:
# Enter basic salary: 50000
# Total Salary =  68500.0

