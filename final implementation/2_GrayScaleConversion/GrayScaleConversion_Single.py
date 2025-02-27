
import matplotlib.pyplot as plot
import cv2

# reading the image
image = cv2.imread('InputDir/')

# changing the color space
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# showing the resultant image
plot.imshow(gray_image,cmap="gray")
plot.show()
