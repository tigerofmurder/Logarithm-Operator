import cv2
import math
import cmath
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def exponential(c,f):
	return int(c*math.log(1+f,10))


Tk().withdraw()
filename = askopenfilename()

imgen = cv2.imread(filename)
img = cv2.cvtColor(imgen, cv2.COLOR_BGR2GRAY)

cons = int(input("Ingrese constante de cambio: "))

cv2.imshow('Coverted Image',img)
cv2.waitKey(0)

height, width = img.shape

for y in range(0,width):
	for x in range(0,height):
		img[x,y] = exponential(cons,img[x,y])

cv2.imshow('Coverted Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


