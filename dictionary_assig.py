"""
Assignment-1:
WAP to create a one student info in dictionary. Dictionary should contain
'student_name, age, roll_no, class, section, percentage, college_name' student data.
Retrieve the student percentage from the dictionary.
"""
student_info = {'student_name': 'Vasu', 'age': 23, 'roll_no': 205,
                'class': 'EEE', 'section': 'A', 'percentage': 62.89,
                'college_name': 'D.N.R College of Engg & Tech'}
print(student_info['percentage'])

"""
Assignment-2:
WAP to create a 3 students info in dictionary. Dictionary should contain 3 students data with 'student_names,
ages, roll_nos, classes, sections, percentages, university_names' keys and values can be stored in list/tuple.
Retrieve the student_3 class from the dictionary.
"""
students_info = {
    'student_names': ('Vasu', 'Sai', 'Tejas'),
    'ages': [23, 22, 23],
    'roll_nos': (205, 102, 303),
    'classes': ('EEE', 'ECE', 'ETC'),
    'sections': ('A', 'B', 'C'),
    'percentages': (62.89, 61.32, 81.20),
    'university_names': ('JNTUK', 'JNTUK', 'AMRAVATI UNIVERSITY ')
}
print(students_info['classes'][2])

"""
Assignment-3:
WAP to create a 4 employees data in a nested dictionary.
Dictionary should contain 4 employees data, each employee data should be represented in a dictionary
Each sub dictionary should have 'employee_name,salary,Designation' keys.
Retrieve the 3rd employee designation from the nested dictionary.
"""
employee = {
    'emp1': {'name': 'Vasu', 'salary': 10000, 'designation': 'trainee-1'},
    'emp2': {'name': 'Sai', 'salary': 20000, 'designation': 'trainee-2'},
    'emp3': {'name': 'Pavan', 'salary': 30000, 'designation': 'trainee-3'},
    'emp4': {'name': 'Tejas', 'salary': 20000, 'designation': 'trainee-4'}
}
print(employee['emp3']['designation'])
