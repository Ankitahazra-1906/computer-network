n=input("enter the first number: ")
m=input("enter the second number: ")
s=bin(int(int(n,2)/int(m,2))).replace("0b","")
print("The result is: ",s)