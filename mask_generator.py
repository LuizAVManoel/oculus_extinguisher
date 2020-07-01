# # # # # # # # # # #  HEADER  # # # # # # # # # # #
#                                                  #
#        STUDENT: Amanda Carrijo Viana Figur       #
#                N. USP: 8937736                   #
#        STUDENT: Luiz Augusto Vieira Manoel       #
#                N. USP: 8937308                   #
#   COURSE: Mestrado em Ciências de Computação e   #
#        Matemática Computacional (PPG-CCMC)       #
#            YEAR OF ENTRY: 2020/2019              #
#             	   FINAL PROJECT		           #
#             	  MASK  GENERATOR		           #
#                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # ##

import imageio as img
import matplotlib.pyplot as plt
import numpy as np
from skimage import morphology as morp  # implements the morphology functions
#import cv2  # for face detection
import sys


sys.setrecursionlimit(1000000)  # allow 'region_growing_average' algorithm to run


# Function that plots two images side by side. r = reference, m = modified
def plot_compare(r, m):
    plt.figure(figsize=(12, 12))

    # defines a panel to show the images side by side
    plt.subplot(121)  # panel with 1 row, 2 columns, to show the image at the first (1st) position
    plt.imshow(r, cmap="gray")
    plt.axis('off')  # remove axis with numbers

    plt.subplot(122)  # panel with 1 row, 2 columns, to show the image at the second (2nd) position
    plt.imshow(m, cmap="gray")
    plt.axis('off')

    plt.show()


# Normalizes an image r (turns max intensity to 255 and min intensity to 0)
def image_normalization(r):
    a = np.amin(r)  # least intensity
    b = np.amax(r)  # maximum intensity
    # normalizer
    r = np.divide((r - a),(b - a))*255
    return r.astype(np.uint8)


# Normalizes the increased or decreased brightness of an image
def brightness_normalization(input_img):
    N, M = input_img.shape
    for i in range(0, N):
        for j in range(0, M):
            if (input_img[i, j] < 0): #sets values below zero to zero
                input_img[i, j] = 0
            elif (input_img[i, j] > 255): #sets values above 255 to 255
                input_img[i, j] = 255

    return input_img


# Brightness modulation by a value c in range 0-255
def brightness(input_img, c):
    input_img_copy = input_img.copy().astype(np.float32)
    input_img_copy = input_img_copy + c
    input_img_copy = brightness_normalization(input_img_copy)
    return input_img_copy.astype(np.uint8)


# Constrat modulation: c is the lowest value and d is the highest value
def contrast(input_img, c, d):
    a = np.amin(input_img)
    b = np.amax(input_img)
    return (((input_img.astype(np.float32) - a) * (d - c) / (b - a)) + c).astype(np.uint8)


# binarizes a gray image by a threshold t in range 0-255.
def treshold_binarization(input_img, t):
    N, M = input_img.shape
    r = input_img.copy()
    for i in range(0, N):
        for j in range(0, M):  #Values equal or greater to threshhold t are white
            if (r[i, j] >= t):
                r[i, j] = 255
            else:              #Values below the threshhold t are black
                r[i, j] = 0
    return r


# performs the opening operation on a grayscale image
def opening(input_img, k):
    structuring_element = morp.disk(k)
    img1 = morp.opening(input_img, structuring_element)
    return img1


# performs the closing operation on a grayscale image
def closing(input_img, k):
    structuring_element = morp.disk(k)
    img1 = morp.closing(input_img, structuring_element)
    return img1


#grows a binary image begining from a seed
def region_growing_average(img, img_t, tolerance, seed):
    x = seed[0]
    y = seed[1]

    img_t[x, y] = 1

    # check matrix border and conquering criterion for the 4-neigbourhood
    if (y + 1 < img.shape[1] and img_t[x, y + 1] == 0 and img[x, y + 1] <= tolerance):
        region_growing_average(img, img_t, tolerance, [x, y + 1])

    if (y - 1 >= 0 and img_t[x, y - 1] == 0 and img[x, y - 1] <= tolerance):
        region_growing_average(img, img_t, tolerance, [x, y - 1])

    if (x + 1 < img.shape[0] and img_t[x + 1, y] == 0 and img[x + 1, y] <= tolerance):
        region_growing_average(img, img_t, tolerance, [x + 1, y])

    if (x - 1 >= 0 and img_t[x - 1, y] == 0 and img[x - 1, y] <= tolerance):
        region_growing_average(img, img_t, tolerance, [x - 1, y])


