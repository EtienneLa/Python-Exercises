class Mario():

    def move(self):
        print("Wohoo, moving!")


class Powershroom():

    def eat_shroom(self):
        print("I am big!")


class BigMario(Mario, Powershroom):
    pass


bm = BigMario()
bm.move()
bm.eat_shroom()
