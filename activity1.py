class Superhero:
    def __init__(self, name, secret_identity, power_level):
        self.name = name
        self._secret_identity = secret_identity  # Protected attribute
        self.__power_level = power_level        # Private attribute
        
    def introduce(self):
        print(f"I am {self.name}! (Secret identity: {self._secret_identity})")
        
    def use_power(self):
        print(f"{self.name} uses a generic superhero power!")
        
    def get_power_level(self):
        return self.__power_level
        
    def set_power_level(self, new_level):
        if new_level >= 0:
            self.__power_level = new_level
        else:
            print("Power level cannot be negative!")
            
    def __str__(self):
        return f"Superhero: {self.name} [Power: {self.__power_level}]"


class FlyingHero(Superhero):
    def __init__(self, name, secret_identity, power_level, max_altitude):
        super().__init__(name, secret_identity, power_level)
        self.max_altitude = max_altitude
        
    def use_power(self):
        print(f"{self.name} soars through the sky at {self.max_altitude} feet!")
        
    def fly(self):
        print(f"{self.name} takes off into the air!")


class TechHero(Superhero):
    def __init__(self, name, secret_identity, power_level, gadget_count):
        super().__init__(name, secret_identity, power_level)
        self.gadget_count = gadget_count
        
    def use_power(self):
        print(f"{self.name} deploys one of their {self.gadget_count} high-tech gadgets!")
        
    def invent(self):
        print(f"{self.name} creates a new gadget!")
        self.gadget_count += 1


# Example usage
if __name__ == "__main__":
    print("=== Superhero Class ===")
    
    superman = FlyingHero("Superman", "Clark Kent", 95, 40000)
    batman = TechHero("Batman", "Bruce Wayne", 85, 12)
    
    superman.introduce()
    superman.use_power()
    superman.fly()
    
    print("\n")
    
    batman.introduce()
    batman.use_power()
    batman.invent()
    
    print("\nPower levels:")
    print(f"{superman.name}: {superman.get_power_level()}")
    print(f"{batman.name}: {batman.get_power_level()}")
    
    # Demonstrating encapsulation
    try:
        print(batman.__power_level)  
    except AttributeError:
        print("\nCan't access private __power_level directly!")