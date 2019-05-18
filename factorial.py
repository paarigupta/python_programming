n=int(input("enter the number: "))
a=1
if n<1:
    print("The factorial is not possible.")
elif n==0:
    print("The factorial is ",1)
else:
    for i in range(1,n+1):
        a=a*i
print("The factorial is" ,a)

    
