class Enemy:

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)


enemy1 = Enemy(5)
enemy2 = Enemy(8)

enemy1.get_energy()
enemy2.get_energy()

