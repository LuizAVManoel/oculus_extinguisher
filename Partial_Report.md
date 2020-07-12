# Final Project - Oculus Extinguisher
 SCC5830: Image processing, first semester of 2020 at University of São Paulo (USP)

**Students:**
* Amanda Carrijo Viana Figur (8937736)
* Luiz Augusto Vieira Manoel (8937308)

---


**Abstract:**

The aim of this project is to "erase" the eyeglasses of photos by filling removed pixels from people's faces. This technique is known as Inpainting and ist's going to be done by using search of texture information through image description. This process might help with facial recognition problems.

**Keywords:**
Inpainting; Image Description; Texture; Faces.

---

## Project Description

The aim of this project is to "erase" the eyeglasses of photos by filling removed pixels from people's faces. This process might help with facial recognition problems.

**Example:**
| Input Image | Aim Result |
|:--:|:--:|
| <img src="/images/00-oculos-1.png" align="center" height="100" > | <img src="/images/00-oculos-2.png" align="center" height="100" > |
|<img src="/images/00-oculos-3.png" align="center" height="100" >| <img src="/images/00-oculos-4.png" align="center" height="100" >|

> Images Source: acquired by the students (Illustrative)

We will use an Image Inpainting Technique Based on the **Fast Marching Method** (FMM). The idea behind such method is to replace the eyeglasses estimating the image smoothness as a weighted average over a known neighborhood of the pixel to inpaint.

The algorithm will be implemented in `Python 3`. We used as main reference the <a title="Code" href="https://github.com/olvb/pyheal" target="_blank" rel="noopener">PyHeal</a> code, a pure Python implementation of Telea article on FMM inpainting. Such article can be found <a title="Article" href="https://www.researchgate.net/publication/238183352_An_Image_Inpainting_Technique_Based_on_the_Fast_Marching_Method" target="_blank" rel="noopener">here</a>: "An Image Inpainting Technique Based on the Fast Marching Method", by Alexandru Telea at the Eindhoven University of Technology, DOI: 10.1080/10867651.2004.10487596.


### The steps needed

<p>An image that is going to be inpainted requires a mask. At this first moment we are going to provide a mask by input. Later our intention is to be able to generate such mask.</p>

<p> We are going to start with a simple frontal portrait and artificially add an eyeglasses mask to it. The original image will work as a comparison reference after the algorithm is implemented on the masked image.</p>
 
<p> The implemented algorithm go through the following steps: </p>

<ol>
<li>
    We'll input on the algorithm an image that is going to be inpainted and a mask. The black region of the mask represents the KNOWN pixels; The white region of the mask represents the UNKNOWN pixes, that are going to be inpainted.
</li>
 


| <img src="/images/02-fidel-RGB-oculus.png" height="290" /> | <img src="/images/03-fidel-RGB-mask.png" height="290" /> |
|:--:|:--:|
| The  image (with eyeglasses)<br/> going to be inpainted. | The mask. |

<li>
    The algorithm will then find the mask border and then find a region acordingly to the given radius that's going to work as reference for the inpainting. The images bellow are just an ILLUSTRATION.
</li>

| <img src="/images/00-oculos-5.png" height="290" /> | <img src="/images/00-oculos-6.png" height="290" /> |
|:--:|:--:|
| The border of the mask (red). | The reference region (blue). |
> Images Source: acquired by the students (Illustrative)

<li>
    The algorithm will fill the mask (white) region with with a mean value based on the pixels directions and the "distance" related to the border and the values on each RGB channel. This is the Fast Marching Method. Bellow we show an output example:
</li>

| <img src="/images/01-fidel-RGB.png" height="290" /> | <img src="/images/01-fidel-RGB-inpainted2.png" height="290" /> | <img src="/images/02-fidel-RGB-oculus.png" height="290" /> |
|:--:|:--:|:--:|
| The original image (without<br/>eyeglasses) for reference. | The output of the algorithm<br/>(the inpainted image). | The input of the algorithm. |

</ol>

### Further Steps

<p> After the inpainting algorithm is sucessfully implemented, we are going to use a simple frontal portrait of a person wearing eyeglasses and try to implement an auxiliary algorithm.</p>

<p>This algorithm goal is to extract the mask containing only the eyeglasses region on an input image. Then, our work will follow as bellow:</p>
<ol>
<li> We'll extract a mask from this image:</li>

| <img src="/images/04-angela-RGB.png" height="290" /> |
|:--:|
| The original image (with eyeglasses).<br/>Source: <a title="Angela" href="https://commons.wikimedia.org/wiki/File:Angela_Davis_%C3%A0_France_Culture_(Palais_de_Tokyo)_(8586327078).jpg" target="_blank" rel="noopener">Wikimedia</a> (altered) |

<li> Then we'll apply the inpainting algorithm on the image with the mask obtained.</li>

</ol>


### Input details

On the table bellow we show the details of each image we are going to use as input on this project and also the output images we've already obtained. The original <a title="Angela" href="https://commons.wikimedia.org/wiki/File:Angela_Davis_%C3%A0_France_Culture_(Palais_de_Tokyo)_(8586327078).jpg" target="_blank" rel="noopener">Angela Davis</a> and <a title="Fidel" href="https://commons.wikimedia.org/wiki/Fidel_Castro#/media/File:Fidel_Castro.jpg" target="_blank" rel="noopener">Fidel Castro</a> images can be accessed on Wikimedia and lie under a Creative Commons license. We altered the input images in order to satisfy our needs.

| Image name | Image format | Dimensions | Color Model | Channel Size | Description |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 01-fidel-RGB | .PNG | 436 x 458 | RGB | 8 bit | The original image without eyeglasses (for comparison) |
| 01-fidel-RGB-inpainted | .PNG | 436 x 458 | RGB | 8 bit | The inpainted image with thinner mask |
| 01-fidel-RGB-inpainted2 | .PNG | 436 x 458 | RGB | 8 bit | The inpainted image with thicker mask |
| 02-fidel-RGB-oculus | .PNG | 436 x 458 | RGB | 8 bit | The input image with artificial eyeglasses |
| 03-fidel-RGB-mask | .PNG | 436 x 458 | RGB | 8 bit | The thin eyeglasses mask |
| 03-fidel-RGB-mask2 | .PNG | 436 x 458 | RGB | 8 bit | The thick eyeglasses mask |
| 04-angela-RGB | .PNG | 436 x 458 | RGB | 8 bit | Angela Davis wearing eyeglasses |
