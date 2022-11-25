import numpy as np
from PIL import Image

fileName = "img\input.jpeg"
img = Image.open(fileName)

print(img.mode)
# (r,c) = img.size

# Generate a checkerboard pattern B of size R × C
# B = np.indices((r,c)).sum(axis=0) % 2
