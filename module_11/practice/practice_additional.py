# Дополнительный урок по практике

from PIL import Image, ImageDraw, ImageFont


class PostMaker:
    def __init__(self, name_photo, divider=1):
        self.image = Image.open(name_photo)
        self.w, self.h = self.image.size
        self.image = self.image.resize((self.w // divider, self.h // divider))

    def paste(self, name_photo, divider=1):
        paste_image = Image.open(name_photo)
        paste_image = paste_image.resize((paste_image.size[0] // divider, paste_image.size[1] // divider))
        self.image.paste(paste_image, (50, 150), paste_image)

    def insert_text(self, text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('arial.ttf', 36)
        draw.text((100, 350), 'Hello', font=font, fill='yellow')

    def show_photo(self):
        self.image.show()


image = PostMaker('image-13.jpg', 2)
image.paste('sun.png')
image.insert_text('Welcome!')
image.show_photo()
