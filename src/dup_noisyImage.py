from PIL import Image

with Image.open('noisy_rgb_image.png') as im:
    pixel = im.load()
print(pixel[200, 0])