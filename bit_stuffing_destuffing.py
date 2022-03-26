a=input("Enter the sequence: ")
flag=[1,1,1,1,1]
z="".join(map(str,flag))
print("Flag: ",z)
b=list(a)
d=[]
count=0
e=0

#Bit Stuffing
for i in range(0,len(b)):
    if(b[i]=='1'):
        count=count+1
        if(count==5):
            b.insert(i+1,'0')
            d.append(i+1)
            e+=1
    else:
        count=0
print(b)
x="".join(map(str,b))

#Bit Destuffing
for i in range(0,len(b)-4):
    if(b[i]=='1'):
        count=count+1
        if(count==5):
            b.pop(i+1)
    else:
        count=0
print(b)
y="".join(map(str,b))

p=(str(z)+str(x))
q=(str(z)+str(y))
print("The index where the bits are stuffed: ",d)
print("The no. of bits are stuffed: ",e)
print("Bit stuffing frame: ",p)
print("Bit destuffing frame: ",q)


