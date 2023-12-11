from PIL import Image
import os

def Grayscale(p):
    image = p
    im = Image.open(image)
    g_list = g_list = [(
        int((p[0] * 299 + p[1] * 587 + p[2] * 114) // 1000),
        int((p[0] * 299 + p[1] * 587 + p[2] * 114) // 1000),
        int((p[0] * 299 + p[1] * 587 + p[2] * 114) // 1000)
        ) for p in im.getdata()]
    im.putdata(g_list)

    output_path = os.path.join("static", "grayscaleEdit.jpg")
    im.save(output_path)
    return "grayscaleEdit.jpg"
   


def sepia(p):
   if p[0] < 63:
       r,g,b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
   elif p[0] > 62 and p[0] < 192:
       r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
   else:
       r = int(p[0] * 1.08)
       g,b = p[1], int(p[2] * 0.5)
      
   return r, g, b

def Sepia(p):
    image = p
    im = Image.open(image)
    s_list = [sepia(pixel) for pixel in im.getdata()]
    im.putdata(s_list)
    output_path = os.path.join("static", "sepiaEdit.jpg")
    im.save(output_path)
    return  "sepiaEdit.jpg"
    
def Negative(p):
    image = p
    im = Image.open(image)
    n_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
    im.putdata(n_list)
    output_path = os.path.join("static", "NegativeEdit.jpg")
    im.save(output_path)
    return "NegativeEdit.jpg"

def Thumbnail(p):
    image = p
    im = Image.open(image)
    im.resize((252,253))
    output_path = os.path.join("static", "thumbnailEdit.jpg")
    im.save(output_path)
    return "thumbnailEdit.jpg"

