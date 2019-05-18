n=int(input("Enter the number: "))
order=len(str(n))
sum=0
temp=n
while temp>0:
    a=temp%10
    sum+=a**order
    temp//=10
if n==sum:
    print(n,"is an armstrong number.")
else:
    print(n,"is not an armstrong number.")
