import os

from skimage.color import rgb2hsv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Read the input image "img3.png"
img_path = "InputDir/img3.png"
sample = np.array(Image.open(img_path))

# Convert to hsv scale
sample_hsv = rgb2hsv(sample)

# Extract the saturation channel
saturation_image = (sample_hsv[:, :, 1] * 255).astype(np.uint8)

# Save the saturation image as "img6.png"
output_path = f"OutputDir/saturated_{os.path.basename(img_path)}"
Image.fromarray(saturation_image).save(output_path)


# Display the results
fig, ax = plt.subplots(1, 2, figsize=(15, 5))
ax[0].imshow(sample)
ax[0].set_title('Original Image', fontsize=15)

ax[1].imshow(saturation_image, cmap='gray')
ax[1].set_title('Saturation Image', fontsize=15)

plt.tight_layout()
plt.show()
