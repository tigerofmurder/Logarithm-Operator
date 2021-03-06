import cv2
import numpy as np 
import math
import cmath
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def exponential(c,f):
	value = int(c*math.log(1+f,10))
	if(value>255):
		return 255
	return value


def squared(c,f):
	value = int(c*math.sqrt(f))
	if(value>255):
		return 255
	return value

def main(cons,img):
	''''
	cv2.imshow('Coverted Image',img)
	cv2.waitKey(0)'''

	height, width = img.shape

	for y in range(0,width):
		for x in range(0,height):
			img[x,y] = exponential(cons,img[x,y])

	'''cv2.imshow('Coverted Image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()'''
	strr = str(cons)+".jpg"
	cv2.imwrite(strr,img);


Tk().withdraw()
filename = askopenfilename()

values = [80,100,120]
for i in values:
	imgen = cv2.imread(filename)
	img = cv2.cvtColor(imgen, cv2.COLOR_BGR2GRAY)
	main(i,img)
#cons = int(input("Valor de constante: "))#255/np.log(1+np.max(imgen)) 



