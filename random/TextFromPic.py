from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\martin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

picPath = input('Enter the path of the picture file: ')
img = Image.open(picPath)
print(pytesseract.image_to_string(img))