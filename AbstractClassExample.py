#  Python program showing Abstract Class coding use
from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self,value):
        print("Passed value: ", value)
    @abstractmethod
    def task(self):
        print("...inside Abstract class task")
 
class polygon_class(Absclass): 
    def task(self):
        print("\n...inside Parent polygon_class  task")

class hexagon_class(polygon_class): 
    def task(self):
        print("\n...inside Child hexagon_class task")
  
if __name__ == "__main__":
 
        #  object of polygon_class created
        polygon_obj = polygon_class()
        polygon_obj.task()
        polygon_obj.print('I have variable sides')
        print("\npolygon_obj is instance of Absclass? ", isinstance(polygon_obj, Absclass))

        #  object of hexagon_class created
        hexagon_obj = hexagon_class()
        hexagon_obj.task()
        hexagon_obj.print('I have 6 sides')
        print("\nhexagon_obj is instance of Absclass? ", isinstance(hexagon_obj, Absclass))
