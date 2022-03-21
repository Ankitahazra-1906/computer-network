a=input("Enter the input signal to be communicated: ")
b=input("Enter the input of noise vector in the channel of communication: ")
d=int(a,2)
e=int(b,2)
c=d^e
#print(c)
i=bin(c).replace('0b','')
print("\n The communicating signal in the communication channel: ",i)
f=c^e
#print(f)
j=bin(f).replace('0b','')
print("\n The communicated message received by the receiver: ",j)