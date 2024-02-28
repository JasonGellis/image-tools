import cv2

def detect_lithic(image_array, config_file):
    """
    Apply binary threshold and edge detection to input image array/s based on configuration file options.
    Resulting image array has pixel values of 0,1

    Parameters
    ----------
    image_array: array
        Array of an unprocessed image (0, 255 pixels)
    config_file: dict
        Information on thresholding values and other configuration options

    Returns
    -------
    sobelXY: array
        Edge-detected image array
    thresh: float
        Threshold value used for binarization
    """

    # thresholding
    thresh_factor = config_file.get('threshold_factor', 1.0)  # Default threshold factor is 1.0
    thresh = cv2.threshold(image_array, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[0] * thresh_factor

    print(f"Threshold value being used: {thresh}")

    # binarization
    _, binary_array = cv2.threshold(image_array, thresh, 255, cv2.THRESH_BINARY)

    # edge detection using Sobel filter
    x = cv2.Sobel(binary_array, cv2.CV_64F, 1, 0, ksize=1)
    y = cv2.Sobel(binary_array, cv2.CV_64F, 0, 1, ksize=1)
    absX = cv2.convertScaleAbs(x)  # convert back to uint8
    absY = cv2.convertScaleAbs(y)  # convert back to uint8
    sobelXY = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

    return sobelXY, thresh
