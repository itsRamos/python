square = lambda num: num**2

if __name__ == '__main__':
    print(square(3))

    mynums = [1,2,3,4,5,6]
    print(list(map(lambda num:num**2,mynums)))

    print(list(filter(lambda num: num%2 == 0, mynums)))

    names = ['Andy','Eve','Sally']
    print(list(map(lambda reverse:reverse[::-1],names)))
