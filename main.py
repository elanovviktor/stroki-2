grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
def average(grades): return sum (grades) / len(grades)
result = {}
for students, grades_list in zip(sorted(students), grades) :
    result [students] = average(grades_list)
print(result)