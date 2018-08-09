from PIL import Image
from pytesseract import *
image = Image.open('validate04.png') # Open image object using PIL
print (image_to_string(image))  # Run tesseract.exe on image