import numpy as np
import pytesseract as ocr

def get_string_from_image(img):
    return ocr.image_to_string(img)