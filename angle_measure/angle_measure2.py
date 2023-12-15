import cv2
import numpy as np

# Load the image
image = cv2.imread('test_2.png')  # Replace 'your_image_path.jpg' with the actual path to your image

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection using Canny
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the largest contour (assuming it is the outer boundary of the concentric lines)
largest_contour = max(contours, key=cv2.contourArea)

# Create a convex hull around the largest contour
hull = cv2.convexHull(largest_contour)

# Draw the boundary around the concentric lines
bounded_area = np.zeros_like(gray)
cv2.drawContours(bounded_area, [hull], 0, (255), thickness=cv2.FILLED)

# Measure the angle of the bounded area
angle = cv2.minAreaRect(hull)[-1]

# Display the result
cv2.imshow('Bounded Area', bounded_area)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the measured angle
print(f"Angle of the bounded area: {angle:.2f} degrees")
