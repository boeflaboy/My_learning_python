class Animal:
    def __init__(self):
        self.number_eyes = 2

    def breathe(self):
        print("Inhale/Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in the water")

    def breathe(self):
        super().breathe()
        print("Doing under water")


nemo = Fish()
nemo.breathe()




