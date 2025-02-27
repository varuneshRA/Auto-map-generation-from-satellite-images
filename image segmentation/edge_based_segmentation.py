import cv2
import numpy as np

# Read the original image
original_image = cv2.imread('img3.png')

# Read the image for edge-based segmentation
image = cv2.imread('img3.png', cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
edges = cv2.Canny(image, 100, 200)

# Convert edges image to 3 channels for display
edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Create a black strip to add a gap
gap = np.zeros((original_image.shape[0], 40, 3), dtype=np.uint8)

# Display the original and segmented images with a gap in between
combined_image = cv2.hconcat([original_image, gap, edges_colored])
cv2.imshow('Original vs Edge-based Segmented', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
