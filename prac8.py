class Animal:
    def __init_(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")


class Dog(Animal):
    def speak(self):
        print("Bow!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


# Create objects
animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on each object
animal.speak()
dog.speak()
cat.speak()



