grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sred_ball = {}
students_ = list(students)
students_.sort()
grades_sr = [sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),
             sum(grades[3])/len(grades[3]),sum(grades[4])/len(grades[4])]
sred_ball [students_[0]] = grades_sr[0]
sred_ball [students_[1]] = grades_sr[1]
sred_ball [students_[2]] = grades_sr[2]
sred_ball [students_[3]] = grades_sr[3]
sred_ball [students_[4]] = grades_sr[4]
print(sred_ball)
