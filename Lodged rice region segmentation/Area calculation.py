import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = ''
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image loading failed")
    exit()

white_value = 255
white_pixel_count = np.sum(image == white_value)
total_pixel_count = image.size

white_area_ratio = white_pixel_count / total_pixel_count

plt.imshow(image, cmap='gray')
plt.title(f"Image: {image_path}\nWhite Area Ratio: {white_area_ratio:.2%}")
plt.axis('off')
plt.show()