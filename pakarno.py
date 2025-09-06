student_list = [ {"name":'A', "num": 5 },
        {"name": 'B', "num": 6},
        {"name": 'C', "num": 7},
        {"name": 'D', "num": 2},
        {"name": 'E', "num": 10},
        {"name": 'F', "num": 8},
        {"name": 'G', "num": 4},
        {"name": 'H', "num": 3},
        {"name": 'I', "num": 7},
        {"name": 'J', "num": 1},
        {"name": 'K', "num": 10},
        {"name": 'L', "num": 9}
        ]

sum_lst = 0
for e in student_list:
    sum_lst += e["num"]
rata2 = sum_lst / len(lst)

dibawah_rata_lst = [ student  for student in student_list if student["num"] < rata2 ]
lulus = [ student  for student in student_list if student["num"] >= rata2 ]

print(dibawah_rata_lst)
print("Dibawah rata2")
for s in dibawah_rata_lst:
    print(s["name"])

print("Lulus")
for s in lulus:
    print(s["name"])
