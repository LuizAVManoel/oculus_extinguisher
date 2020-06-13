# Final Project - Oculus Extinguisher
 SCC5830: Image processing, first semester of 2020 at University of São Paulo (USP)

**Students:**
* Amanda Carrijo Viana Figur (8937736)
* Luiz Augusto Vieira Manoel (8937308)

---


**Abstract:**

The aim of this project is to "erase" the eyeglasses of photos by filling removed pixels from people's faces. This technique is known as Inpainting and ist's going to be done by using search of texture information through image description. This process might help with facial recognition problems.

**Example:**
| Input Image | Aim Result |
|:--:|:--:|
| <img src="/images/00-oculos-1.png" align="center" height="100" > | <img src="/images/00-oculos-2.png" align="center" height="100" > |
|<img src="/images/00-oculos-3.png" align="center" height="100" >| <img src="/images/00-oculos-4.png" align="center" height="100" >|

> Images Source: acquired by the students

**Keywords:**
Inpainting; Image Description; Texture; Faces.

---

## Project Description

The aim of this project is to "erase" the eyeglasses of photos by filling removed pixels from people's faces.

We will use an Image Inpainting Technique Based on the **Fast Marching Method**. The idea behind such method is to replace the eyeglasses estimating the image smoothness as a weighted average over a known neighborhood of the pixel to inpaint.

The algorithm will be implemented in `Python 3.8` using the pseudocode provided on <a title="Article" href="https://www.researchgate.net/publication/238183352_An_Image_Inpainting_Technique_Based_on_the_Fast_Marching_Method" target="_blank" rel="noopener">the article</a> "An Image Inpainting Technique Based on the Fast Marching Method", by Alexandru Telea at the Eindhoven University of Technology, DOI: 10.1080/10867651.2004.10487596.


### The steps needed

<p>An image that is going to be inpainted requires a mask.</p>

<p> We are going to start with a simple frontal portrait and artificially add an eyeglasses mask to it. The original image will work as a reference after the algorithm is implemented on the masked image.</p>
 
<p> Based on the article, we decided to go through the following steps: </p>

<ol>
<li>
    We'll implement the inpaiting algorithm on a grayscale image. 
</li>
 


| <img src="/images/01-fidel-grayscale.png" height="290" /> | <img src="/images/02-fidel-grayscale.png" height="290" /> |
|:--:|:--:|
| The original image (without<br/>eyeglasses). Source: <a title="Fidel" href="https://commons.wikimedia.org/wiki/Fidel_Castro#/media/File:Fidel_Castro.jpg" target="_blank" rel="noopener">Wikimedia</a> (altered) | The masked image. |

<li>
    Once the algorithm is sucessfully implemented on a grayscale image we'll apply the same method for each RGB channel of a collored image.
</li>

| <img src="/images/03-fidel-RGB.png" height="290" /> | <img src="/images/04-fidel-RGB.png" height="290" /> |
|:--:|:--:|
| The control image (without<br/>eyeglasses). Source: <a title="Fidel" href="https://commons.wikimedia.org/wiki/Fidel_Castro#/media/File:Fidel_Castro.jpg" target="_blank" rel="noopener">Wikimedia</a> (altered) | The masked image. |
</ol>

<br/>

<p> After the inpainting algorithm is sucessfully implemented, we are going to use a simple frontal portrait of a person wearing eyeglasses and try to implement an auxiliary algorithm.</p>

<p>This algorithm goal is to extract the mask containing only the eyeglasses region on an input image. Then, our work will follow as bellow:</p>
<ol>
<li> We'll extract a mask from this image:</li>

| <img src="/images/05-angela-grayscale.png" height="290" /> |
|:--:|
| The original image (with eyeglasses).<br/>Source: <a title="Angela" href="https://commons.wikimedia.org/wiki/File:Angela_Davis_%C3%A0_France_Culture_(Palais_de_Tokyo)_(8586327078).jpg" target="_blank" rel="noopener">Wikimedia</a> (altered) |

<li> Then we'll apply the inpainting algorithm on the masked and colored image (to be obtained).</li>

</ol>

### Input details
<p> On the table bellow we show the details of each image we are going to use on this project. We altered them in order to satisfy our needs.</p>

| Image name | Image format | Dimensions | Color Model | Channel Size |
|:--:|:--:|:--:|:--:|:--:|
| 01-fidel-grayscale | .PNG | 436 x 458 | grayscale | 8 bit |
| 02-fidel-grayscale | .PNG | 436 x 458 | grayscale | 8 bit |
| 03-fidel-RGB | .PNG | 436 x 458 | RGB | 8 bit |
| 04-fidel-RGB | .PNG | 436 x 458 | RGB | 8 bit |
| 05-angela-grayscale | .PNG | 436 x 458 | grayscale | 8 bit |
| 06-angela-RGB | .PNG | 436 x 458 | RGB | 8 bit |

The originals <a title="Angela" href="https://commons.wikimedia.org/wiki/File:Angela_Davis_%C3%A0_France_Culture_(Palais_de_Tokyo)_(8586327078).jpg" target="_blank" rel="noopener">Angela Davis</a> and <a title="Fidel" href="https://commons.wikimedia.org/wiki/Fidel_Castro#/media/File:Fidel_Castro.jpg" target="_blank" rel="noopener">Fidel Castro</a> images can be accessed on Wikimedia and lie under a Creative Commons license.
