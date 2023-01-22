my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# creating a temperary list to hold the unique elements and it will be used to check the duplicate elements
temp_list = []
for elm in my_list:
    if elm not in temp_list:
        temp_list.append(elm)
my_list = temp_list
print("The list with unique elements only:")
print(my_list)