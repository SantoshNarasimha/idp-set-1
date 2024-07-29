import cv2
import numpy as np

# Load the two images
image1 = cv2.imread("C:/Users/santo/Downloads/images.jpeg")
image2 = cv2.imread("C:/Users/santo/Downloads/istockphoto-453237357-612x612.jpg")

# Resize images to have the same dimensions
image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

# Blending factor
alpha = 1

# Blend the images
blended_image = cv2.addWeighted(image1, alpha, image2, (1 - alpha), 0)

# Display the blended image
cv2.imshow('Blended Image', blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
