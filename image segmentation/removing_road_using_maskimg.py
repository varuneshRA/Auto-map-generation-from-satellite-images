import cv2
from PIL import Image
import numpy as np

def multiply_color_with_binary(color_path, binary_path):
    # Open the images
    binary_image = cv2.imread(binary_path, cv2.IMREAD_GRAYSCALE)

    color_image = Image.open(color_path)

    # Convert images to numpy arrays for easier manipulation
    color_array = np.array(color_image)
    binary_array = np.array(binary_image)

    # Set white regions in binary image to zero
    color_array[binary_array == 0] = 0 # 255 is white color and 0 is black color

    # Create a new image from the modified array
    result_image = Image.fromarray(color_array)

    # Display the result
    result_image.show()

    # Save the result
    result_image.save("building.png")


if __name__ == "__main__":
    # Provide the paths to your color and binary images
    color_image_path = "img5.png"
    binary_image_path = "mask.png"

    # Perform the operation and display the result
    multiply_color_with_binary(color_image_path, binary_image_path)
