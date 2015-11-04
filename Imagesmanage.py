__author__ = 'avarm1'
from PIL import Image

def displayimage(count):
    image=Image.open("images/stage"+str(count)+".png")
    image.show()
