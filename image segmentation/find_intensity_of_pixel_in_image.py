import cv2
import numpy as np
from PIL import Image

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the intensity of the pixel at the clicked coordinates
        pixel_intensity = get_pixel_intensity(x, y)
        print(f"Pixel Intensity at ({x}, {y}): {pixel_intensity}")

def get_pixel_intensity(x, y):
    # Get the intensity of the pixel at the specified coordinates
    pixel_intensity = image.getpixel((x, y))

    return pixel_intensity

# Replace 'your_image_path.jpg' with the path to your image file
image_path = 'mlt.png'

# Open the image using Pillow
image = Image.open(image_path)

# Convert the image to RGB if it's not already in that format
if image.mode != 'RGB':
    image = image.convert('RGB')

# Create a window and set the mouse callback
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", on_mouse)

while True:
    frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imshow("Image", frame)

    # Break the loop if the 'ESC' key is pressed
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
