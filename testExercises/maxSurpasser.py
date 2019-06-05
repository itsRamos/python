#Function to get a surpasser list
def surpasser_list(number_list):
    n = len(number_list)
    surpasser_list = []

    for i in range(n):
        count = 0

        for j in range(i + 1, n):
            if(number_list[j] > number_list[i]):
                count += 1
            
        surpasser_list.append(count)

    # return surpasser_list
    return surpasser_list


# Function to get a max surpasser from a list
def get_max_surpasser(number_list):
    surpassers = surpasser_list(number_list)
    max_surpasser = max(surpassers)
    max_surpasser_index = surpassers.index(max_surpasser)
    return number_list[max_surpasser_index]


def main():
    numbers = [10,3,2,5,7]
    
    # Print an array of surpassers for a number list
    surpassers = surpasser_list(numbers)
    print("Surpassers in {} are {}".format(numbers,surpassers))

    # Print the first max surpasser found in the numebr list
    max_surpasser = get_max_surpasser(numbers)
    print("Max surpasser in {} is {}".format(numbers, max_surpasser))


if __name__ == '__main__':
    main()
