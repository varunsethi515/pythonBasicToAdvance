age = 20
def variable_global_and_local():
    print("We can access the global variable inside the function only with the help of 'globus() method'")
    print("Initial global variable is :", globals()['age'])
    print("We can also modify the global variable with the help of globus() method")
    globals()['age']=21
    print("After updating the value of global variable the global variable comes out to be",globals()['age'])
    print("Now declearing the local variable inside the function itself")
    age = 22
    print("Local variable",age)
variable_global_and_local()
print("age",age)
