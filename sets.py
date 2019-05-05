# Advanced Sets
# create the set first and then modify it with add
s = set()

s.add(1)
s.add(3)

# add method will only add one ocurrence of the char
s.add(2)
s.add(2)

# only one 2 will be added to the set
print (s)

# copying a set
s = {1,2,3}
sc = s.copy()
print (sc)

# any changes to the current set will not affect the copy
s.add(4)
print(s)
print(sc)

# method to check the difference between sets
print (s.difference(sc))

# method to remove all characters that are repeats
s1 = {1,2,3}
s2 = {1,4,5}

s1.difference_update(s2)
print(s1)

# method to discard any given characters
sd = {1,2,3,4,5}
sd.discard(2)
print(sd)

# method to check for intersections or repeats
sint = {1,2,3}
sint2 = {1,2,4}
print (sint.intersection(sint2))

# method to update a set with any repeats
sint3 = {1,2,3}
sint4 = {1,2,4}
print (sint3.intersection_update(sint4))
