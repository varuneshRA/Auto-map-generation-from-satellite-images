import cv2
import matplotlib.pyplot as plt

def bilateral_filtering(image_path,d, sigma_color, sigma_space):
    # Read the input image
    image = cv2.imread(image_path)

    # Apply bilateral filter
    filtered_image = cv2.bilateralFilter(image, d, sigma_color, sigma_space)

    #display the image
    plt.subplot(121), plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
    plt.title('bilateral filtered Image'), plt.xticks([]), plt.yticks([])
    plt.show()


# Specify the path to the input image
input_image_path = "result_1_2.png"

# Specify the parameters for bilateral filtering
# Adjust these parameters based on your requirements
diameter = 100  # Diameter of each pixel neighborhood
sigma_color = 100 # Filter sigma in the color space
sigma_space = 100  # Filter sigma in the coordinate space


# Apply bilateral filtering
bilateral_filtering(input_image_path,diameter, sigma_color, sigma_space)
