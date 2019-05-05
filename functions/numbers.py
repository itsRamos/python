# Function to convert any given number to hex or binary
def convert(numberToConvert, typeOfConversion):
    if typeOfConversion == 'b':
        convertedNumber = bin(numberToConvert)
        finalValue = "{} in Binary is {}".format(numberToConvert, convertedNumber)
        return finalValue

    elif typeOfConversion == 'h':
        convertedNumber = hex(numberToConvert)
        finalValue = "Hexadecimal: " + convertedNumber
        finalValue = "{} in Hexadecimal is {}".format(numberToConvert, convertedNumber)
        return finalValue
    
    else:
        print ("Unsupported conversion")

# Function to round any number to the specified decimal places
def round_number(number_to_round, decimal_places):
    if (decimal_places > 10):
        print ("Function can only round to 10 decimal places")
    else:    
        rounded_number = round(number_to_round, decimal_places)
        finalValue = "{} rounded to {} decimal places is {}".format(number_to_round, decimal_places, rounded_number)
        return finalValue


def main():
    # number conversion to binary and hex
    number = 1024
    binaryConversion = convert(number, 'h')
    print (binaryConversion)

    hexConversion = convert(number, 'b')
    print (hexConversion)

    # rounding numbers to specified decimal places
    number_to_round = 3.14159265359
    two_decimals = 2
    rounded_to_2 = round_number(number_to_round, two_decimals)
    print (rounded_to_2)
    four_decimals = 4
    rounded_to_4 = round_number(number_to_round, four_decimals)
    print (rounded_to_4)

if __name__ == '__main__':
    main()
