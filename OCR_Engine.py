import pytesseract
import ftfy
import aadhaar_read_data
import sys , os



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


pytesseract.pytesseract.tesseract_cmd = resource_path(r'D:\Tesseract-OCR\tesseract.exe')


def extract(img_f, img_b):
    
    text_f = pytesseract.image_to_string(img_f, lang='eng')
    text_b = pytesseract.image_to_string(img_b, lang='eng')

    # writing the text of both images
    text_output = open('output.txt', 'w', encoding='utf-8')
    # text_output.write("Data Of Front Image")
    text_output.write(text_f)

    # text_output.write("Data Of Back Image")
    text_output.write(text_b)

    text_output.close()

    file = open('output.txt', 'r', encoding='utf-8')
    text = file.read()

    # Fixing the Encoding
    text = ftfy.fix_text(text)
    text = ftfy.fix_encoding(text)

    data = aadhaar_read_data.adhaar_read(text)

    return data

    