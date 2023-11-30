from PIL import Image

def Grayscale(p):
    image = "hw3_images/" + p + ".jpg"
    im = Image.open(image)
    g_list = g_list = [(
        int((p[0] * 299 + p[1] * 587 + p[2] * 114) // 1000),
        int((p[0] * 299 + p[1] * 587 + p[2] * 114) // 1000),
        int((p[0] * 299 + p[1] * 587 + p[2] * 114) // 1000)
        ) for p in im.getdata()]
    im.putdata(g_list)
    im.show()


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
    image = "hw3_images/" + p + ".jpg"
    im = Image.open(image)
    s_list = [sepia(pixel) for pixel in im.getdata()]
    im.putdata(s_list)
    im.show()
    
def Negative(p):
    image = "hw3_images/" + p + ".jpg"
    im = Image.open(image)
    n_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
    im.putdata(n_list)
    im.show()

def Thumbnail(p):
    image = "hw3_images/" + p + ".jpg"
    im = Image.open(image)
    trgt = im.resize((252,253))
    trgt.show()

def None_(p):
    image = "hw3_images/" + p + ".jpg"
    im = Image.open(image)
    im.show()
