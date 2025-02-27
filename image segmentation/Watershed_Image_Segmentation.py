import cv2
import numpy as np

# Read the original image
original_image = cv2.imread('../img3.png')

# Read the image for watershed segmentation
image = cv2.imread('../img3.png')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Apply morphological operations to clean the image
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Detect sure background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# Calculate sure foreground area
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# Subtract sure background from sure foreground to get unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Label markers
_, markers = cv2.connectedComponents(sure_fg)

# Add one to all the labels to avoid 0 label (unknown region)
markers = markers + 1

# Mark the unknown region with 0
markers[unknown == 255] = 0

# Apply watershed algorithm
cv2.watershed(image, markers)

# Mark the segmented region with a color
image[markers == -1] = [0, 0, 255]

# Convert segmented image to 3 channels for display
watershed_segmented_colored = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Create a black strip to add a gap
gap = np.zeros((original_image.shape[0], 40, 3), dtype=np.uint8)

# Display the original and segmented images with a gap in between
combined_image = cv2.hconcat([original_image, gap, watershed_segmented_colored])
cv2.imshow('Original vs Watershed Segmented', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
