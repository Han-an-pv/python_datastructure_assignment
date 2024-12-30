#list

#1. Create a list of 5 random numbers and print the list.

import random
list=random.sample(range(100,500),5)
print(list,type(list))

#2. Insert 3 new values to the list and print the updated list.

list.extend([201,303,404])
print(list)

# 3. Try to use a for loop to print each element in the list.
for element in list:
    print(element)

#dictionary

# 1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.

dictionary={'name':'john','age':'25','address':'New York'}
print(dictionary)

# 2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'

dictionary.update({'phone':'1234567890'})
print(dictionary)

#set
# 1.Create a set with values 1, 2, 3, 4, and 5.

set={1,2,3,4,5}
print(set)

# 2. Add the value 6 to the set created in Q1.

set.add(6)
print(set)

# 3. Remove the value 3 from the set created in Q1.
set.remove(3)
print(set)

#tuple

# 1. Create a tuple with values 1, 2, 3, and 4
tuple = (1,2,3,4)
print(tuple,type(tuple))

# 2. Print the length of the tuple created in Q1.

print(len(tuple))
