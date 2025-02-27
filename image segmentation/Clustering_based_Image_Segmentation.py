import cv2
import numpy as np

# Read the original image
original_image = cv2.imread('../img5.png')

# Read the image for clustering segmentation
image = cv2.imread('../img5.png')

# Reshape the image to a 2D array of pixels
pixels = image.reshape((-1, 3))

# Convert to float32
pixels = np.float32(pixels)

# Define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 3  # Number of clusters
_, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert back to 8-bit values
centers = np.uint8(centers)
segmented_image = centers[labels.flatten()]

# Reshape back to the original image dimensions
segmented_image = segmented_image.reshape(image.shape)

# Convert segmented image to 3 channels for display
segmented_image_colored = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB)

# Create a black strip to add a gap
gap = np.zeros((original_image.shape[0], 40, 3), dtype=np.uint8)

# Display the original and segmented images with a gap in between
combined_image = cv2.hconcat([original_image, gap, segmented_image_colored])
cv2.imshow('Original vs Clustering Segmented', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
