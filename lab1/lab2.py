# Write a program that reads the length of the base and the height of a right-angled triangle and print the area. Every number is given on a seperate line.
length = int(Input("Enter the base of the length: "))
height = int(Input("Enter the height of the triangle: "))

area = (length * height)//2

print(f"The area of right angled triangle is {area} ")