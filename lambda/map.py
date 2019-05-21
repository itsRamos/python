def square(num):
    return num*2


if __name__ == '__main__':

    my_nums = [1,2,3,4,5]

    # pro way
    for item in map(square,my_nums):
        print (item)

    # practical way
    print (list(map(square,my_nums)))


    # Logical way
    for i in range(len(my_nums)):
        square_number = square(my_nums[i])
        print(square_number)
