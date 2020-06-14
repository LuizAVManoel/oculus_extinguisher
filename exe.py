import imageio
import inpanting_pyheal



img = imageio.imread("/home/luiz/Desktop/2k20/PI/Trabalhos/ProjetoFinal/oculus_extinguisher/images/04-fidel-RGB.png")
mask_img = imageio.imread("/home/luiz/Desktop/2k20/PI/Trabalhos/ProjetoFinal/oculus_extinguisher/images/04-fidel-RGB-mask.png")
inpanting_pyheal.inpaint(img, mask_img, 4)
imageio.imwrite("fidel.png", img)