# 🐶 Exercise: Pet Class
#
# 1. Create a class called Pet with a class attribute:
#       species = "Mammal"
#
# 2. The class should have an __init__ method that accepts:
#       - name
#       - age
#       - breed
#       - owner (default = None)
#
# 3. Add a method assign_owner(owner_name) to set the owner of the pet.
#
# 4. Add a method display_info() that prints:
#       - Name
#       - Age
#       - Breed
#       - Species (class attribute)
#       - Owner
#
# Task:
# - Create at least two Pet objects.
# - Assign an owner to each.
# - Call display_info() to print their details.
#
# Bonus Challenge:
# - Create a subclass called Dog that inherits from Pet.
# - Add an extra method bark() that prints "Woof! Woof!".
# - Create a Dog object, assign an owner, and call both display_info() and bark().

class Mammal:       # Creating class
    species = "Mammal"      # Creating a default attribute

    def __init__(self, name, age, breed, owner=None):       # Creating attributes
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner if owner else None

    def assign_owner(self, owner_name):     # Creating Method 1
        self.owner = owner_name

    def display_info(self):     # Creating Method 2
        print("Name:", self.name)
        print("Age:", self.age)
        print("Breed:", self.breed)
        print("Species:", self.species)
        print("Owner:", self.owner)
        print("-"*20)

# Creating sub-classes


class Dog(Mammal):
    def __init__(self, name, age, breed, owner=None):       # Creating attributes
        super().__init__(name, age, breed, owner)

    def speak(self):
        print(f"{self.name} = Woof Woof!")
        print("-"*20)


class Cat(Mammal):
    def __init__(self, name, age, breed, owner=None):       # Creating attributes
        super().__init__(name, age, breed, owner)

    def speak(self):
        print(f"{self.name} = Maaawww Maaawww!")
        print("-"*20)


# Creating objects
pet_1 = Mammal("Gala", 1, "Dachsund")
pet_2 = Mammal("Kitchie", 1, "Persian")

# Creating objects for sub-classes
dog_1 = Dog("Gala", 1, "Dachsund", "Ronnel")
cat_1 = Cat("Kitchie", 1, "Persian", "Joana")

# Assigning owners to objects
pet_1.assign_owner("Ronnel")
pet_2.assign_owner("Joana")

# Displaying infos of pets
pet_1.display_info()
dog_1.speak()
pet_2.display_info()
cat_1.speak()
