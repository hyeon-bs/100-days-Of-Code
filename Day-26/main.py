student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value) 

import pandas

student_dict_frame = pandas.DataFrame(student_dict)
print(student_dict_frame)

# # Loop through a data frame
# for (key, value) in student_dict_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_dict_frame.iterrows():
    if row.student == "Anglea":
        print(row.score)

# {new_key:new_value for (index, row) in df.iterrows()}