weight=0
day=0
total=0
print("Enter the weight you have lifted each day of the last week and plz dont lie")

while day <= 6:
    day=day+1
    weight=int(input("Enter the weight that you have lifter {}:".format(day)))
    total=total+weight
avg=total/day
print("The average weight that you have lifter in {} days is {} :".format(day,avg))
    
    
