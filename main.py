class Pet:
    def __init__(self, name, hunger, energy, happiness):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness

    def __repr__(self):
        return f"My pet is {self.name} with {self.hunger} hunger, {self.energy} energy, and {self.happiness} happiness."

    def eat(self):
        pass
    def sleep(self):
        pass
    def play(self):
        pass
    def play(self):
        pass
    def get_status(self):
        pass
    def train(self, trick):
        pass



Pet("Elisa")