class Person:
    name = 'jenan'
    age  =17

    def is_adult(self):
        if self.age > 18:
            print("You have too much responsibilities")
        else:
            print("Lucky")

person1 = Person()
print(f"this is {person1.name} and she is {person1.age} years old")
person1.is_adult()

# PART 3
class Person2:
    def __init__(self, name, age,hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies
    

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old , she likes {self.hobbies[0]}, {self.hobbies[1]} and {self.hobbies[2]}"

hobby = ["coding", "editing","baking"] #bonus
person22 = Person2("sarah", 19, hobby)
print(person22)