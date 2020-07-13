# Final Project - Oculus Extinguisher
 SCC5830: Image processing, first semester of 2020 at University of São Paulo (USP), Brazil.

**Students:**
* Amanda Carrijo Viana Figur (8937736) - <a href="https://github.com/mandafigura">Amanda GitHub profile</a>.
* Luiz Augusto Vieira Manoel (8937308) - <a href="https://github.com/LuizAVManoel">Luiz GitHub profile</a>.

---


**Abstract:**

The aim of this project is to "erase" the eyeglasses of photos by filling removed pixels from people's faces. This technique is known as Inpainting and we made it by using Color Processing, Histogram Analysis, Image Enhancement, Morphology and Segmentation. Our project receives a RGB image of a person's face wearing eyeglasses, extracts the eyeglasses mask and returns the respective inpaited image without the eyeglasses. We used `Python 3` to make all our codes and Adobe Photoshop to obtain some of our images. This process might help with facial recognition problems.

**Keywords:**
Inpainting; Faces; Mask; Extraction; Segmentation.

---

## Project Description

The aim of this project is to "erase" the eyeglasses of photos by filling masked pixels from people's faces. We also implemented a program that generates such mask of pixels. Every code at this project is implemented using `Python 3`.

**Link for a brief video explaining our work (in Portuguese):** https://youtu.be/5S9GbPym8l4

**Example:**
| Input Image | Aim Result |
|:--:|:--:|
| <img src="/images/00-oculos-1.png" align="center" height="100" > | <img src="/images/00-oculos-2.png" align="center" height="100" > |
|<img src="/images/00-oculos-3.png" align="center" height="100" >| <img src="/images/00-oculos-4.png" align="center" height="100" >|

> Images Source: acquired by the students (Illustrative)

Here you can find the following inpainting codes:

* `inpanting_popular`: the simplest implementation of a inpainting algorithm you can find. Lacks a visual descriptor, only replaces the pixel in the mask area by a pixel outside the mask area;

* `inpanting_revolution`: the above algorithm with a visual descriptor. Searches and replaces near pixels;

* `inpanting_pyheal`: We used the <a title="Code" href="https://github.com/olvb/pyheal" target="_blank" rel="noopener">PyHeal</a> code, a pure Python implementation of Telea article on FMM inpainting to compare its results to our own algorithms. It uses an Image Inpainting Technique Based on the **Fast Marching Method** (FMM). The idea behind such method is to replace the eyeglasses estimating the image smoothness as a weighted average over a known neighborhood of the pixel to inpaint. The article can be found <a title="Article" href="https://www.researchgate.net/publication/238183352_An_Image_Inpainting_Technique_Based_on_the_Fast_Marching_Method" target="_blank" rel="noopener">here</a>: "An Image Inpainting Technique Based on the Fast Marching Method", by Alexandru Telea at the Eindhoven University of Technology, DOI: 10.1080/10867651.2004.10487596.

You can also find the additional codes:

* `mask_generator`: a code that receives an image and a seed point inside the glasses and generates a mask that can be used on any of the inpainting algorithms above;

* `plot_compare`: a function you can use to compare two images side by side while running any of the algorithms.

Try to run our `demo.py` file and use `Final_Project.ipynb` as a reference for understanding all the code implementations. This last code describe with details and compares the results we obtained.

You can find most of the images used in this project (the input, outputs, examples, etc.) on the images folder.


### Input images

On the table bellow we show the details of each image we used as input on this project. The original <a title="Angela" href="https://commons.wikimedia.org/wiki/File:Angela_Davis_%C3%A0_France_Culture_(Palais_de_Tokyo)_(8586327078).jpg" target="_blank" rel="noopener">Angela Davis</a> and <a title="Fidel" href="https://commons.wikimedia.org/wiki/Fidel_Castro#/media/File:Fidel_Castro.jpg" target="_blank" rel="noopener">Fidel Castro</a> images can be accessed on Wikimedia and lie under a Creative Commons license. We altered them in order to satisfy our needs.

| Image name | Image format | Dimensions | Color Model | Channel Size | Description |
|:--:|:--:|:--:|:--:|:--:|:--:|
| original_Fidel | .PNG | 436 x 458 | RGB | 8 bit | The original image without eyeglasses (for comparison) |
| oculus_Fidel | .PNG | 436 x 458 | RGB | 8 bit | The input Fidel image with artificial eyeglasses |
| manual_mask_Fidel | .PNG | 436 x 458 | RGB | 8 bit | The manual eyeglasses mask for Fidel |
| original_Angela | .PNG | 436 x 458 | RGB | 8 bit | Angela Davis wearing eyeglasses |
