# Function to reverse a list by copying it first
def reverse_list_copy(lst):
    new_lst = lst.copy()
    new_lst.reverse() 
    return new_lst 

# Function to reverse a list by using reversed
def reverse_list(lst):
    reversed(lst)
    return lst

# Function to sort a list
def sort_list(lst):
    print(lst)
    new_list = lst.copy()
    print (new_list)
    new_list.sort()
    print (new_list)
    return new_list

def main():
    # list to test on
    lst = [1,2,3,4]

    # Reversing by using a copy
    reverse = reverse_list_copy(lst)
    print ("{} reversed is {}".format(lst,reverse))

    # Reversing by using reversed
    reversed_list = reverse_list(lst)
    print ("{} reversed is {}".format(lst,reversed_list))

    # Sorting a list
    unsorted_list = [5,4,3,2,1]
    sorted_list = sort_list(unsorted_list)
    print(sorted_list)

if __name__ == '__main__':
    main()
