from PIL import Image
import numpy as np
import random
import math

# open image
with Image.open('noisy_rgb_image.png') as im:
    
    # access individual pixel values
    pixel = im.load()

# get width and height of image
width = im.width
height = im.height

# iterate through each pixel
for w in range(width):
    for h in range(height):
        # calculate PHI