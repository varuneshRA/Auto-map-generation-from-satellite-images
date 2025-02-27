import cv2
import numpy as np

# Read the original image
original_image = cv2.imread('../img3.png')

# Read the image in grayscale for segmentation
image = cv2.imread('../img3.png', cv2.IMREAD_GRAYSCALE)

# Apply Otsu's thresholding
_, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Convert binary image to 3 channels for display
binary_image_colored = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)

# Create a black strip to add a gap
gap = np.zeros((original_image.shape[0], 40, 3), dtype=np.uint8)

# Display the original and segmented images side by side
combined_image = cv2.hconcat([original_image, gap,binary_image_colored])
cv2.imshow('Original vs otsu image (Threshold)Segmented', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
