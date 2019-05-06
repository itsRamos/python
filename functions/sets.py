# Function to check elements in set1 that are not in set2
def elements_that_are_not(set1, set2):
    different_elements = set1.difference(set2)
    return different_elements

# Function to check elements in either set
def elements_in_either(set1, set2):
    same_elements = set1.union(set2)
    return same_elements

def main():
    # Sets to test on
    set1 = {2,3,1,5,6,8}
    set2 = {3,1,7,5,6,8}

    # Finding the elements in set1 that are not in set2
    difference = elements_that_are_not(set1, set2)
    print (difference)

    # Finding elements that are in either set
    same = elements_in_either(set1, set2)
    print (same)

if __name__ == '__main__':
    main()
