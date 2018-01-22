n=int(input("Enter the number:"))
temp=n
r=0
sum=0
while(temp>0):
    r=temp%10
    sum+=r**3
    temp=temp//10
if(n==sum):
    print("Yes")
else:
    print("No")
    
