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
#                                                  #
# # # # # # # # # # # # # # # # # # # # # # # # # ##

import imageio
import inpanting_pyheal
import mask_generator as masker

# computes the error between the reference image r and the modified image m
def calculo_erro(r, m):
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
    print(f"{RMSE:.4f}", sep='', end='')

'''
    Read inputs:
    "image to be inpainted filename"
    int (1, 2 or 3) (fidel, angela or manual mask)
    if 3 => "mask filename"
'''
filename = str(input()).rstrip()
inpaint_option = int(input())

if inpaint_option == 1: #fidel
    img = imageio.imread(filename)
    mask = masker.mask_generator(filename, [164, 228])
    inpanting_pyheal.inpaint(img, mask, 4)
    imageio.imwrite("./images/01-fidel-RGB-inpainted-generated-mask.png", img)
elif inpaint_option == 2: #angela
    img = imageio.imread(filename)
    mask = masker.mask_generator(filename, [240,200])
    inpanting_pyheal.inpaint(img, mask, 4)
    imageio.imwrite("./images/04-angela-RGB-inpainted-generated-mask.png", img)
elif inpaint_option == 3: #manual mask
    maskname = str(input()).rstrip()
    img = imageio.imread(filename)
    mask = imageio.imread(maskname)
    inpanting_pyheal.inpaint(img, mask, 4)
    imageio.imwrite("./images/01-inpaint-manual-mask.png", img)