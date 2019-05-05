# Practice exercises
# 1. Convert 1024 to binary and hex
num = bin(1024)
print (num)
num2 = hex(1024)
print (num2)

# 2. Round 5.23222 to two decimal places
num3 = 5.23222
rounded = round(5.23222,2)
print (rounded)

# 3. Check is every letter in the string is lower case
s = 'hello how are you Mary, are you feeling okay?'
is_lower_case = s.islower()
# if is_lower_case == True:
if is_lower_case:
    print ("String is all lowercase")
else:
    print ("string contains chars that are not lowercase")

# 4. How many times does letter 'w' show up in the string
s1 = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
w = s1.count('w')
print(w)

# 5. Find the element in set1 that are not in set2
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
found = set1.difference(set2)
print (found)

# 6. Find all elements that are in either set
# WRONG
# in_either = set1.intersection(set2)
# print(in_either)
# RIGHT
in_either = set1.union(set2)
print (in_either)

# 7. Create this dictionary {0:1, 1:1, 2:8, 3:27, 4:64} using dict comprehension
# WRONG
# new_dict = {x, x.pow(3) for i in range(4)}
# print (new_dict)

# RIGHT
new_dict = {x:x**3 for x in range(5)}
print (new_dict)

# 8. Reverse the list below
l = [1,2,3,4]
l.reverse()
print (l)

# 9. Sort the list below
l1 = [3,4,2,5,1]
l1.sort()
print (l1)

other_Way = sorted(l1)
print(other_Way)

# Remove all duplicates from the string below
# sr = "abcdabcdaer"
sr = "aaabbbcccddd"
nsr = "".join(set(sr))
print (nsr)

# Remove all dups in order
from collections import OrderedDict
sr1 = "aaabbbcccddd"
nsr1 = "".join(OrderedDict.fromkeys(sr1))
print (nsr1)
