import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(image_path, threshold_value=127, noise_removal_kernel=3):
    # Read the color image
    color_image = cv2.imread(image_path)

    # Convert to grayscale
    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

    # Define the kernel for morphological operations
    kernel = np.ones((noise_removal_kernel, noise_removal_kernel), np.uint8)

    # Apply erosion followed by dilation to remove noise
    cleaned_binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)

    return color_image, binary_image, cleaned_binary_image

def detect_buildings(image, cleaned_image):
    # Find contours in the cleaned binary image
    contours, _ = cv2.findContours(cleaned_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    building_boundaries_image = image.copy()
    cv2.drawContours(building_boundaries_image, contours, -1, (0, 255, 0), thickness=2)

    return building_boundaries_image

def segment_and_detect(image_path, threshold_value=127, noise_removal_kernel=3):
    # Preprocess the image
    color_image, binary_image, cleaned_binary_image = preprocess_image(image_path, threshold_value, noise_removal_kernel)

    # Detect buildings and draw boundaries on the color image
    building_boundaries_image = detect_buildings(color_image, cleaned_binary_image)

    # Display the original, binary, and building-boundaries images
    plt.subplot(131), plt.imshow(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(132), plt.imshow(binary_image, cmap="gray")
    plt.title('Binary Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(133), plt.imshow(cv2.cvtColor(building_boundaries_image, cv2.COLOR_BGR2RGB))
    plt.title('Building Boundaries'), plt.xticks([]), plt.yticks([])

    plt.show()

# Example usage
image_path = 'img2.png'
segment_and_detect(image_path)
