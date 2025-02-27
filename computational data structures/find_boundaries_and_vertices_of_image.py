import cv2
import numpy as np

# Read the segmented image
segmented_image = cv2.imread('building_img.jpg', cv2.IMREAD_GRAYSCALE)

# Threshold the image to get binary image
_, binary_image = cv2.threshold(segmented_image, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a blank image for drawing boundaries
boundary_image = np.zeros_like(segmented_image)

# Draw contours and extract vertices
for idx, contour in enumerate(contours, start=1):
    # Approximate the contour to reduce the number of vertices
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Draw the contour with thicker boundary
    cv2.drawContours(boundary_image, [approx], 0, (255, 255, 255), 4)

    # Print the number of vertices of each polygon
    print(f"Polygon {idx}: Number of vertices = {len(approx)}")
    for i, vertex in enumerate(approx):
        print(f"   Vertex {i+1}: ({vertex[0][0]}, {vertex[0][1]})")

# Display the boundary image
cv2.imshow('Spatial Boundaries', boundary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
