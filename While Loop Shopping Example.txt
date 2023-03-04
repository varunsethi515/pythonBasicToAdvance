no_of_shop=0
no_of_items=0
total_items=0
print("Shopping !!Shopping !!Shopping !!Shopping !!Shopping !!Shopping ")
while no_of_shop <= 5:
    no_of_shop=no_of_shop+1
    no_of_items=int(input("Enter the number of items from shop{}:".format(no_of_shop)))
    total_items=total_items+no_of_items
print("Total number of items i have purchased toady for {} shops are {}".format(no_of_shop,total_items))
