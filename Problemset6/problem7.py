p1=input("enter your post ").lower()
name=input("enter your name ").lower()
if(name in p1):
  print(f"{name} is present in post: {p1}")
else:
  print(f"{name} is not present in post: {p1}")
      