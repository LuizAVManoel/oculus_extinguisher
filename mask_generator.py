# # # # # # # # # # #  HEADER  # # # # # # # # # # #
#                                                  #
#        STUDENT: Amanda Carrijo Viana Figur       #
#                N. USP: 8937736                   #
#        STUDENT: Luiz Augusto Vieira Manoel       #
#                N. USP: 8937308                   #
#   COURSE: Mestrado em Ciências de Computação e   #
#        Matemática Computacional (PPG-CCMC)       #
#            YEAR OF ENTRY: 2020/2019              #
#             							           #
#                                                  #
##  # # # # # # # # # # # # # # # # # # # # # # # ##

import imageio as img  
import matplotlib.pyplot as plt  
import numpy as np  
from skimage import morphology as morp # implements the morphology functions
import cv2 # for face detection
import sys

sys.setrecursionlimit(1000000) # allow region growing average algorithm runs

# Function that plots two images side by side. r = reference, m = modified
def plot_compare(r, m):
    plt.figure(figsize=(12, 12))

    # defines a panel to show the images side by side
    plt.subplot(121)  # panel with 1 row, 2 columns, to show the image at the first (1st) position
    plt.imshow(r, cmap="gray")
    plt.axis('off')   # remove axis with numbers

    plt.subplot(122)  # panel with 1 row, 2 columns, to show the image at the second (2nd) position
    plt.imshow(m, cmap="gray")
    plt.axis('off')

    plt.show()

def brightness_normalization(input_img):
	N, M = input_img.shape
	for i in range(0, N):
		for j in range(0, M):
			if (input_img[i,j] < 0):
				input_img[i,j] = 0
			elif (input_img[i,j] > 255):
				input_img[i,j] = 255

	return input_img

# Brightness modulation
def brightness(input_img, c):
	input_img_copy = input_img.copy().astype(np.float32)
	input_img_copy = input_img_copy + c
	input_img_copy = brightness_normalization(input_img_copy)
	return input_img_copy.astype(np.uint8)

# Constrat modulation
def contrast(input_img, c, d): 
	a = np.amin(input_img)
	b = np.amax(input_img)
	return (((input_img.astype(np.float32) - a) * (d - c) / (b - a)) + c).astype(np.uint8)


def treshold_binarization(input_img,t):
	N, M = input_img.shape
	r = input_img.copy()
	for i in range(0, N):
		for j in range(0, M):
			if (r[i,j] >= t):
				r[i,j] = 255
			else:
				r[i,j] = 0

	return r

def opening_and_close(input_img, k):
	structuring_element = morp.disk(k)
	img1 = morp.opening(input_img, structuring_element)
	return img1 

def distance(a, b):
    return np.abs(a-b)

def region_growing_average(img, img_t, tolerance, seed):
    
    x = seed[0] 
    y = seed[1]

    img_t[x, y] = 1
    
    avg = np.mean(img[np.where(img_t==1)])
    
    # check matrix border and conquering criterion for the 4-neigbourhood
    if (y+1 < img.shape[1] and img_t[x,y+1] == 0 and img[x, y+1] <= tolerance):
        region_growing_average(img, img_t, tolerance, [x, y+1])
        
    if (y-1 >= 0 and img_t[x,y-1] == 0  and img[x, y-1] <= tolerance):
        region_growing_average(img, img_t, tolerance, [x, y-1])
        
    if (x+1 < img.shape[0] and img_t[x+1,y] == 0  and img[x+1, y] <= tolerance):
        region_growing_average(img, img_t, tolerance, [x+1, y])
        
    if (x-1 >= 0 and img_t[x-1,y] == 0  and img[x-1, y] <= tolerance):
        region_growing_average(img, img_t, tolerance, [x-1, y])

# Inversion modulation
def inversion(input_img): 
	return (255 - input_img.astype(np.float32)).astype(np.uint8)

# Main
filename = str(input()).rstrip()
input_img = img.imread(filename)
brightness_parameter = int(input()) #144

bighter_img = brightness(input_img, brightness_parameter)
# plot_compare(input_img, bighter_img)

contrast_img = contrast(bighter_img, 0, 255)
# plot_compare(bighter_img, contrast_img)

modified_img = opening_and_close(contrast_img, 4)
# plot_compare(contrast_img, modified_img)

binarie_image = treshold_binarization(modified_img, 174)
# plot_compare(modified_img, binarie_image)

binarie_invert = inversion(binarie_image)
# plot_compare(binarie_image, binarie_invert)

disk = morp.disk(2)
binarie_dilation = morp.dilation(binarie_invert, disk)
# plot_compare(binarie_invert, binarie_dilation)

binarie_dilation_desinvert = inversion(binarie_dilation)
# plot_compare(binarie_dilation, binarie_dilation_desinvert)

img_seed = np.zeros(input_img.shape)
region_growing_average(binarie_dilation_desinvert, img_seed, 0, [240, 200])
region_growing_average(binarie_dilation_desinvert, img_seed, 0, [282, 202])
# plot_compare(binarie_dilation_desinvert, img_seed)

# rectangle = morp.rectangle(12,1)
# mask = morp.dilation(img_seed,rectangle)
# plot_compare(img_seed, mask)

img.imwrite('maskagdv.png',img_seed.astype(np.uint8))

############################### FACE DETECTION ##############################
# Load the cascade
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
# img_cv2 = cv2.imread(filename)
# Convert into grayscale
# gray = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)
# Detect faces
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
# for (x, y, w, h) in faces:
	# cv2.rectangle(img_cv2, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the output
# print(faces)
# cv2.imshow('img', img_cv2)
# cv2.waitKey()
#############################################################################
