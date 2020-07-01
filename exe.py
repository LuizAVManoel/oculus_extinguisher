import imageio
import inpanting_pyheal
import mask_generator as masker

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