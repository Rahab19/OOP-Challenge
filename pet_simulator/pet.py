class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap.")

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played with you.")

    def get_status(self):
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    def train(self, trick):
        if trick in self.tricks:
            print(f"{self.name} already knows {trick}.")
        else:
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1)
            print(f"{self.name} learned {trick}!")

    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} knows no tricks.")
        else:
            print(f"{self.name} knows: {', '.join(self.tricks)}")
