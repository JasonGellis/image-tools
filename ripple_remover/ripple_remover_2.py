import cv2
import numpy as np

# Load the image
image = cv2.imread('lithic_drawing.png')  # Replace 'your_image_path.jpg' with the actual path to your image

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection using Canny
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the outermost contour
outer_contour = max(contours, key=cv2.contourArea)

# Create a mask for the outer contour
mask = np.zeros_like(gray)
cv2.drawContours(mask, [outer_contour], 0, (255), thickness=cv2.FILLED)

# Remove lines inside the square using the mask
result = cv2.bitwise_and(image, image, mask=~mask)

# Display the result
cv2.imshow('Square without Lines', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
