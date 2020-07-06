# # # # # # # # # # #  HEADER  # # # # # # # # # # #
#                                                  #
#        STUDENT: Amanda Carrijo Viana Figur       #
#                N. USP: 8937736                   #
#        STUDENT: Luiz Augusto Vieira Manoel       #
#                N. USP: 8937308                   #
#   COURSE: Mestrado em Ciências de Computação e   #
#        Matemática Computacional (PPG-CCMC)       #
#            YEAR OF ENTRY: 2020/2019              #
#                  FINAL PROJECT                   #
#                  DEMONSTRATION                   #
#                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # ##


import inpanting_pyheal
import inpanting_popular
import inpanting_revolution
import mask_generator as masker


import imageio
import matplotlib.pyplot as plt
import numpy as np
import sys
from plot_compare import plot_compare

# computes the error between the reference image r and the modified image m
def RMSE(r, m):
    # converts values to float
    m = m.astype(np.float32)
    r = r.astype(np.float32)

    #calculates how many pixels image has
    N, M = r[:,:,0].shape
    T = N*M

    # auxiliary matrix for computations
    aux = np.subtract(m,r)
    aux = np.power(aux, 2)
    mean = np.divide(np.sum(aux),T)
    RMSE = np.sqrt(mean)

    # prits error with 4 decimal places and adjusts identation
    print(f"{RMSE:.4f}\n", sep='', end='')

# FIRST STEP: FIDEL CASTRO WITH THE MANUAL MASK
original_img = imageio.imread('./images/original_Fidel.png')
img = imageio.imread('./images/oculus_Fidel.png')
mask = imageio.imread('./images/manual_mask_Fidel.png')
plot_compare(img, mask)

img_pyheal = inpanting_pyheal.inpaint(img, mask, 4)
plot_compare(img, img_pyheal)
print('RMSE Original - Pyheal(manual mask)')
RMSE(original_img, img_pyheal)
plot_compare(img_pyheal, original_img)

img_popular = inpanting_popular.inpainting_popular(img, mask)
plot_compare(img, img_popular)
print('RMSE Original - Popular(manual mask)')
RMSE(original_img, img_popular)
plot_compare(img_popular, original_img)

img_revolution = inpanting_revolution.inpainting_revolution(img, mask)
plot_compare(img, img_revolution)
print('RMSE Original - Revolution(manual mask)')
RMSE(original_img, img_revolution)
plot_compare(img_revolution, original_img)

print('\n')

# SECOND STEP: FIDEL CASTRO WITH THE GENERATED MASK
mask2 = masker.mask_generator('./images/oculus_Fidel.png', [164, 228])
plot_compare(img, mask2)

plot_compare(mask, mask2)

img_pyheal = inpanting_pyheal.inpaint(img, mask2, 4)
plot_compare(img, img_pyheal)
print('RMSE Original - PyHeal(generated mask)')
RMSE(original_img, img_pyheal)
plot_compare(img_pyheal, original_img)

img_popular = inpanting_popular.inpainting_popular(img, mask2)
plot_compare(img, img_popular)
print('RMSE Original - Popular(generated mask)')
RMSE(original_img, img_popular)
plot_compare(img_popular, original_img)

img_revolution = inpanting_revolution.inpainting_revolution(img, mask2)
plot_compare(img, img_revolution)
print('RMSE Original - Revolution(generated mask)')
RMSE(original_img, img_revolution)
plot_compare(img_revolution, original_img)

# THIRD STEP: ANGELA DAVIS WITH THE GENERATED MASK
img = imageio.imread('./images/original_Angela.png')
mask = masker.mask_generator('./images/original_Angela.png', [240,200])
plot_compare(img, mask)

img_pyheal = inpanting_pyheal.inpaint(img, mask, 4)
plot_compare(img, img_pyheal)

img_popular = inpanting_popular.inpainting_popular(img, mask)
plot_compare(img, img_popular)

img_revolution = inpanting_revolution.inpainting_revolution(img, mask)
plot_compare(img, img_revolution)