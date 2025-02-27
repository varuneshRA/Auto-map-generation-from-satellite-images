import os

import cv2
import matplotlib.pyplot as plt

def convert_to_binary(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Use Otsu's thresholding to automatically determine the threshold
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


    # Save the binary image
    cv2.imwrite(output_path, binary_image)

    # Display the original and binary images
    plt.subplot(121), plt.imshow(image, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(binary_image, cmap='gray')
    plt.title('Binary Image (Otsu)'), plt.xticks([]), plt.yticks([])
    plt.show()

# Example usage
image_path = 'InputDir/img3.png'
output_path = f"OutputDir/binary_{os.path.basename(image_path)}"
convert_to_binary(image_path, output_path=output_path)
