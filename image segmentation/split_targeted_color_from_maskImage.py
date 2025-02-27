
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "mlt.png"  # Replace with the path to your image
image = cv2.imread(image_path)

# Convert the image from BGR to RGB (OpenCV uses BGR by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the target color
target_color = np.array([240, 2, 127]) # yellow-[253, 192, 134] pink -[240, 2, 127]

# Create a mask for the target color
mask = np.all(image_rgb == target_color, axis=-1)

# Create an image with only the target color
color_image = np.zeros_like(image_rgb)
color_image[mask] = target_color

# Display the color image
plt.imshow(color_image)
plt.title("Target Color")
plt.axis('off')
plt.show()

# Save the segmented image
plt.imsave("mask.png", color_image, cmap='Accent', format='png')
