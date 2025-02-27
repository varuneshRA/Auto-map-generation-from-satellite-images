# Import necessary libraries
import cv2 as cv
import matplotlib.pyplot as plt

# Read the input image
img = cv.imread('B05_0.png')

# Convert the image to grayscale
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Display the original and histogram equalized images side by side
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

# Apply histogram equalization to the grayscale image
img = cv.equalizeHist(img)

# Display the histogram equalized image
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('Histogram Equalized Image'), plt.xticks([]), plt.yticks([])

# Show the plots
plt.show()
