a=input("Enter the bit string: ")
b=list(a)
p=int(input("Enter the postion: "))
c=input("Enter the bit you want to insert: ")
b.insert(p,c)
d="".join(map(str,b))
print(d)


