class Mammals:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        print(f"{self.name} moves in a generic way.")

class Bird(Mammals):
    def move(self):
        print(f"{self.name} flies through the air! 🦅")


class Snake(Mammals):
    def move(self):
        print(f"{self.name} slithers across the ground! 🐍")


class Dog(Mammals):
    def move(self):
        print(f"{self.name} runs on four legs! 🐕")


# Example usage
if __name__ == "__main__":
    print("=== Mammals  ===")
    
    Mammals = [
        Bird("Eagle"),
        Snake("Viper"),
        Dog("Rex")
    ]
    
    for animal in Mammals:
        animal.move()
        
