#   Create a class, then an object.  Assogm vaiues using the __init__() function.(pg 179)
class Horse:
  def __init__(self, hclass, breed, gait, origin, colors):
    self.hclass = hclass
    self.breed = breed
    self.gait = gait
    self.origin = origin
    self.colors =  colors

horse1 = Horse("Ponies", "Shetland","general","Scotland","various")

print("\nOf the {} classification, the {} is well-known.  Their gait is {}, unlike dressage horses.\
  They also  have {} colors unlike the Palomino (ex.) and is thought to have originally come\
 from {}.".format(horse1.hclass, horse1.breed, horse1.gait, horse1.colors, horse1.origin))
