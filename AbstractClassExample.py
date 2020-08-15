from abc import ABC, abstractmethod

class Image(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod                                                                                                                        
    def load_image(self, filename):
        pass
        
    @abstractmethod
    def save_image(self, filename):
        pass

# Sub class BITMAP
class Bitmap(Image):
    def load_image(self,filename):
        print('loading bitmap')

    def save_image(self,filename):
        print('save bitmap')

#  Sub class JPEG
class Jpeg(Image):
    def load_image(self,filename):
        print('loading jpeg')

    def save_image(self,filename):
        print('saving jpeg')

if __name__ == "__main__":
    img = Bitmap()
    img.load_image(img_1234.bmp)


# Python program showing 
# abstract base class work 

from abc import ABC, abstractmethod 

class Polygon(ABC): 

	# abstract method 
	def noofsides(self): 
		pass

class Triangle(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 3 sides") 

class Pentagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 5 sides") 

class Hexagon(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 6 sides") 

class Quadrilateral(Polygon): 

	# overriding abstract method 
	def noofsides(self): 
		print("I have 4 sides") 

# Driver code 
R = Triangle() 
R.noofsides() 

K = Quadrilateral() 
K.noofsides() 

R = Pentagon() 
R.noofsides() 

K = Hexagon() 
K.noofsides() 
