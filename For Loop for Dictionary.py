dictionary={1:"one",2:"two", 3:"three"}
for x in dictionary.items():
    print(x)
#output will be in form of tuple

for key,value in dictionary.items():
    print("keys",key)
    print("values",value)
#seperate key value output not in form of tuple
