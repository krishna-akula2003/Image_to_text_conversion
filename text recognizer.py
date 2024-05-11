from PIL import Image
import pytesseract
tesseract_path = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

image_path = r"C:\Users\User\Pictures\Screenshots\decision tree.png"

img = Image.open(image_path)

pytesseract.pytesseract.tesseract_cmd = tesseract_path

text = pytesseract.image_to_string(img)

print(text)
