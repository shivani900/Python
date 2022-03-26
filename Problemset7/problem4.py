# Write a program to find whether a given number is prime or not.


n1=int(input("enter your number"))
for i in range(2,n1):
  if(n1%i==0):
    print("not prime")
    break
else:
  print("prime")