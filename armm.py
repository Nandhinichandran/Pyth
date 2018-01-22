n1=int(input("Enter the 1st number:"))
n2=int(input("Enter the 2nd number:"))
for i in range(n1,n2):
    temp=i
    r=0
    sum=0
    while(temp>0):
        r=temp%10
        sum+=r**3
        temp=temp//10
    if(i==sum):
        print(i)
    
