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

### Example:
 
| Input Image | Aim Result |
|:--:|:--:|
| <img src="/images/00-oculos-1.png" align="center" height="200" > | <img src="/images/00-oculos-2.png" align="center" height="200" > |
|<img src="/images/00-oculos-3.png" align="center" height="200" >| <img src="/images/00-oculos-4.png" align="center" height="200" >|

> Images Source: aquired by the students

---

## Objective

The aim of this project is to "erase" the eyeglasses of photos by filling removed pixels from people's faces.

We will use an Image Inpainting Technique Based on the Fast Marching Method. The idea behind such method is to replace the eyeglasses estimating the image smoothness as a weighted average over a known neighborhood of the pixel to inpaint.

The algorithm will be implemented in python using the pseudocode provided on the article "An Image Inpainting Technique Based on
the Fast Marching Method" - Alexandru Telea, Eindhoven University of Technology.

<br/>

## Input images

<p>An image that is going to be inpainted requires a mask.</p>

<p> We are going to start with a simple frontal portrait and artificially add an eyeglasses mask to it. The original image (without eyeglasses) will work as a reference after the algorithm is implemented on the masked (with eyeglasses) image. Based on the article, we decided to go through the following steps: </p>

<ol>
<li>
    We'll implement the inpaiting algorithm on a grayscale image. 
</li>
 


| <img src="/images/01-fidel-grayscale.png" height="290" /> | <img src="/images/02-fidel-grayscale.png" height="290" /> |
|:--:|:--:|
| The control image (without<br/>eyeglasses). Source: <a title="Fidel" href="https://commons.wikimedia.org/wiki/Fidel_Castro#/media/File:Fidel_Castro.jpg" target="_blank" rel="noopener">Wikimedia</a> (altered) | The masked image. |
 
<br/>

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

<br/>

<li> Then we'll apply the inpainting algorithm on the masked and colored image (to be obtained).</li>

</ol>
<br/>

<p> On the table bellow we show the details of each image we are going to use on this project:</p>

| Image name | Image format | Dimensions | Color Model | Channel Size |
|:--:|:--:|:--:|:--:|:--:|
| 01-fidel-grayscale | .PNG | 436 x 458 | grayscale | 8 bit |
| 02-fidel-grayscale | .PNG | 436 x 458 | grayscale | 8 bit |
| 03-fidel-RGB | .PNG | 436 x 458 | RGB | 8 bit |
| 04-fidel-RGB | .PNG | 436 x 458 | RGB | 8 bit |
| 05-angela-grayscale | .PNG | 436 x 458 | grayscale | 8 bit |
| 06-angela-RGB | .PNG | 436 x 458 | RGB | 8 bit |

## Methods and Material
