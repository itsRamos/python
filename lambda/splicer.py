def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

if __name__ == '__main__':
    names = ['Andy','Eve','Sally']
    
    # Functions in the map function do not need to be written with parenthesis
    print(list(map(splicer,names)))
