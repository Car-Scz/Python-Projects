
#  Create a Parent class
class Pet():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

#  create a child class
class Cat(Pet):
    is_feline = True
    legs = 4
    makes_sound = ("\"Meow!\"")

    def cat_info(self):
        msg = ("\n{} weighs {} pounds, has {} legs, and says {}".format(self.name,self.weight,self.legs,self.makes_sound))
        return msg

# create a second child class
class Parrot(Pet):
    is_feline = False
    wings = 2
    makes_sound = (" \"Polly wants a cracker!\"")

    def parrot_info(self):
        msg = ("\n{} weighs {} pounds, has {} wings, and says {}".format(self.name,self.weight,self.wings,self.makes_sound))
        return msg

if __name__ == "__main__":

    my_cat = Cat('Kibbles', 8)
    print(my_cat.cat_info())

    my_parrot = Parrot('Polly', 25)
    print(my_parrot.parrot_info())
