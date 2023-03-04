# Some additional methods over Dictionary are keys() values() and get()

dictionary={1:"one",2:"Two",3:"Three"}
print("All the keys present in the dictionary")
for x in dictionary.keys():
    print(x)
print("All the values present in the dictionary")
for x in dictionary.values():
    print(x)
print("Fetch the value presnt at particular key")
print("The value present at key 1 is:"(dictionary.get(1)))
