from PIL import Image
import os

source_folder = 'D:\\Users\\User\\Desktop\\img\\'
destination_folder = 'D:\\Users\\User\\Desktop\\marvelshop\\img\\sticker\\spider-man\\'
directory = os.listdir(source_folder)

for item in directory:
    img = Image.open(source_folder + item)
    imgResize = img.resize((800, 800), Image.ANTIALIAS)
    imgResize.save(destination_folder + item[:-4] + '.webp', quality=90)
