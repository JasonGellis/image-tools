# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('test_2.png')  # Replace 'your_image_path.jpg' with the actual path to your image

# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply edge detection using Canny
# edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# # Detect lines using HoughLinesP
# lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=1000)

# # Iterate through each line and calculate the angle
# for line in lines:
#     x1, y1, x2, y2 = line[0]
#     angle_rad = np.arctan2(y2 - y1, x2 - x1)
#     angle_deg = np.degrees(angle_rad)
    
#     # Draw the line on the image
#     cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
#     # Annotate the image with the measured angle
#     cv2.putText(image, f'Angle: {np.mean(angle_deg):.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 1)

# # Display the annotated image
# cv2.imshow('Line Angles', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import numpy as np

# # Load the image
# image = cv2.imread('test_2.png')  # Replace 'your_image_path.jpg' with the actual path to your image

# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply edge detection using Canny
# edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# # Find contours in the edge-detected image
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Find the largest contour (assuming it is the concentric lines)
# largest_contour = max(contours, key=cv2.contourArea)

# # Create a bounding box around the concentric lines
# x, y, w, h = cv2.boundingRect(largest_contour)

# # Draw the bounding box on the original image
# cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # Measure the angle of the bounding box
# angle_deg = 0.5 * np.degrees(np.arctan2(h, w))

# # Annotate the image with the measured angle
# cv2.putText(image, f'Angle: {angle_deg:.2f}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 1)

# # Display the result
# cv2.imshow('Bounding Box around Concentric Lines', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
