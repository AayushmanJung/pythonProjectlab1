# A school decided to replace the desks in three classrooms. Each desks sits two students. Given the number of students in each class, Print the smallest possible number of desks that can be purchased. The program should read three integers: the number of students in each of three classes a,b and c respectively. In the first test there are three groups. The first group has 20 students and thus need 10 desks. The second student has 21 students , so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So we need 32 desks in totoal.

no_student_class1 = int(input("Enter the number of student in first class : "))
no_student_class2 = int(input("Enter the number of student in second class : "))
no_student_class3 = int(input("Enter the number of student in third class : "))

desk_class1 = (no_student_class1 //2)
print(f"The required number of desk for first class is {desk_class1} ")
desk_class2 = (no_student_class2 //2)
print(f"The required number of desk for second class is {desk_class2} ")
desk_class3 = (no_student_class3 //2)
print(f"The required number of desk for third class is {desk_class3} ")
