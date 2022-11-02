#Classes

class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4
    
    def speak(self):
        print(self.name + ' says: Bark!')

my_dog = Dog('Rover')
another_dog = Dog('Fluffy')

my_dog.speak()
another_dog.speak()
