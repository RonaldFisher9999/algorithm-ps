class Doggy :
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, breed) :
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
    
    def bark(self) :
        print(f"{self.name} barks. Bow-Wow")

    def death(self) :
        print(f"{self.name} is dead. Farewell.")
        Doggy.num_of_dogs -= 1
    
    @classmethod
    def get_status(cls) :
        print(f"living dogs : {cls.num_of_dogs}")
        print(f"all dogs : {cls.birth_of_dogs}")


# dog1 = Doggy("aaa", "x")
# dog2 = Doggy("bbb", "y")

# dog1.bark()
# dog2.bark()

# Doggy.get_status()
# dog1.get_status()
# dog2.get_status()

# dog1.death()

# Doggy.get_status()