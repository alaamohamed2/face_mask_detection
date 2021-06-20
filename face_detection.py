import cv2
import os
import mediapipe as mp

# Color values in BGR
RED = (0, 0, 255)
GREEN = (0, 255, 0)

padding =  70



def print_face(image, face, is_masked):
    """ Prints face with color corresponding to if face is masked or not.

    Args:
        image (int[]): Array of image pixels.
        face (tuple): Bounds of face.
        is_masked (boolean): True if mask, false otherwise.

    Returns:
        int[]: Colored image of face with or without mask.
    """
    x, y, w, h = face
    if is_masked:
        image = cv2.rectangle(image, (x - padding // 2, y - padding // 2), (x + w + padding // 2, y + h + padding // 2), GREEN)
    else:
        image = cv2.rectangle(image, (x - padding // 2, y - padding // 2), (x + w + padding // 2, y + h + padding // 2), RED)

    return image

def crop_image(image, face):
    """ Crop image in according to the face bounds plus additional padding.

    Args:
        image (int[]): Array of image pixels.
        face (tuple): Bounds of face.

    Returns:
        int[]: Cropped image.
    """
    x, y, w, h = face
    crop_img = image[y - padding // 2: y + h + padding // 2, x - padding // 2: x + h + padding // 2]
    return crop_img
