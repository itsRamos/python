# use the append method to add values to the
l = [1,2,3]
l.append(4)
print(l)

# use the count method to count the number of items in a list
print(l.count(10))
print(l.count(1))

# append will add a list to the list itself
x = [1,2,3]
x.append([4,5])
print (x)

# extend will the values as part of the list
x1 = [1,2,3]
x1.extend([4,5])
print (x1)

# use the index method to find the index of a given value
print (l.index(2))


#use the inser method to place an object at the index applied
l.insert(2,'inserted')
print(l)

# use the pop method to grab the popped item 
popped = l.pop()
print (popped)
print (l)

# add an index to pop to grab the value at that index
pop_index = l.pop(0)
print (pop_index)
print(l)

# use remove to get rid of the first ocurrence of a value
l.remove('inserted')
print(l)

# use the reverse method to reverse a list
r = [1,2,3,4,5,6]
r.reverse()
print (r)

# use the sort method to sor the list in place
r.sort()
print (r)
