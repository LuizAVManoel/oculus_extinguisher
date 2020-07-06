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
#              INPAINTING REVOLUTION	           #
#                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # ##

import imageio
import matplotlib.pyplot as plt
import numpy as np
from skimage import morphology as morp  # implements the morphology functions
import sys
from plot_compare import plot_compare


INF = 10000000000

def inpainting_revolution(input_img, mask):

	# TODO normalizar as imagens
	N, M = input_img.shape[0:2]
	r = input_img.copy()
	for i in range(0, N):
		for j in range(0, M):
			if mask[i,j,0] == 255:
				inpainting_search(r, mask, i, j)

	return r

def euclidian_distance(i, j, x, y):
	return np.sqrt(((x - i) * (x - i)) + ((y - j) * (y - j)))

def inpainting_search(input_img, mask, i, j):

	k = 2
	inpainted = False

	min_distance = INF
	min_distance_x = 0
	min_distance_y = 0

	while(not inpainted):

		sub_region_base = morp.disk(k)
	
		sub_region_input = input_img[i - k: i + k + 1, j - k:j + k + 1]
		sub_region_mask = mask[i - k: i + k + 1, j - k:j + k + 1]

		for x in range(0, ((2*k) +1)):
			for y in range(0, ((2*k) +1)):
				if sub_region_base[x,y] == 1 and sub_region_mask[x,y,0] == 0:
					euc_distance = euclidian_distance(i, j, x, y)
					if euc_distance < min_distance:
						min_distance = euc_distance
						min_distance_x = x
						min_distance_y = y	 

		if min_distance < INF:
			n_pixels = 0
			sum_pixelsR = 0
			sum_pixelsG = 0
			sum_pixelsB = 0
			for z in range(min_distance_x - 1, min_distance_x + 2):
				for w in range(min_distance_y -1, min_distance_y + 2):
					if z >= 0 and z <= 2*k and w >=0 and w <= 2*k:
						if sub_region_base[z,w] == 1 and sub_region_mask[z,w,0] == 0:
							sum_pixelsR += sub_region_input[z,w,0]
							sum_pixelsG += sub_region_input[z,w,1]
							sum_pixelsB += sub_region_input[z,w,2]
							n_pixels += 1	

			mean_pixels_valueR = sum_pixelsR / n_pixels
			mean_pixels_valueG = sum_pixelsG / n_pixels
			mean_pixels_valueB = sum_pixelsB / n_pixels
			input_img[i,j,0] = mean_pixels_valueR
			input_img[i,j,1] = mean_pixels_valueG
			input_img[i,j,2] = mean_pixels_valueB
			inpainted = True

		k += 1