import cv2
import numpy as np
import matplotlib.pyplot as plt
from rtree import index

class Rectangle:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

def find_rectangles(segmented_image):
    # Convert segmented image to binary
    binary_image = cv2.threshold(segmented_image, 127, 255, cv2.THRESH_BINARY)[1]

    # Find contours
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    rectangles = []
    # Iterate over contours and create rectangles
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        rectangles.append(Rectangle(x, y, x+w, y+h))

    return rectangles

def create_rtree_index(rectangles):
    p = index.Property()
    idx = index.Index(properties=p)
    for i, rect in enumerate(rectangles):
        idx.insert(i, (rect.left, rect.bottom, rect.right, rect.top))
    return idx

def find_nearest_rectangle_rtree(idx, input_point):
    nearest_rectangle = None
    min_distance = float('inf')

    for rect_id in idx.nearest((input_point[0], input_point[1]), 1):
        rect = rectangles[rect_id]
        rect_center = ((rect.left + rect.right) / 2, (rect.bottom + rect.top) / 2)
        distance = np.sqrt((input_point[0] - rect_center[0])**2 + (input_point[1] - rect_center[1])**2)
        if distance < min_distance:
            min_distance = distance
            nearest_rectangle = rect

    return nearest_rectangle

def plot_rectangles(segmented_image, rectangles, ax, input_point=None, nearest_rectangle=None):
    ax.imshow(segmented_image, cmap='gray')

    for rect in rectangles:
        ax.add_patch(plt.Rectangle((rect.left, rect.bottom), rect.right-rect.left, rect.top-rect.bottom, fill=False, edgecolor='blue'))

    if input_point:
        ax.plot(input_point[0], input_point[1], marker='o', color='red', markersize=5)

    if nearest_rectangle:
        ax.add_patch(plt.Rectangle((nearest_rectangle.left, nearest_rectangle.bottom), nearest_rectangle.right-nearest_rectangle.left, nearest_rectangle.top-nearest_rectangle.bottom, fill=False, edgecolor='green'))

    ax.autoscale_view()
    ax.set_aspect('equal', 'box')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Segmented Image with Rectangles')
    plt.show()

# Example Usage
segmented_image_path = 'eg.png'
input_point = (420, 245)

segmented_image = cv2.imread(segmented_image_path, cv2.IMREAD_GRAYSCALE)

rectangles = find_rectangles(segmented_image)
idx = create_rtree_index(rectangles)

nearest_rectangle = find_nearest_rectangle_rtree(idx, input_point)

fig, ax = plt.subplots()
plot_rectangles(segmented_image, rectangles, ax, input_point=input_point, nearest_rectangle=nearest_rectangle)

print("Nearest Rectangle:", nearest_rectangle.left, nearest_rectangle.bottom, nearest_rectangle.right, nearest_rectangle.top)
