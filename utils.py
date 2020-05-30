import re
import numpy as np
import pytesseract.pytesseract as pt


from settings import ENV

patterns = ["\(\d\d\)\d{4,5}-\d{4,4}", "\d\d\d\d\d\d\d\d", "(\d\d)\d{8,9}"]

if ENV == "dev":
    pt.tesseract_cmd = r'Tesseract-OCR/tesseract.exe'
    
def pre_process_string(string):
    string = string.replace(" ", "")
    return string

def pre_process_image(img):
    return img

def find_numbers_from_string(string, regex):
    string = pre_process_string(string)
    return re.findall(regex, string)

def phone_numbers_from_image(img):
    string = get_string_from_image(img)
    numbers = []
    for regex in patterns:
        numbers += find_numbers_from_string(string, regex)
    
    return numbers

def get_string_from_image(img):
    img = pre_process_image(img)
    return pt.image_to_string(img)


# number paterns

