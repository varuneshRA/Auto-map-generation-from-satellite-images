from skimage.color import rgb2hsv
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Read the input image "img3.png"
img_path = "InputDir/img5.png"
sample = np.array(Image.open(img_path))

# Convert to hsv scale
sample_hsv = rgb2hsv(sample)

# Graph per HSV Channel
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
ax[0].imshow(sample_hsv[:, :, 0], cmap='hsv')
ax[0].set_title('Hue', fontsize=15)
ax[1].imshow(sample_hsv[:, :, 1], cmap='hsv')
ax[1].set_title('Saturation', fontsize=15)
ax[2].imshow(sample_hsv[:, :, 2], cmap='hsv')
ax[2].set_title('Value', fontsize=15)
plt.show()

# Use saturation channel as a mask for segmentation
saturation_mask = sample_hsv[:, :, 1]

# Apply thresholding to create binary mask
saturation_threshold = threshold_otsu(saturation_mask)
segmentation_mask = saturation_mask > saturation_threshold

# Apply the segmentation mask to the original image
segmented_image = np.copy(sample)
segmented_image[~segmentation_mask] = 0  # Set non-segmented regions to black

# Display the results
fig, ax = plt.subplots(1, 4, figsize=(20, 5))
ax[0].imshow(sample)
ax[0].set_title('Original Image', fontsize=15)

ax[1].imshow(saturation_mask, cmap='gray')
ax[1].set_title('Saturation Image', fontsize=15)

ax[2].imshow(segmentation_mask, cmap='gray')
ax[2].set_title('Saturation Binary Mask', fontsize=15)

ax[3].imshow(segmented_image)
ax[3].set_title('Segmented Image', fontsize=15)

plt.tight_layout()
plt.show()
