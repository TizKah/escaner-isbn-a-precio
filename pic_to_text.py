# pic_to_text.py

from PIL import Image
import pytesseract
import cv2
import pyzbar.pyzbar as pyzbar

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_isbn():

    isbn = ''
    cam = cv2.VideoCapture(0)
    while True:
        _, frame = cam.read()

        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            isbn = obj.data

        cv2.imshow("Escanea el código de barra pa", frame)

        key = cv2.waitKey(1)
        if isbn != "" or key == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    isbn = str(isbn)[2:-1]
    print(f"ISBN: {isbn}\n")

    #image = Image.open(image_path)
    #isbn = pytesseract.image_to_string(image)
    return isbn
