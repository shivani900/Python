# Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
n1=int(input("enter your marks "))
n2=int(input("enter your marks "))
n3=int(input("enter your marks "))
total_marks=n1+n2+n3
percentage=total_marks/3
if(percentage>40 and n1>33 and n2>33 and n3>33):
  print("pass")
else:
  print("fail")
