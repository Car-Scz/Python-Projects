#  Encapsulation example
class Polygon(object):
   def __init__(self):
      self.a = 123
      self._b = 123
      self.__c = 123

if __name__ == "__main__":
    obj = Polygon()
    #  unprotected and not private
    print(obj.a)
    # private variable
    print(obj._b)
    # proected variable
    print(obj.__c)
