'''
A school decided to replace desks in three classrooms. Each desk sits two students. Given the no. of
students in each class, print the smallest possible number of desk that can be purchased.
'''


student1 = int(input("Enter the no. of students in first class: "))
student2 = int(input("Enter the no. of students in second class: "))
student3 = int(input("Enter the no. of students in third class: "))

number_of_desk1 = student1//2
number_of_desk2 = student2//2
number_of_desk3 = student3//2

print(f"{number of desk1} desks are needed for the first class. ")
print("{} desks are needed for the second class." .format(number_of_desk2))
print("%s desks are needed for the third class." %(number_of_desk3))

remaining_desk1 = student1 % 2
remaining_desk2 = student2 % 2
remaining_desk3 = student3 % 2

print(f"{remaining_desk1} desks are remained from first class")
print(f"{remaining_desk2} desks are remained from second class")
print(f"{remaining_desk3} desks are remained from third class")

total_desk_purchase = number_of_desk1+ number_of_desk2 + number_of_desk3 + remaining_desk1 + remaining_desk2 + remaining_desk3

print(f"{total_desk_purchase} desks should be purchased for total classes")
