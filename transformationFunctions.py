from PIL import Image
import numpy as np
import os

def scaling_fewer_pixels(your_image):
    my_src = Image.open(your_image)
    w, h = my_src.width // 2, my_src.height // 2
    my_trgt = Image.new('RGB', (w, h))

    target_x = 0
    for source_x in range(0, my_src.width, 2):
        target_y = 0
        for source_y in range(0, my_src.height, 2):
            p = my_src.getpixel((source_x, source_y))
            my_trgt.putpixel((target_x, target_y), p)
            target_y += 1
        target_x += 1

    # my_trgt.show()
    transformed_path = os.path.join("static/images", "transformed_image_scaling_fewer_pixels.jpg")
    my_trgt.save(transformed_path)

    return transformed_path


def scaling_up(your_image):
    my_src = Image.open(your_image)
    mf = 2
    w, h = my_src.width * mf, my_src.height * mf

    my_trgt = Image.new('RGB', (w, h))
    target_x = 0
    for source_x in np.repeat(range(my_src.width), mf):
        target_y = 0
        for source_y in np.repeat(range(my_src.height), mf):
            p = my_src.getpixel((int(source_x), int(source_y)))
            my_trgt.putpixel((target_x, target_y), p)
            target_y += 1
        target_x += 1

    # my_trgt.show()
    transformed_path = os.path.join("static/images", "transformed_image_scaling_up.jpg")
    my_trgt.save(transformed_path)

    return transformed_path

