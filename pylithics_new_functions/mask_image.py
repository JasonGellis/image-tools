# import numpy as np
# import scipy.ndimage as ndi

# def mask_image(binary_array, contour, innermask=False):
#     """
#     Mask negative (white pixels) areas to generate contour lines.

#     Parameters
#     ----------
#     binary_array: array
#         Array of a processed image (0, 1 pixels)
#     contour: list of lists
#         Pixel coordinates for a contour of a single flake scar
#         or outline of a lithic object detected by contour finding
#     innermask: bool, optional
#         If True, returns the mask instead of the masked image array. Default is False.

#     Returns
#     -------
#     An image array if innermask is False, otherwise returns the mask.
#     """

#     # Create mask
#     r_mask = np.zeros_like(binary_array, dtype=bool)
#     r_mask[np.round(contour[:, 1]).astype(int), np.round(contour[:, 0]).astype(int)] = True
#     r_mask = ndi.binary_fill_holes(r_mask)

#     # Apply mask
#     if innermask:
#         return r_mask
#     else:
#         new_image = np.where(r_mask, binary_array, 0)
#         return new_image
import numpy as np
import cv2
from scipy import ndimage as ndi

# Load the image
image = cv2.imread("/Users/jasongellis/Projects/Palaeoanalytics/data/images/qesem_cave.png", cv2.IMREAD_GRAYSCALE)

def mask_image(binary_array, contour, innermask=False):
    """
    Mask negative (white pixels) areas of lithic flakes scars in order to generate contour lines.

    Parameters
    ----------
    binary_array: array
        Array of a processed image  (0, 1 pixels)
    contour: list of lists
        Pixel coordinates for a contour of a single flake scar
        or outline of a lithic object detected by contour finding
    innermask: bool, optional
        Whether to return the mask (r_mask) instead of applying it to the image. Default is False.

    Returns
    -------
    An image array or a mask
    """

    r_mask = np.zeros_like(binary_array, dtype='bool')
    r_mask[np.round(contour[:, 1]).astype('int'), np.round(contour[:, 0]).astype('int')] = 1
    r_mask = ndi.binary_fill_holes(r_mask)

    if innermask:
        return r_mask
    else:
        new_image = np.multiply(r_mask, binary_array)
        return new_image

# Example usage:
# Assuming you have the binary array and contour available
# new_image = mask_image(binary_array, contour)
# Or to get the mask itself:
# r_mask = mask_image(image, contour, innermask=True)
