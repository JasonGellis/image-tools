import os
import cv2

def read_image(input_dir, id, im_type='png'):
    """
    Read an image from the specified directory using OpenCV.

    Parameters:
    input_dir (str): Path to the directory where the images are located.
    id (str): Identifier code for the image.
    im_type (str, optional): Image file extension type. Default is set to '.png'.

    Returns:
    numpy.ndarray: An array representing the image data in grayscale.
    """
    # Construct the filename by combining the input directory, image identifier code, and image file extension
    filename = os.path.join(input_dir, f"{id}.{im_type}")

    # Read the image file using cv2.imread() function with the flag cv2.IMREAD_GRAYSCALE
    filename = os.path.join(input_dir, f"{id}.{im_type}")

    if not os.path.isfile(filename):
        print(f"Error: Image file '{filename}' does not exist.")
        return None

    im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    if im is None:
        print(f"Error: Unable to read image file '{filename}'.")
        return None

    print(f"Image '{filename}' read successfully.")
    return im