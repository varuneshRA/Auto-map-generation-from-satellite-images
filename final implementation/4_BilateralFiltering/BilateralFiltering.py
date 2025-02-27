import cv2
import os
import matplotlib.pyplot as plt

def bilateral_filtering_and_save(input_dir, output_dir, d, sigma_color, sigma_space):
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # Filter for image files
            # Construct the full path for the input image
            input_path = os.path.join(input_dir, filename)

            # Read the input image
            image = cv2.imread(input_path)

            # Apply bilateral filter
            filtered_image = cv2.bilateralFilter(image, d, sigma_color, sigma_space)

            # Construct the full path for the output image
            output_path = os.path.join(output_dir, f"bilateral_filtered_{filename}")

            # Save the bilateral filtered image
            cv2.imwrite(output_path, filtered_image)

if __name__ == "__main__":
    # Specify your input directory and output directory
    input_directory = 'InputDir'
    output_directory = 'OutputDir'

    # Specify the parameters for bilateral filtering
    # Adjust these parameters based on your requirements
    diameter = 10  # Diameter of each pixel neighborhood
    sigma_color = 35  # Filter sigma in the color space
    sigma_space = 50  # Filter sigma in the coordinate space

    # Apply bilateral filtering and save the images
    bilateral_filtering_and_save(input_directory, output_directory, diameter, sigma_color, sigma_space)
