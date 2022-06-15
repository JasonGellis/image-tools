# When pixels(px) are equal to PPI, then 1 PPI = 1 inch or 2.54cm.
# 1cm = 96pixels/2.54, or 1cm = 37.7952756 pixels at 96ppi
# As PPI increases, and number of pixels stay the same, cm decreases.
# As number of pixels increases, and PPI stays the same, cm increases.
# PPI * x = 96 and pixel height * y = 37.7952756

# Formulas
# 1cm = 96px / 2.54
# 1px = 2.54 cm / 96
# 1px = 2.54 cm / PPI
# cm = pixels * ( 2.54 / PPI )

from PIL import Image

scale_size = int(input("Enter scale size in cm: "))
scale_res = int(input("Enter scale resolution in PPI: "))
scale_px = scale_size/(2.54/scale_res)  # pixels number based on the equation: cm = pixels * ( 2.54 / PPI )
scale_unit = scale_px/scale_size  # what 1 cm of the scale will be in pixels
# print(scale_px)
# print(scale_unit)
# Import the image
img = Image.open("scale_real.png")

# dimension information in pixels
px_width = img.size[0]
px_height = img.size[1]
dpi = img.info['dpi']

# Return information about the scanned image
print('Pixel width of the image is:', px_width)
print('Pixel height of the image is:', px_height)
print('DPI of the image is:', dpi)
print('PPI of the image is:', dpi[1])

px_cm = 1/(2.54/dpi[1])  # how many pixels of the scanned image equal 1 cm
scanned_cm = px_height*(2.54/dpi[1])  # cm of scanned image based on image resolution an pixel count
multiplier = scale_unit/px_cm  # to equalize the pixels in 1cm of the scale and 1cm of the scanned image
new_cm = multiplier*px_height

print(f"For the scanned image, {px_cm} pixels at {dpi[1]} PPI is equal to 1 cm.")
print(f"Based on scanning resolution, the imported image appears as {scanned_cm} centimeters in height on the screen.")
print(f"Based on the provided scale of {scale_size} cm, at a DPI of {scale_res}, 1 cm will equate to {scale_unit} pixels.")