# A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
message=input("enter your message")
if("make a money"in message):
  print("this message is a spam ")
elif("buy now"in message):
  print("this message is a spam ")
elif("subscribe now"in message):
  print("this message is a spam ")
elif("click this"in message):
  print("this message is a spam ")
else:
  print("this message is not spam ")