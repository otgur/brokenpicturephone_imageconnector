#python main.py 0.png 1.png 2.png -> out.png

import sys
from PIL import Image

files = sys.argv

count = len(files)-1

#offset image drawing from tower mode
offset = 200
height = 650
width = 600

height = (height-offset)*count

#size of connected image
size = width,height

img = Image.new('RGB', size, color = 'white')

#copy every single-image into the new image
for x in range(count):
    t = Image.open(files[x+1])
    tcopy = t.copy()
    img.paste(tcopy, (0, height - 450*(x+1)))

#save image as out.png
img.save("out.png")