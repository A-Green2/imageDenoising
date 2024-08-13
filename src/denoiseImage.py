from PIL import Image
import numpy as np
import random
import math

# TODO: create another data structure thats image height and width * 3 -> 3 because RGB are the classes
# store phi values for each pixel with respect to each class
# phi = what I think I should be based off what I see
# message = what my neighbor thinks I should be based off what they see
def new_image(original_image_width, original_image_height):
    new_image_width = original_image_width * 3
    new_image_height = original_image_height * 3
    # new_image = new_image_width * new_image_height
    
    # array for the image with a white background
    image_array = np.ones((new_image_height, new_image_width, 3), dtype=np.uint8) * 255

    return image_array


# function to evaluate the likelihood of a pixel's color
# evaluate phi for all 3 colors store in data structure above - take the best/highest value 
def calculate_phi(actual_pixel_value, expected_pixel_value, sigma):

    # initialize variable holding numerator of function
    pixel_diff = ()
    
    # calculate difference between the pixel's actual value and the RGB value
    pixel_diff = (actual_pixel_value[0] - expected_pixel_value[0], 
                  actual_pixel_value[1] - expected_pixel_value[1], 
                  actual_pixel_value[2] - expected_pixel_value[2]
                  )
    
    # finish calculating the numerator by negating pixel_diff and squaring each component
    numerator = -1 * (math.pow(pixel_diff[0], 2) + 
                      math.pow(pixel_diff[1], 2) + 
                      math.pow(pixel_diff[2], 2)
                      )
    
    # apply the numerator to the power of e
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

# get width and height of image
width = im.width
height = im.height

# initialize the variance, sigma
mean_deviation = 5

# initialize list to store phi values
# initialize array storing phi values for each pixel's RGB values
phi_values_list = np.zeros((width, height, 3))

# iterate through each pixel
# print(width)
for w in range(width):
    # print("w: ", w)
    # phi_values_list[w] = []
    
    for h in range(height):
        # phi_values_list[w][h]= []
        
        # iterate over colors
        for i in range(len(RGB_colors)):
            
            # convert pixel list to pixel tuple
            pixel[w, h] = tuple(pixel[w, h])
            
            # print("pixel: ", pixel[w, h])
            
            # calculate phi 
            phi = calculate_phi(pixel[w, h], RGB_colors[i], mean_deviation)
            # print("phi: ", phi)
            # print(f"phi for pixel ({w}, {h}) and color {RGB_colors[i]}: {phi}")
            # TODO: save as list then convert to tuple
            # phi_values_list[w][h][i] = phi
            phi_values_list[w][h] = phi

# print("phi list: ", phi)

# iterate over the phi of each pixel
# for p in phi_values_list:
    