from skimage import morphology as morp  # implements the morphology functions
import imageio

import matplotlib.pyplot as plt

from PIL import Image

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


def inpainting_popular(input_img, mask):

	# TODO normalizar as imagens
	N, M = input_img.shape[0:2]
	r = input_img.copy()
	for i in range(0, N):
		for j in range(0, M):
			if mask[i,j,0] == 255:
				inpainting_search(r, mask, i, j)

	plot_compare(input_img, r)

def inpainting_search(input_img, mask, i, j):

	k = 2
	inpainted = False

	while(not inpainted):

		sub_region_base = morp.disk(k)
	
		sub_region_input = input_img[i - k: i + k + 1, j - k:j + k + 1]
		sub_region_mask = mask[i - k: i + k + 1, j - k:j + k + 1]

		for x in range(0, ((2*k) +1)):
			for y in range(0, ((2*k) +1)):
				if sub_region_base[x,y] == 1 and sub_region_mask[x,y,0] == 0:
					input_img[i,j,:] = sub_region_input[x,y,:]
					inpainted = True

		k += 1

img = imageio.imread("gray-fidel.png")
mask = imageio.imread("gray-mask.png")
inpainting_popular(img, mask)