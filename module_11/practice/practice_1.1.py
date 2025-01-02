# Практика. 1.1

from PIL import Image

im = Image.open('image-13.jpg')
print(im.format, im.size, im.mode)
# im.show()

# print(dir(Image))

out = im.resize((100, 100))
# out.show()