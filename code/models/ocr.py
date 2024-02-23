
import pytesseract


def getTextFromImage(img_cv):
    arabic_text=pytesseract.image_to_string(img_cv , lang='ara')
    return arabic_text