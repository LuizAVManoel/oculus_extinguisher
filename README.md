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
| <img src="/images/01-oculos.png" align="center" height="200" > | <img src="/images/02-oculos.png" align="center" height="200" > |
|<img src="/images/03-oculos.png" align="center" height="200" >| <img src="/images/04-oculos.png" align="center" height="200" >|

> Images Source: aquired by the students

---

## Objective

The aim of this project is to "erase" the eyeglasses of photos by filling removed pixels from people's faces. For this, we will use an Image Inpainting Technique Based on the Fast Marching Method. The idea is to replace the glasses estimating the image smoothness as a weighted average over a known image neighborhood of the pixel to inpaint. The algorithm will be implemented in python using the pseudocode provided in article "An Image Inpainting Technique Based on
the Fast Marching Method" - Alexandru Telea, Eindhoven University of Technology.

<br/>

## Input images

<p>An image that is going to be inpainted requires a mask. Based on the article, we decided to divide our work on the following steps:</p>
<ol>
<li> It's going to be our control image in order to inplement the inpainting algorithm;</li>

<br/>

| <img src="/images/fidel-01.png" height="290" /> | <img src="/images/fidel-02.png" height="290" /> |
|:--:|:--:|
| The original image (without<br/>eyeglasses). Source: <a title="Fidel" href="https://commons.wikimedia.org/wiki/Fidel_Castro#/media/File:Fidel_Castro.jpg" target="_blank" rel="noopener">Wikimedia</a> | The masked image. |

<br/>

<li>After the inpainting algorithm is implemented, we are going to use a simple frontal portrait of a person wearing eyeglasses and try to implement an auxiliary algorithm. This algorithm goal is to extract a mask containing only the eyeglasses region on any input image.</li>

<br/>

| <img src="/images/angela-01.png" height="290" /> |
|:--:|
| The original image (with eyeglasses).<br/>Source: <a title="Angela" href="https://commons.wikimedia.org/wiki/File:Angela_Davis_%C3%A0_France_Culture_(Palais_de_Tokyo)_(8586327078).jpg" target="_blank" rel="noopener">Wikimedia</a> (altered) |
</ol>
<br/>

## Methods and Material
