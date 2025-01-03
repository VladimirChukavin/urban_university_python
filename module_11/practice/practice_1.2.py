# Практика. 1.2

from PIL import Image


def new_photo(name, divider):
    img = Image.open(name)
    w, h = img.size
    return img.resize((w // divider, h // divider))


im = new_photo('image-13.jpg', 2)
im_2 = new_photo('sun.png', 1)
# im.show()
# im_2.show()

im.paste(im_2, (40, 100), im_2)
im.show()
