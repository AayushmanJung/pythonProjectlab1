'''
WAP to take an input form the user to ask the user age. If the user's age is below 15 print a message "You are child"
If the user's age is greater than 15 and less than 40 print a message "You are adult" .If user's age is greater than 40
 print the message "You are old"
 '''
a=int(input("Enter the age: "))
if a<15:
    print('You are child')
elif a>15 and a<40:
    print('You are adult')
else:
    print('You are old')
