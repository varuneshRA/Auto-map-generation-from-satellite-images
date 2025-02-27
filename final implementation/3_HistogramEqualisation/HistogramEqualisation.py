import cv2 as cv
import os

def process_and_save_images(input_dir, output_dir):
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # Filter for image files
            # Construct the full path for the input image
            input_path = os.path.join(input_dir, filename)

            # Read the input image
            img = cv.imread(input_path)

            # Convert the image to grayscale
            img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            # Apply histogram equalization to the grayscale image
            img_equalized = cv.equalizeHist(img_gray)

            # Construct the full path for the output image
            output_path = os.path.join(output_dir, f"equalized_{filename}")

            # Save the histogram equalized image
            cv.imwrite(output_path, img_equalized)

if __name__ == "__main__":
    # Specify your input directory and output directory
    input_directory = 'InputDir'
    output_directory = 'OutputDir'

    # Process and save the images
    process_and_save_images(input_directory, output_directory)
