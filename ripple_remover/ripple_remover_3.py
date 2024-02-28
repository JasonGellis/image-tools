# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('your_image_path.jpg')  # Replace 'your_image_path.jpg' with the actual path to your image

# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply thresholding to create a binary mask
# _, thresholded = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# # Find contours in the binary mask
# contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Create an empty mask for the large shape
# large_shape_mask = np.zeros_like(gray)

# # Draw the largest contour on the mask
# largest_contour = max(contours, key=cv2.contourArea)
# cv2.drawContours(large_shape_mask, [largest_contour], 0, (255), thickness=cv2.FILLED)

# # Apply the mask to the original image
# result = cv2.bitwise_and(image, image, mask=large_shape_mask)

# # Display the result
# cv2.imshow('Large Shape Without Inner Shapes', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

# Load the image
image = cv2.imread('lithic_drawing.png')  # Replace 'your_image_path.jpg' with the actual path to your image

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Measure and print the area of each shape within the larger shape
for idx, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    print(f"Area of Shape {idx + 1}: {area}")

# Measure and print the area of the larger shape
larger_shape_area = cv2.contourArea(max(contours, key=cv2.contourArea))
print(f"\nArea of Larger Shape: {larger_shape_area}")

# Display the original image with contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

