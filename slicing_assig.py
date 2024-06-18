# Retrieve 'hoK' from the following tuple using indexing and slicing
t = ([30, 'hi', (4, {'names': ['Kohli', 'Sunil'], 'Ages': (45, 47)})])
print(t[2][1]['names'][0][-3::-1])

# WAP to retrieve ' OE' in reverse order using the positive indexing from following string
s1 = 'I LOVE PYTHON Java'
print(s1[5:2:-2])

# WAP to extract 'Bengaluru' in reverse order using negative indexing from following string
s2 = 'Hello I am going to Bengaluru How are you doing?'
print(s2[-28:-19:1])

# WAP to print the complete string in 7 ways using the slicing. String is given below
s3 = 'Program'
print('1: ', s3[::])
print('2: ', s3[0::])
print('3: ', s3[:8:])
print('4: ', s3[:8:1])
print('5: ', s3[0:8:])
print('6: ', s3[0:8:1])
print('6: ', s3[-7::1])

# WAP to retrieve the 'Iam' from following string using slicing
s4 = 'I ama jam'
print(s4[0::4])

"""
WAP to retrieve 'Python' in reverse order using negative indexing.
You should use Indexing and slicing Together. Please use below list.
"""
l1 = [1, 7.3, [33, 22], 'Hello Python']
print(l1[3][-1:-7:-1])

"""
WAP to retrieve Jayansh and Shanvika ages in reverse order using positive indexing.
Output should be [7,4].
Please use below dictionary.
"""
students_info = {'student_names': ['Anil', 'Jayansh', 'Shanvika'], 'ages': [19, 4, 7],
                 'roll_nos': (201, 202, 205), 'classes': ['Intermediate', 'UKG', '2nd Grade'],
                 'sections': ['A', 'E', 'G'], 'percentages': [65.6, 78.9, 99.1]
                 }
print(students_info['ages'][2:0:-1])

"""
WAP to retrieve (4,5) using positive indexing.
You should use Indexing and slicing Together.
Please use below list.
"""
l2 = [21, ['hi', 'hello', (3, 4, 5)], 45, 765, 2001, 51, 2034, 'Jai']
print(l2[1][2][1::])

"""
Retrieve the value 2 using indexing and slicing using positive indexing.
Please use below list.
Write down the differences.
"""
l3 = [1, 2, 3]
print(l3[1])
print(l3[1:2:1])
"""
/**** Insexing ****/
 1.In Indexing we give only one index that releated to that value
 2.Only access that index releated value
"""
"""
 /**** Slicing ****/
 1.In Slicing we give [Start_Index:End_Index:Step_Index] to access that value
 2.Access values from staring index to end of the the Index value in Slicing and
   Stepping the index by using Step_index 
"""
