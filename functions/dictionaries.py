# Function to use dictionary comprehension
def dictionary_comprehension():
    new_dict = {x:x**3 for x in range(10)}
    return new_dict

# Function to use dictionary comprehension and zip
def dictionary_comprehension_zip():
    new_dict = {x:y**3 for x,y in zip(['a','b','c'], range(5))}
    return new_dict

def main():
    # Building a dictionary using dictionary comprehension
    dict_compr = dictionary_comprehension()
    print (dict_compr)

    # Building a dictionary using dictionary comprehension and zip
    dict_zip = dictionary_comprehension_zip()
    print (dict_zip)

if __name__ == "__main__":
    main()
