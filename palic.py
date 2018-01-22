n=int(input("Enter the number:"))
temp=n
rev=0
while(temp!=0):
    rev=rev*10
    rev=rev+(temp%10)
    temp=temp//10
if(n==rev):
    print("Yes")
else:
    print("No")
