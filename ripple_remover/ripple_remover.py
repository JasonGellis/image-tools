import cv2
import numpy as np

def remove_concentric_lines(input_image_path, output_image_path):
    # Read the input image
    image = cv2.imread(input_image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection to find contours
    edges = cv2.Canny(gray, 50, 150)

    # Find contours in the edged image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours and remove concentric lines
    for contour in contours:
        # Fit a bounding ellipse around the contour
        (x, y), (major_axis, minor_axis), angle = cv2.fitEllipse(contour)

        # Check if the major and minor axes are almost equal
        if major_axis / minor_axis < 1.1:
            # If axes are almost equal, draw the contour (remove the line)
            cv2.drawContours(image, [contour], -1, (255, 255, 255), thickness=cv2.FILLED)

    # Save the output image
    cv2.imwrite(output_image_path, image)

if __name__ == "__main__":
    input_path = "path/to/your/input/image.jpg"
    output_path = "path/to/your/output/image_removed_lines.jpg"

    remove_concentric_lines(~/Desktop/103.png, ~/Desktop/output)
