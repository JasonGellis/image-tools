# import packages
import argparse
import cv2
import imutils
import numpy as np

# construct argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to the input image")
ap.add_argument("-o", "--output", required = True, help="path to output image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# convert it to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# threshold the image
(T, threshInv) = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

# find outer contour of thresholded image
conts = cv2.findContours(threshInv.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
conts = imutils.grab_contours(conts)

# loop over the contour/s for image moments
for c in conts:
	#  compute the center of the contour
	M = cv2.moments(c)
	#  calculate the centroid
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

# draw and fill the contour on the image
cv2.drawContours(image, [c], -1, (0, 0, 0), thickness=cv2.FILLED)

# draw the centroid on the filled contour
cv2.circle(image, (cX, cY), 7, (255, 0, 0), -1)

# portions of the image (includes white and black pixels)
top_half = image[0:cY, :]
bottom_half = image[cY:, :]
left_half = image[:, 0:cX]
right_half = image[:, cX:]

# halves of images containing black pixels
top_half = top_half[:, :, 1]
bottom_half = bottom_half[:, :, 1]
left_half = left_half[:, :, 1]
right_half = right_half[:, :, 1]

#  np.size() gives total number of pixels in the image
#  np.count_nonzero() gives number of white pixels
top_bottom_ratio = (int(np.size(top_half) - np.count_nonzero(top_half)) / (np.size(bottom_half) - np.count_nonzero(bottom_half)))
left_right_ratio = (int(np.size(left_half) - np.count_nonzero(left_half)) / (np.size(right_half) - np.count_nonzero(right_half)))

# area of the entire contour

# show images
cv2.imshow("Original Image", gray)
cv2.imshow("Centroid", image)
cv2.imshow("Top Half (at the centroid)", top_half)
cv2.imshow("Bottom Half (at the centroid)", bottom_half)
cv2.imshow("Left Half (at the centroid)", left_half)
cv2.imshow("Right Half (at the centroid)", right_half)
cv2.waitKey(0)

# Save the image to disk.
cv2.imwrite(args["output"] + ".png", gray)
cv2.imwrite(args["output"] + ".png", image)  
cv2.imwrite(args["output"] + ".png", top_half)  
cv2.imwrite(args["output"] + ".png", bottom_half)  
cv2.imwrite(args["output"] + ".png", left_half)  
cv2.imwrite(args["output"] + ".png", right_half)  

print(f'The ratio of top to bottom halves is: {round(top_bottom_ratio, 3)}')
print(f'The ratio of left to right halves is: {round(left_right_ratio, 3)}')
