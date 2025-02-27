import cv2
import matplotlib.pyplot as plt

def convert_to_binary(image_path, threshold_value=40, output_path='img7.png'):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply binary thresholding
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Save the binary image
    cv2.imwrite(output_path, binary_image)

    # Display the original and binary images
    plt.subplot(121), plt.imshow(image, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(binary_image, cmap='gray')
    plt.title('Binary Image'), plt.xticks([]), plt.yticks([])
    plt.show()

# Example usage
image_path = 'mask.png'
output_path = 'img6.png'
convert_to_binary(image_path, output_path=output_path)
