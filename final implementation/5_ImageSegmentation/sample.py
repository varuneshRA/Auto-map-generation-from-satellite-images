import cv2
import os
import matplotlib.pyplot as plt


# Function to read images from directories
def read_images_from_directories(directory_paths) :
    images = []
    for directory in directory_paths :
        directory_images = []
        for filename in os.listdir(directory) :
            if filename.endswith(".jpg") or filename.endswith(".png") :
                img = cv2.imread(os.path.join(directory, filename))
                directory_images.append(img)
        images.append(directory_images)
    return images


# Function to save images to a directory with titles and layout
def save_images_to_directory(output_directory, images) :
    os.makedirs(output_directory, exist_ok=True)
    fig, axes = plt.subplots(3, 2, figsize=(12, 8))

    for i, image_set in enumerate(images) :
        row = i // 2
        col = i % 2
        output_image = cv2.hconcat(image_set)
        axes[row, col].imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
        axes[row, col].axis('off')
        axes[row, col].set_title(f"Image {i + 1}")

    plt.tight_layout()
    plt.savefig(os.path.join(output_directory, "output_images.jpg"))


# Input directories
input_directories = [
    "Segmentation_results\Input_Dataset",
    "Segmentation_results\Ouput_MultiOtsu_Segmentation",
    "Segmentation_results\Output_Watershed_Segmentation",
    "Segmentation_results\OutputAnalysis\Multi_Otsu_Seg\Mask1Img",
    "Segmentation_results\OutputAnalysis\Multi_Otsu_Seg\Mask2Img",
    "Segmentation_results\OutputAnalysis\Multi_Otsu_Seg\Mask3Img",
    "Segmentation_results\OutputAnalysis\Multi_Otsu_Seg\Mask4Img"
]

# Output directory
output_directory = "output_images"

# Read images from directories
images = read_images_from_directories(input_directories)

# Save images to output directory
save_images_to_directory(output_directory, images)
