#Write a program to find the greatest of four numbers entered by the user.
n1=int(input("enter your number "))
n2=int(input("enter your number "))
n3=int(input("enter your number "))
n4=int(input("enter your number "))
if(n1>n2 and n1>n3 and n1>n4):
  print(f"greatest number is {n1} ")
elif(n2>n1 and n2>n3 and n2>n4):
  print(f"greatest number is {n2}")
elif(n3>n1 and n3>n2 and n3>n4):
  print(f"greatest number is {n3}")
else:
  print(f"greatestnumber is {n4}")