# Inverts values of an image
def inversion(input_img):
    return (255 - input_img.astype(np.float32)).astype(np.uint8)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                    THE MAIN FUNCTION                    #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def mask_generator(filename,seed):
    # Starts program with an RGB image and converts it to grayscale
    original_image = img.imread(filename)
    grayscale_image = 0.2125 * original_image[:,:,0] + 0.7154 * original_image[:,:,1] + 0.0721 * original_image[:,:,2]
    '''
        smoothening image, so it has less noise. Also the objective is to increase
        the contrast between the skin and the eyeglasses, so we can find the eyeglasses
        easily.
    '''
    brighter_img = brightness(grayscale_image,150) #144
    plot_compare(grayscale_image,brighter_img)
    contrast_img = contrast(brighter_img,0,255)
    open_img = opening(contrast_img,4) #disk of radius 4 for opening

    #making operations on binary img
    binary_img = treshold_binarization(open_img,174) #how can we define this threshold better?
    # we have some operations that can only be perfomed on the white area of the image
    invert_img = inversion(binary_img)
    disk = morp.disk(2)
    invert_img = morp.dilation(invert_img, disk)
    #the binary image again, with operations applyed
    binary_img = inversion(invert_img)
    plot_compare(grayscale_image,binary_img)

    '''
        Now we are going to perform the image segmentation at the binary image. We need seeds
        and the final output should be the wanted eyeglasses mask.
    '''
    img_seed = np.zeros(grayscale_image.shape)  #the segmentations are saved here
    #performs search using two seeds
    region_growing_average(binary_img, img_seed, 0, seed)
    #region_growing_average(binary_img, img_seed, 0, [282, 202])
    #plots images
    plot_compare(binary_img, img_seed)

    #normalizes the seed, so it has Grayscale values
    grayscale_mask = image_normalization(img_seed)

    #Composing a RGB image
    rgb_mask = np.zeros(original_image.shape, dtype=np.uint8)
    rgb_mask[:,:,0] = grayscale_mask
    rgb_mask[:,:,1] = grayscale_mask
    rgb_mask[:,:,2] = grayscale_mask

    img.imwrite(filename + 'generated-mask.png', rgb_mask.astype(np.uint8))

    return rgb_mask


# # Main
# filename = str(input()).rstrip()
# input_img = img.imread(filename)
# brightness_parameter = int(input())  # 144
#
# bighter_img = brightness(input_img, brightness_parameter)
# # plot_compare(input_img, bighter_img)
#
# contrast_img = contrast(bighter_img, 0, 255)
# # plot_compare(bighter_img, contrast_img)
#
# modified_img = opening(contrast_img, 4)
# # plot_compare(contrast_img, modified_img)
#
# binarie_image = treshold_binarization(modified_img, 174)
# # plot_compare(modified_img, binarie_image)
#
# binarie_invert = inversion(binarie_image)
# # plot_compare(binarie_image, binarie_invert)
#
# disk = morp.disk(2)
# binarie_dilation = morp.dilation(binarie_invert, disk)
# #plot_compare(binarie_invert, binarie_dilation)
#
# binarie_dilation_desinvert = inversion(binarie_dilation)
# #plot_compare(binarie_dilation, binarie_dilation_desinvert)
#
# img_seed = np.zeros(input_img.shape)
# region_growing_average(binarie_dilation_desinvert, img_seed, 0, [240, 200])
# region_growing_average(binarie_dilation_desinvert, img_seed, 0, [282, 202])
# plot_compare(binarie_dilation_desinvert, img_seed)
#
# # rectangle = morp.rectangle(12,1)
# # mask = morp.dilation(img_seed,rectangle)
# # plot_compare(img_seed, mask)
#
# img_seed = image_normalization(img_seed)
# img.imwrite('maskagdv.png', img_seed.astype(np.uint8))
#
# ############################### FACE DETECTION ##############################
# # Load the cascade
# # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# # Read the input image
# # img_cv2 = cv2.imread(filename)
#
# # Convert into grayscale
# # gray = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)
# # Detect faces
# # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# # Draw rectangle around the faces
# # for (x, y, w, h) in faces:
# # cv2.rectangle(img_cv2, (x, y), (x+w, y+h), (255, 0, 0), 2)
# # Display the output
# # print(faces)
# # cv2.imshow('img', img_cv2)
# # cv2.waitKey()
# #############################################################################
