age= float(input("Enter Your age:"))


# age >= 18 and age <= 60
# 0–12    → Child
# 13–19   → Teenager
# 20–59   → Adult
# 60+     → Senior

if age >= 0 and age <=12:
    print("Child")
elif age >=13 and age <=19:
    print("Teenager")
elif age >=20 and age <= 59:
    print("Adult")
else:
    print("Senior")