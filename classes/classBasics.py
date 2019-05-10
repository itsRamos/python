# Basic class of a dog
class Dog():

    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = "mammal"

    def __init__(self, breed, name):
        
        # Attributes
        # Assign using self.attribute_name
        self.breed = breed
        self.name = name

    #OPERATIONS/Actions ---> Method
    def bark(self, number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))

   
# my_dog = Dog("Lab", "Frankie")

# # Command to see the type of Dog
# print(type(Dog))

# my_dog.bark(14)



# Basic class of a cirlce
class Circle():

    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * self.pi

    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2

# my_circle = Circle()
# print(my_circle.pi)
# print(my_circle.radius)
# print(my_circle.area)
# print(my_circle.get_circumference())


# Example of a derived Dog class from Animal class
class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am a dog")

    def eat(self):
        print("I am a dog and eating")

    def bark(self):
        print("WOOF!")

# my_animal = Animal()
# my_dog = Dog()
# my_dog.eat()
# my_dog.who_am_i()
    
    
# Example of two classes with similar methods
class Dog():
    
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + " says meow!"

def pet_speak(pet):
    print(pet.speak())

# fido = Dog("fido")
# isis = Cat("isis")



# Example of an abstract class
class Animal():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")



class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):

    def speak(self):
        return self.name + " says meow!"

# my_animal = Animal('fred')
# my_animal.speak()

# niko = Dog("Niko")
# felix = Cat("Felix")

# print(niko.speak())
# print(felix.speak())

# for pet in [niko,felix]:
#     print(type(pet))
#     print(pet.speak())

# pet_speak(niko)
# pet_speak(felix)
    


# Example of magic methods for length, delete and str
class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")
        
# b = Book('Python rocks', 'Jose', 200)
# print(b)
# print(str(b))
# print(len(b))



if __name__ == '__main__':
  pass




   
