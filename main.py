# Empty list 
my_list = []

#Appending element
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting 15 at second position
my_list.insert(1, 15)
print(my_list)

# Extend my_list with other list
other_list = [5,15,25,35]
my_list.extend(other_list)
print(my_list)

# sort my_list in ascending order
my_list.sort()
print(my_list)
print(my_list.index(30))
print(my_list)
print(len(my_list))