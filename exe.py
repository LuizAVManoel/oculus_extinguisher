import imageio
import inpanting_pyheal

img = imageio.imread("./images/02-fidel-RGB-oculus.png")
mask = imageio.imread("./images/03-fidel-RGB-mask.png")
inpanting_pyheal.inpaint(img, mask, 4)
imageio.imwrite("./images/01-fidel-RGB-inpainted.png", img)