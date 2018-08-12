class Parent:

    def print_last_name(self):
        print("Mustermann")

    def print_home_state(self):
        print("Florida")

class Child(Parent):

    def print_first_name(self):
        print("Max")

    def print_last_name(self):
        print("Notmustermann")


max = Child()
max.print_first_name()
max.print_last_name()
max.print_home_state()
