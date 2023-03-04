num=int(input("Enter the number yhose factorial you want to calculate:"))
fact=1
for x in range(1,num+1):
    fact=fact*x
print("The factorial of {} is {}:".format(num,fact))
    
