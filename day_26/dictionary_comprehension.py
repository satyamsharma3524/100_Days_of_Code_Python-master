# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

import random
names = ['satyam', 'shivam', 'meera', 'roshni', 'raju', 'doraemon', 'pokemon']
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

# iterating through dictionary
passed_students = {student: scores for (student, scores) in student_scores.items() if scores > 40}
print(passed_students)