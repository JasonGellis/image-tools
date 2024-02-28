from skimage.restoration import denoise_tv_chambolle
from skimage import exposure
import numpy as np

def process_image(image_array, config_file):
    """
    Applying De-noising and contrast stretching on an input image.

    Parameters
    ----------
    image_array : array
        Array of an unprocessed image (0, 255 pixels)
    config_file : dict
        Information on configuration values for denoising and contrast stretching.

    Returns
    -------
    img_rescale : array
        Processed image array after denoising and contrast stretching.
    denoise_weight : float
        The weight used for denoising operation.
    contrast_stretch_range : tuple
        The percentile range used for contrast stretching.
    """

    # Denoising
    denoise_weight = config_file.get('denoise_weight', 0.1)  # Default denoise weight is 0.1
    img_denoise = denoise_tv_chambolle(image_array, weight=denoise_weight, multichannel=False)

    # Contrast stretching
    contrast_stretch_range = config_file.get('contrast_stretch', (2, 98))  # Default contrast stretch range is (2, 98)
    p2, p98 = np.percentile(img_denoise, contrast_stretch_range)
    img_rescale = exposure.rescale_intensity(img_denoise, in_range=(p2, p98))

    print(f"Denoise weight used: {denoise_weight}")
    print(f"Contrast stretch range used: {contrast_stretch_range}")

    return img_rescale
