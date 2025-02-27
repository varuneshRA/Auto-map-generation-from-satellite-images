import cv2
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os

def watershed_segmentation(input_folder):
    try:
        # Get the current working directory
        root = os.getcwd()

        # Create an output folder for segmented images
        output_folder = 'OutputDir/output_segmented'
        os.makedirs(output_folder, exist_ok=True)

        # Get a list of all files in the input folder
        image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

        for image_file in image_files:
            # Read the input image in BGR format
            img_path = os.path.join(input_folder, image_file)
            img = cv.imread(img_path)

            # Convert the image to RGB for matplotlib display
            imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

            # Convert the image to grayscale
            img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            # Apply thresholding to create a binary image
            _, imgThreshold = cv.threshold(img_gray, 120, 255, cv.THRESH_BINARY_INV)

            # Invert the binary image
            imgThreshold = cv2.bitwise_not(imgThreshold)

            # Apply morphological dilation
            kernel = np.ones((3, 3), np.uint8)
            imgDilate = cv.morphologyEx(imgThreshold, cv.MORPH_DILATE, kernel)

            # Compute distance transform
            distTrans = cv.distanceTransform(imgDilate, cv.DIST_L2, 5)

            # Threshold the distance transform
            _, distThresh = cv.threshold(distTrans, 5, 255, cv.THRESH_BINARY)

            # Convert to uint8 and find connected components
            distThresh = np.uint8(distThresh)
            _, labels = cv.connectedComponents(distThresh)

            # Apply watershed algorithm
            labels = np.int32(labels)
            labels = cv.watershed(imgRGB, labels)

            # Highlight watershed boundaries on the original image
            imgRGB[labels == -1] = [255, 0, 0]

            # Save the segmented image
            output_path = os.path.join(output_folder, f"{os.path.splitext(image_file)[0]}_segmented.png")
            cv.imwrite(output_path, cv.cvtColor(imgRGB, cv.COLOR_RGB2BGR))
            print(f"Segmentation successful for: {img_path} -> {output_path}")

    except Exception as e:
        print(f"Error during segmentation: {e}")

    # Display the figures
    plt.show()

if __name__ == '__main__':
    # Replace 'input_folder' with the path to your input folder
    input_folder = 'InputDir/Dataset'
    watershed_segmentation(input_folder)
