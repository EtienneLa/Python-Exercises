class Girl:

    gender = "female"

    def __init__(self, name):
        self.name = name


girl1 = Girl("Lucy")
girl2 = Girl("Barbara")

print(girl1.gender, girl1.name)
print(girl2.gender, girl2.name)

