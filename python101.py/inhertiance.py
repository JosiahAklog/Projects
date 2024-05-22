class Mammal:
    def walk(self):
        print("walk")
    
    
class Dog(Mammal):
     def bark (self):
        print("Bark")
    
    
    
class Cat(Mammal):
    def meow(self):
        print("meow")
    
cat1 = Cat()
cat1.meow()