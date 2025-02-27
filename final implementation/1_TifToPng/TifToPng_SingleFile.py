# Import necessary libraries
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

# Open a TIFF image and convert it to a NumPy array
im = Image.open('sample_tiffr.tif')
imarray = np.array(im)

# Display the original image using Matplotlib
plt.imshow(imarray)
plt.show()  # To see how the TIFF file looks like

# Normalize the pixel values to the range [0, 255]
img = (np.maximum(imarray, 0) / imarray.max()) * 255.0

# Invert the pixel values
img = 255 - img

# Convert the NumPy array back to an image and save it as a PNG file
img = Image.fromarray(np.uint8(img))
img.save('imgg.png')
