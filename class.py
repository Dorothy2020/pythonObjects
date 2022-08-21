# Create a class named Person, use the __init__() function to assign values for name and age:


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Dorothy",22)

print(p1.name)
print(p1.age)

# Insert a function that prints a greeting, and execute it on the p1 object:
class Greeting:
    def __init__(self,name,age):
        self.name=name
        self.age=name

    def myfunc(self):
        print("Hello my name is" + " ", self.name  )
p1=Greeting("Ann",23)

p1.myfunc()




