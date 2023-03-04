# Anonymous Functions are the function with no name

# 1. LAMBDA FUNCTION
# Syntax lambda(attributes ; function)
def addition(a,b):
    return a+b
result = addition(5,1)
print(result, " with Normal Function")

result1 = lambda a,b:a+b
print(result1(5,1), " With Anonymous Function")

# 2. FILTER FUNCTION
# Syntax filter( function : sequence)
def even_numbers(list):
    for i in range(len(list)-1):
        if list[i]%2==0:
            print("Even",end=" ")
        else:
            print("ODD" ,end=" ")

list_sample=[1,2,3,4,5,6,7,8,9]
print(even_numbers(list_sample))

even_numbers1 = list(filter(even_numbers() , list_sample))
print(even_numbers1)

# 3. MAP FUNCTION
# Syntax list(map(function , sequence))
def update(list):
    for i in range(len(list)):
        if list[i]%2==0:
            print(list[i]*2,end=" ")
        else:
            print(list[i], end=" ")
list_sample2=[1,2,3,4,5,6,7,8,9]
print(update(list_sample2))

update2 = list(map( update , list_sample2))
print(update2)
