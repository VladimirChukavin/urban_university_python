# Практика. 1.2

from PIL import Image, ImageDraw, ImageFont


def new_photo(name, divider):
    img = Image.open(name)
    w, h = img.size
    return img.resize((w // divider, h // divider))


im = new_photo('image-13.jpg', 2)
im_2 = new_photo('sun.png', 1)

w, h = im.size

im.paste(im_2, (w - 700, h - 500), im_2)

draw = ImageDraw.Draw(im)
font = ImageFont.truetype('arial.ttf', 36)
draw.text((100, 400), 'Hello', font=font, fill='yellow')

im.show('TestPhoto')
