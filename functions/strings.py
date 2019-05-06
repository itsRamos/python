# Function to check if a given string contains all lowercase
def check_lowercase(str):
    lowercase_string = str.islower()
    
    if lowercase_string:
        print ("'{}' contains all lowercase".format(str))
        return lowercase_string
    else:
        print ("Not all characters in '{}' are lowercase".format(str))
        return lowercase_string

# Function to check the frequency of a given letter in a string
def frequency_of_letter(string, letter):
    frequency = string.count(letter)
    finalValue = "'{}' contains the letter '{}' {} times".format(string, letter, frequency)
    return finalValue

def main():
    # Check if strings are all lowercase
    string_to_check = "hello how are you Ramos, are you feeling okay?"
    check_lowercase(string_to_check)

    another_string_to_check = 'hello this contains all lowercase'
    check_lowercase(another_string_to_check)

    # Check the frequency of letter 'a'
    letter_to_check = 'o'
    frequency = frequency_of_letter(string_to_check,letter_to_check)
    print(frequency)

if __name__ == '__main__':
    main()
