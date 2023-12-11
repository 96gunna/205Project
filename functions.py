from PIL import Image
import os

def Grayscale(p):
    image = p
    im = Image.open(image)
    w, h = im.width, im.height
    my_trgt = Image.new('RGB', (w, h))
    g_list = g_list = [(
        int((p[0] * 299 + p[1] * 587 + p[2] * 114) // 1000),
        int((p[0] * 299 + p[1] * 587 + p[2] * 114) // 1000),
        int((p[0] * 299 + p[1] * 587 + p[2] * 114) // 1000)
        ) for p in im.getdata()]
    im.putdata(g_list)

    # output_path = os.path.join("static/images", "grayscaleEdit.jpg")
    output_path = os.path.join("static/images", "grayscaleEdit.jpg")
    my_trgt.save(output_path)
    return output_path
   


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
    w, h = im.width, im.height
    my_trgt = Image.new('RGB', (w, h))
    s_list = [sepia(pixel) for pixel in im.getdata()]
    im.putdata(s_list)
    output_path = os.path.join("static/images", "sepiaEdit.jpg")
    my_trgt.save(output_path)
    return  output_path
    
def Negative(p):
    image = p
    im = Image.open(image)
    w, h = im.width, im.height
    my_trgt = Image.new('RGB', (w, h))
    n_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
    im.putdata(n_list)
    output_path = os.path.join("static/images", "NegativeEdit.jpg")
    my_trgt.save(output_path)
    return output_path

def Thumbnail(p):
    image = p
    im = Image.open(image)
    w, h = im.width, im.height
    my_trgt = Image.new('RGB', (w, h))
    im.resize((252,253))
    output_path = os.path.join("static/images", "thumbnailEdit.jpg")
    my_trgt.save(output_path)
    return output_path
