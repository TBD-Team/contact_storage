from settings import ENV
import numpy as np
import pytesseract.pytesseract as pt

if ENV == "dev":
    pt.tesseract_cmd = r'Tesseract-OCR/tesseract.exe'

def get_string_from_image(img):
    return pt.image_to_string(img)