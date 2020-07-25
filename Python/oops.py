'''
class Dog():

    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


myDog = Dog("Lab", "Bruno")
print(myDog.breed)
print(myDog.name)
print(myDog.species)
'''

'''
class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


myc = Circle(3)
myc.set_radius(100)
print(myc.area())
'''

# INHERITANCE


class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print('EATING')


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")


myAnimal = Dog()
myAnimal.whoAmI()
myAnimal.eat()
