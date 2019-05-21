def check_even(num):
    return num%2 == 0

if __name__ == '__main__':
    mynums = [1,2,3,4,5,6]

    print(filter(check_even, mynums))

    print(list(filter(check_even,mynums)))
