class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
         print(f'{self.name} is {self.age} years old and {self.color} in color')
         print(f'{my_cat.name} is {my_cat.age} years old and {my_cat.color} in color')
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print("meow")

my_cat = Cat("fluffy", 6, "black")

print(my_cat.name)
print(my_cat.age)
print(my_cat.color)
my_cat.speak()
my_cat.intro()