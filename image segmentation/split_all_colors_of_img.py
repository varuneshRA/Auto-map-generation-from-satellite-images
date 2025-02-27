import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "mlt.png"  # Replace with the path to your image
image = cv2.imread(image_path)

# Convert the image from BGR to RGB (OpenCV uses BGR by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get unique colors in the image
unique_colors = np.unique(image_rgb.reshape(-1, image_rgb.shape[2]), axis=0)

# Display each color individually in larger size
for i, color in enumerate(unique_colors) :
    # Create a mask for the current color
    mask = np.all(image_rgb == color, axis=-1)

    # Create an image with only the current color
    color_image = np.zeros_like(image_rgb)
    color_image[mask] = color

    # Display the color image
    plt.figure(figsize=(5, 5))  # Set the figure size for each color image
    plt.imshow(color_image)
    plt.title(f"Color {i + 1}")
    plt.axis('off')
    plt.show()
