class Pet:
    def __init__(self, name, hunger, energy, happiness):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.trick_list = []

    def __repr__(self):
        return f"My pet is {self.name} with {self.hunger} hunger, {self.energy} energy, and {self.happiness} happiness."

    def eat(self):
        hunger_staus = 0
        happiness_status = 0
        while self.hunger >= 0 and self.happiness <= 10:
            hunger_staus = self.hunger - 3
            happiness_status = self.happiness + 1
            return hunger_staus, happiness_status

    def sleep(self):
        energy_status = 0
        while self.energy <= 10:
            energy_status = self.energy + 5
            return energy_status

    def play(self):
        energy_status = 0
        happiness_status = 0
        hunger_status = 0
        while self.energy >= 0 and self.happiness <= 10 and self.hunger <= 10:
            energy_status = self.energy - 2
            happiness_status = self.happiness + 2
            hunger_status = self.hunger + 1
            return energy_status, happiness_status, hunger_status

    def get_status(self):
        energy_status = self.sleep() + self.play()[0]
        hunger_status = self.eat()[0] + self.play()[2]
        happiness_status = self.eat()[1] + self.play()[1]

        print(f"{self.name} has {energy_status} energy, {hunger_status} hunger, and {happiness_status} happiness.")

    def train(self, trick):
        self.trick_list.append(trick)
        print(f"{self.name} learned new trick(s): {self.trick_list}")



if __name__ == "__main__":
    print("Welcome to the Pet Simulator!")
    pet_name = "Eliza"
    pet_hunger = 5
    pet_energy = 5
    pet_happiness = 5

    pet = Pet(pet_name, pet_hunger, pet_energy, pet_happiness)
    pet.eat()
    pet.sleep()
    pet.play()
    pet.train("Roll Over")
    pet.train("Sit")
    pet.get_status()