# generate a noisy RGB image

from PIL import Image
import numpy as np

# block dimensions of each RGB color block
block_width, block_height = 100, 100
spacing = 0  # no spacing between blocks
total_width = 3 * block_width + 2 * spacing  # total image width
total_height = block_height  # total image height

# array for the image with a white background
image_array = np.ones((total_height, total_width, 3), dtype=np.uint8) * 255

# list to define colors (RGB)
colors = [
    [255, 0, 0],    # Red
    [0, 255, 0],    # Green
    [0, 0, 255]     # Blue
]

# fill in color blocks
for i in range(len(colors)):
    color = colors[i]
    start_x = i * (block_width + spacing)
    end_x = start_x + block_width
    image_array[:, start_x:end_x] = color
    
# generate random noise
# noise = np.random.randint(0, 10, (total_height, total_width, 3), dtype=np.uint8)

# add noise to image array
# noisy_image_array = image_array + noise
noisy_image_array = image_array


# clip values that fall out of [0, 255] range
noisy_image_array = np.clip(noisy_image_array, 0, 255)

# convert array to image
noisy_image = Image.fromarray(noisy_image_array.astype(np.uint8))

# access pixels
pixels = noisy_image.load()

# get height and width of image
height = noisy_image.height
width = noisy_image.width

# calculate the total number of pixels in the image = height * width
total_num_pixels = height * width
print(total_num_pixels)

# random number of pixels to swap
num_swaps = np.random.randint(0, total_num_pixels)
# num_swaps = 100
print(num_swaps)

# loop through the number of pixels to swap
for i in range(num_swaps):
    
    # pick a random pixel where x is the image width and y is the image height
    x = np.random.randint(0, noisy_image.size[0])
    y = np.random.randint(0, noisy_image.size[1])
    
    # extract the current color of that pixel
    current_color = pixels[x, y]
    
    # variable to hold the remaining colors to swap
    remaining_colors = []
    
    # iterate over colors list
    for j in range(len(colors)):
        
        # check if current pixel color is not equal to any colors in the list
        if current_color[0] != colors[j][0] or current_color[1] != colors[j][1] or current_color[2] != colors[j][2]:
            
            # add that color to the remaining colors for that specific pixel
            remaining_colors.append(colors[j])
            
    # pick a random color from the remaining colors list
    rand_color = remaining_colors[np.random.randint(0, len(remaining_colors))]
    pixels[x, y] = tuple(rand_color)          

# save image
noisy_image.save('noisy_rgb_image.png')

# display the image
noisy_image.show()

# instead of generating random black particles, pick random pixels, check what color it is, then swap it for either of the remaining colors
# use PixelAccess class to read and write access to PIL.Image data at a pixel level
# Note: accessing individual pixels is fairly slow - look for other methods
# refs: https://pillow.readthedocs.io/en/stable/reference/PixelAccess.html, https://stackoverflow.com/questions/36468530/changing-pixel-color-value-in-pil

