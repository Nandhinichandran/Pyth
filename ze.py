dig=int(input("Enter the number:"))
sum=0
while(dig>0):
    x=dig%10
    sum=sum+x
    dig=dig//10
print(sum)
