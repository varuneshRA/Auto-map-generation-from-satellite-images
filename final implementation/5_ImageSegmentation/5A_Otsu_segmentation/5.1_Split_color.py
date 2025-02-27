import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Input and output directories
input_directory = "OutputDir/Dataset"
output_directory = "OutputAnalysis/Mask4Img"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# List all files in the input directory
files = os.listdir(input_directory)

# Process each file in the input directory
for file in files:
    # Check if the file is an image (you may want to add more checks based on file extension)
    if file.lower().endswith(('.png')):
        # Construct the full path to the input image
        image_path = os.path.join(input_directory, file)
        image = cv2.imread(image_path)

        # Convert the image from BGR to RGB (OpenCV uses BGR by default)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Define the target color
        target_color = np.array([102,102,102])  # yellow-[253, 192, 134] pink -[240, 2, 127] green-[127,201,127] black -[102,102,102]

        # Create a mask for the target color
        mask = np.all(image_rgb == target_color, axis=-1)

        # Create an image with only the target color
        color_image = np.zeros_like(image_rgb)
        color_image[mask] = target_color


        # Save the segmented image to the output directory
        output_path = os.path.join(output_directory, f"MaskImg_{file}")
        plt.imsave(output_path, color_image, cmap='Accent', format='png')
        print(f"{file} processed")

print("Segmentation complete. Segmented images saved in the output directory.")
