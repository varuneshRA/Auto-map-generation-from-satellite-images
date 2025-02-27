import cv2
from PIL import Image
import numpy as np
import os

def multiply_color_with_binary(color_folder, binary_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # List all files in both color and binary folders
    color_files = sorted(os.listdir(color_folder))
    binary_files = sorted(os.listdir(binary_folder))

    # Iterate over both lists simultaneously
    for color_file, binary_file in zip(color_files, binary_files):
        # Check if the files are images (you may want to add more checks based on file extension)
        if color_file.lower().endswith(('.png',)) and binary_file.lower().endswith(('.png')):
            # Construct the full paths to the color and binary images
            color_image_path = os.path.join(color_folder, color_file)
            binary_image_path = os.path.join(binary_folder, binary_file)

            # Open the images
            binary_image = cv2.imread(binary_image_path, cv2.IMREAD_GRAYSCALE)
            color_image = Image.open(color_image_path)

            # Convert images to numpy arrays for easier manipulation
            color_array = np.array(color_image)
            binary_array = np.array(binary_image)

            # Set white regions in binary image to zero
            color_array[binary_array == 0] = 0

            # Create a new image from the modified array
            result_image = Image.fromarray(color_array)

            # Save the result to the output folder
            output_path = os.path.join(output_folder, f"result_{color_file}")
            result_image.save(output_path)

            print(f"Processed {color_file}")

if __name__ == "__main__":
    # Provide the paths to your color and binary image folders and the output folder
    color_folder_path = "InputDir/Dataset"
    binary_folder_path = "OutputAnalysis/MaskImg"
    output_folder_path = "OutputAnalysis/Buildings_from _mask"

    # Perform the operation and save the results
    multiply_color_with_binary(color_folder_path, binary_folder_path, output_folder_path)
