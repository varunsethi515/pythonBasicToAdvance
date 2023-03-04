average=0
addition=0
multiplication=1
list_sample=[1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1]
for x in list_sample:
    addition=addition+x;
    multiplication=multiplication*x;
    average=addition/len(list_sample)
print("The average of all the {} elements present in the list is {}:".format(len(list_sample),average))
print("The multiplication of all the {} elements present in the list is {}:".format(len(list_sample),multiplication))
