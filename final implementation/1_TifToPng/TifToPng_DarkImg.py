from PIL import Image, ImageSequence
import os
import numpy as np

# Function to convert a single image page
def convert(im):
    # Convert the image page to a NumPy array
    imarray = np.array(im)

    # Normalize the pixel values to the range [0, 255]
    img = (np.maximum(imarray, 0) / imarray.max()) * 255.0

    # Invert the pixel values
    img = 255 - img

    # Convert the NumPy array back to an image
    img = Image.fromarray(np.uint8(img))

    return img

# Specify the root directory where you want to search for TIF images
root_directory = "InputDir/bhuvan"

# Walk through the directory and its subdirectories
for root, dirs, files in os.walk(root_directory):
    for file in files:
        # Check if the file has a .tif extension (case-insensitive)
        if file.lower().endswith(".tif"):
            # Construct the full path to the TIFF file
            tif_file = os.path.join(root, file)
            try:
                # Open the TIFF image
                image = Image.open(tif_file)

                # Extract filename without extension and folder name
                filename = os.path.splitext(file)[0]
                folder_name = os.path.basename(root)

                # Create an output folder for the PNG images (if it doesn't exist)
                output_folder = "OutputDir"

                # Iterate through all pages in the TIFF image
                for i, page in enumerate(ImageSequence.Iterator(image)):
                    # Construct the path for the PNG file
                    png_path = os.path.join(output_folder, f"{filename}_{i}.png")

                    # Check if the PNG file doesn't already exist
                    if not os.path.isfile(png_path):
                        try:
                            # Convert the current page using the convert function
                            img = convert(page)

                            # Save the converted image as a PNG
                            img.save(png_path)
                            print(f"Converted {tif_file} to {png_path}")
                        except Exception as e:
                            print(f"Error saving {png_path}: {e}")
            except Exception as e:
                print(f"Error processing {tif_file}: {e}")
