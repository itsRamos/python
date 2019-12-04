import random

def main():
    smaller = int(input("Enter the smaller number: "))
    larger = int(input("Enter the larger number: "))
    myNumber = random.randint(smaller, larger)
    count=0
    while True:
        count+=1
        userNumber=int(input("Enter a guess: "))
        if userNumber < myNumber:
            print("Too Small")
        elif userNumber > myNumber:
            print("Too big")
        else:
            print("Got it in ", count, " tries!")
            break

if __name__ == "__main__":
    main()