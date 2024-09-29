from PIL import Image
from PIL import ImageFile
import pytesseract
import csv
from datetime import datetime

ImageFile.LOAD_TRUNCATED_IMAGES=True

# Open the CSV file
with open('/home/thomas/GBN/GBN-backend/src/data/pagina.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        if row[0] == "id":
            continue
        ocr_output = []
        # Get the path to the image file
        pagina_id = row[0]
        modelo_ocr = "tesseract"
        image_path = row[2]
        
        image = Image.open(image_path)
        
        # Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(image)
        
        # write the text to the CSV file
        ocr_output.append(pagina_id)
        ocr_output.append(text)
        ocr_output.append(modelo_ocr)
        ocr_output.append(row[0])
        ocr_output.append(datetime.now())
        ocr_output.append(datetime.now())


        with open('/home/thomas/GBN/GBN-backend/src/data/texto_ocr.csv', 'a') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(ocr_output)