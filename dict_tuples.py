
# Dictionary is a key value pair
# Dictionary uses key to access the value. List uses index to access elements of a list
d = {"tom":98888899,"joe":98756423,"Bob":243234224}
print(d["tom"])

#adding a value to a dictionary
d["sam"] = 222223333444
print(d)

#deleting an entry from a dictionary
del d["sam"]
print(d)

#accessing values in the dictionary recursively using a for loop
for key in d:
    print("Key:",key,"Value:", d[key])

#accessing values in the dictionary recursively using a for loop - method 2
for k,v in d.items():
    print("Key:",k,"Value:", v)

# check if a key is present in a dictionary
print("tom" in d) # returns true because tom is present
print("raj" in d) # returns False because raj is not present

# remove all the items in the dictionary
d.clear()
print(d)

#---------------------------------------------------------------------------------------------
# Tuple is a list of values grouped together
# In List all the values have the same meaning (Homogeneous values). Example - Groceries List
# In Tuple All values have heterogeneous meaning. Example - Address. 
point = (5,9) #5 is X-Coordinate and 9 is Y-Coordinate
print(point[0]) # access tuple values using index
print(point[1])
print(point)

#Tuple is immutable. you cant change the value of an index in a tuple.
point[0] = 50 # Results in an error.