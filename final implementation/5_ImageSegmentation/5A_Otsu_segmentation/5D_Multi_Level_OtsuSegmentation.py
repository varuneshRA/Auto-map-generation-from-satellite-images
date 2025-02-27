import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import threshold_multiotsu

def process_and_save_image(input_path, output_path):
    # Read an image
    image = cv2.imread(input_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply multi-Otsu threshold
    thresholds = threshold_multiotsu(gray_image, classes=4)

    # Digitize (segment) original image into multiple classes.
    regions = np.digitize(gray_image, bins=thresholds)

    # Convert to uint8
    output = regions.astype(np.uint8)

    # Save the figure with the same basename as the input image
    output_figure_path = os.path.join(output_path)

    # Save the segmented image
    plt.imsave(output_figure_path, output, cmap='Accent', format='png')

    plt.close()  # Close the figure to avoid displaying it

def process_images_in_directory(input_directory, output_directory):
    # Process each file in the input directory and its subdirectories
    for root, dirs, files in os.walk(input_directory):
        for filename in files:
            if filename.endswith(".png"):  # You can adjust the file extension as needed
                input_path = os.path.join(root, filename)

                # Generate corresponding output subdirectory structure
                relative_path = os.path.relpath(root, input_directory)
                output_subdirectory = os.path.join(output_directory, relative_path)

                # If the file is in a subdirectory, create the subdirectory in the output path
                if relative_path != '.':
                    os.makedirs(output_subdirectory, exist_ok=True)

                # Corrected output file path
                output_path = os.path.join(output_subdirectory, f"output_{filename}")
                process_and_save_image(input_path, output_path)
                print(f"{filename} is processed and saved")

# Example usage:
input_directory = "InputDir"
output_directory = "OutputDir"
process_images_in_directory(input_directory, output_directory)
