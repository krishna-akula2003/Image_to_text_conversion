from PIL import Image
import pytesseract

# Path to tesseract executable
tesseract_path = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Path to the image or video
image_path = r"C:\Users\User\Pictures\Screenshots\decision tree.png"

# Open the image file
img = Image.open(image_path)

# Set the tesseract path in the pytesseract module
pytesseract.pytesseract.tesseract_cmd = tesseract_path

# Use pytesseract to convert the image into text
text = pytesseract.image_to_string(img)

# Print the text
print(text)
