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
    
# generate random noise
noise = np.random.randint(0, 10, (total_height, total_width, 3), dtype=np.uint8)

# instead of generating random black particles, pick random pixels, check what color it is, then swap it for either of the remaining colors

# add noise to image array
noisy_image_array = image_array + noise

# clip values that fall out of [0, 255] range
noisy_image_array = np.clip(noisy_image_array, 0, 255)

# convert array to image
noisy_image = Image.fromarray(noisy_image_array.astype(np.uint8))

# save image
noisy_image.save('noisy_rgb_image.png')

# display the image
noisy_image.show()
