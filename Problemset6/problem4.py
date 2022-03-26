# Write a program to find whether a given username contains less than 10 characters or not.
name=input("enter your username")
if(len(name) <10):
  print("true if the user_name contain less than 10 character")
else:
  print("false if the user_name contain more than 10 character")