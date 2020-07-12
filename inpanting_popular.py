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
#             	 INPAINTG POPULAR		           #
#                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # ##

import imageio
import matplotlib.pyplot as plt
import numpy as np
from skimage import morphology as morp  # implements the morphology functions
from plot_compare import plot_compare
import sys

#Searchs each input_img pixels until finds white mask pixels
def inpainting_popular(input_img, mask):

	N, M = input_img.shape[0:2]
	r = input_img.copy()
	for i in range(0, N):
		for j in range(0, M):
			if mask[i,j,0] == 255:
				inpainting_search(r, mask, i, j)

	return r

#Do the inpainting on the pixel
def inpainting_search(input_img, mask, i, j):

	k = 2
	inpainted = False

	while(not inpainted):

		#The subregion to find pixels outside mask
		sub_region_base = morp.disk(k)

		#Generates a subregion of size 2k + 1 around pixel to be inpainted
		sub_region_input = input_img[i - k: i + k + 1, j - k:j + k + 1]
		sub_region_mask = mask[i - k: i + k + 1, j - k:j + k + 1]

		#searches every pixel of the subregion
		for x in range(0, ((2*k) +1)):
			for y in range(0, ((2*k) +1)):
				#if pixel is inside sub_region_base and outside mask, then inpainting occurs
				if sub_region_base[x,y] == 1 and sub_region_mask[x,y,0] == 0:
					input_img[i,j,:] = sub_region_input[x,y,:] #inpaint respective RGB channels
					inpainted = True

		k += 1 #keeps searching for adequate subregion