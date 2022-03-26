# Write a program to greet all the person names stored in a list l1 and which starts with S.
l1 = ["Harry", "Sohan", "Sachin", "Rahul"]
a= "Good afternoon "
for i in l1:
  if(i[0]=="S"):
    print(a+i)

for i in range(len(l1)):
  if(l1[i][0] == "S"):
    print(a+l1[i])
  