import os
import cv2
import matplotlib.pyplot as plt

def process_and_save_images(input_dir, output_dir):
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # Filter for image files
            # Construct the full path for the input image
            input_path = os.path.join(input_dir, filename)

            # Reading the image
            image = cv2.imread(input_path)

            # Changing the color space
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Construct the full path for the output image
            output_path = os.path.join(output_dir, f"gray_{filename}")

            # Saving the resultant image
            cv2.imwrite(output_path, gray_image)

if __name__ == "__main__":
    # Specify your input and output directories
    input_directory = 'InputDir'
    output_directory = 'OutputDir'

    # Process and save images
    process_and_save_images(input_directory, output_directory)
