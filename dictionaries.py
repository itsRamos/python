d = {'k1':1, 'k2':2}
# print (d)

# Dictionary comprehension
new_d = {x:x**2 for x in range(10)}
print (new_d)

# dict comprehension using zip
zipd = {k:v**2 for k,v in zip(['a','b', 'c'], range(5))}
print (zipd)

# method to print items individually 
for k in d.iteritems():
    print (k)

for k in d.itervalues():
    print (k)

for k in d.iterkeys():
    print (k)

# similarly you can use specific functions
d.viewitems()
d.viewvalues()
