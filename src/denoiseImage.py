from PIL import Image
import numpy as np
import random
import math

# TODO: create another data structure thats image height and width * 3 -> 3 because RGB are the classes

# function to evaluate the likelihood of a pixel's color
# evaluate phi for all 3 colors store in data structure above - take the best/highest value 
def calculate_phi(actual_pixel_value, expected_pixel_value, sigma):
    # TODO: access individual elements of pixels values
    # TODO: ensure numerator computes the dot product
    # TODO: call function using example values to check function
    # numerator = -1 * math.pow((actual_pixel_value - expected_pixel_value), 2)
    pixel_diff = ()
    pixel_diff = (actual_pixel_value[0] - expected_pixel_value[0], actual_pixel_value[1] - expected_pixel_value[1], actual_pixel_value[2] - expected_pixel_value[2])
    numerator = -1 * (math.pow(pixel_diff[0], 2) + math.pow(pixel_diff[1], 2) + math.pow(pixel_diff[2], 2))
    x = math.exp(numerator / math.pow(sigma, 2))
    return x

#  tuple of RGB colors
RGB_colors = [
    [225, 0, 0],
    [0, 225, 0],
    [0, 0, 225]
]

# open image
with Image.open('noisy_rgb_image.png') as im:
    
    # access individual pixel values - list datatype
    pixel = im.load()
    
print(tuple(pixel[0, 0]))

# get width and height of image
width = im.width
height = im.height

mean_deviation = 5

# iterate through each pixel
for w in range(width):
    for h in range(height):
        
        # iterate over colors
        for i in range(len(RGB_colors)):
            
            # convert pixel list to pixel tuple
            pixel[w, h] = tuple(pixel[w, h])
            
            print("pixel: ", pixel[w, h])
            
            # calculate phi
            phi = ()
            phi = calculate_phi(pixel[w, h], RGB_colors[i], mean_deviation)
            