# Attempt problem 1 using a while loop.
li=["shivani","shipra","neha","priyanka","monika"]
a="good morning"
q=0
while(q<len(li)):
  if(li[q][0]=="s"):
   print(a+li[q])
  q=q+1