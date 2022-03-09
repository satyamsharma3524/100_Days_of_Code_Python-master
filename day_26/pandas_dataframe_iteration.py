import pandas

student_dict = {
    "student": ['satyam', 'roshni', 'meera'],
    "scores": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
print(student_df)

# loop though rows of dataframe
for (index, row) in student_df.iterrows():
    print(row.student)
    if row.student == "satyam":
        print(row.scores)
