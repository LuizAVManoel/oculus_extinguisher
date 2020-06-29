import imageio
import inpanting_pyheal

img = imageio.imread("./images/04-angela-RGB.png")
mask = imageio.imread("maskagdv.png")
mask_rgb = img.copy()

# Putting the mask on RGB
mask_rgb[:,:,0] = mask
mask_rgb[:,:,1] = mask
mask_rgb[:,:,2] = mask

inpanting_pyheal.inpaint(img, mask_rgb, 4)
imageio.imwrite("./images/inpantedagdv.png", img)