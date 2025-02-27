import os
from PIL import Image

def tif_to_png(input_folder, output_folder):
    try:
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Loop through all files in the input folder
        for filename in os.listdir(input_folder):
            if filename.endswith(".tif") or filename.endswith(".tiff"):
                # Construct the input and output file paths
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")

                # Open the TIFF file and save as PNG
                with Image.open(input_path) as img:
                    img.save(output_path, format='PNG')
                print(f"Conversion successful: {input_path} -> {output_path}")

    except Exception as e:
        print(f"Error during conversion: {e}")

# Replace 'input_folder' and 'output_folder' with your folder names
input_folder = 'InputDir/bhuvan'
output_folder = 'OutputDir'

tif_to_png(input_folder, output_folder)
