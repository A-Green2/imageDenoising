# generate an RGB image

from PIL import Image
import numpy as np

# block dimensions of each RGB color block
block_width = 100
block_height = 100
spacing = 0  # no spacing between blocks
total_width = 3 * block_width + 2 * spacing  # total image width
total_height = block_height  # total image height

# array for the image with a white background
image_array = np.ones((total_height, total_width, 3), dtype=np.uint8) * 255

# define colors (RGB)
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

# convert array to image
image = Image.fromarray(image_array)

# save image
image.save('rgb_image.png')

# display the image
image.show()
