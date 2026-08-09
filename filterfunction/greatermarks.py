Students = {"ram": 50, "shyam": 30, "sita": 60, "geeta": 45, "hari": 35}

PassedStd = dict(filter(lambda student: student[1] > 40, Students.items()))

print("Passed Students:", PassedStd)

 