a=input("Enter the sequence: ")
b=list(a)
count=0
for i in range(0,4):
    if(b[i]!='1'):
        print('invalid')
        exit()
#Bit Stuffing
for i in range(5,len(b)):
    if(b[i]=='1'):
        count=count+1
        if(count==5):
            b.insert(i+1,'0')
    else:
        count=0
print(b)
x="".join(map(str,b))
#Bit Destuffing
for i in range(5,len(b)-1):
    if(b[i]=='1'):
        count=count+1
        if(count==5):
            b.pop(i+1)
    else:
        count=0
print(b)
y="".join(map(str,b))
print("Bit stuffing: ",x)
print("Bit destuffing: ",y)
