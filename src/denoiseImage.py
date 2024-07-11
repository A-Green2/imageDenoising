from PIL import Image
import numpy as np
import random
import math

# function to evaluate the likelihood of a pixel's color
def calculate_phi(actual_pixel_value, expected_pixel_value, sigma):
    numerator = -1 * math.pow((actual_pixel_value - expected_pixel_value))
    x = math.exp(numerator / math.pow(sigma))
    return x

#  RGB color list
RGB_colors = [
    [225, 0, 0],
    [0, 225, 0],
    [0, 0, 225]
]


# open image
with Image.open('noisy_rgb_image.png') as im:
    
    # access individual pixel values
    pixel = im.load()

# get width and height of image
width = im.width
height = im.height

mean_deviation = 5

# iterate through each pixel
for w in range(width):
    for h in range(height):
        
        # calculate phi
        phi = calculate_phi(pixel[w, h], RGB_colors, mean_deviation)