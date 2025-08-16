
import cv2
import easyocr
from deepface import DeepFace
from PIL import Image
import numpy as np
import re

reader = easyocr.Reader(['en','ar'])

def read_text_from_image(image_path):
    results = reader.readtext(image_path)
    # text = " ".join([res[1] for res in results])
    full_text = " ".join([res[1] for res in results])
    print('OCR detected text:', full_text)

    #name_match = re.findall(r'\b[A-Z][a-zA-Z]+\s[A-Z][a-zA-Z]+\b', full_text)
    id_match = re.findall(r'\b784-\d{4}-\d{7}-\d{1}\b', full_text)

    # Improved logic to extract name after the word "Name"
    name = "Name Not Found"

    # Find Arabic name after known keyword hints

    # Try to find the word "قم الهوية" and extract following Arabic phrases
    text = full_text.replace('_','')
    arabic_letters = r'[\u0621-\u064A]'
    arabic_text = ' '.join(re.findall(f'{arabic_letters}+',text))
    match = re.search(r"قم الهوية\s*([\u0621-\u064A\s]{15,})", arabic_text)
    if match:
        raw_name = match.group(1)
        raw_name = raw_name.split('تاريخ الميلاد')
        arabic_name = (raw_name[0])
    else:
        arabic_name = "Arabic Name Not Found"
    
    # For English Name
    name_index = full_text.find("Name")
    if name_index != -1:
        # Extract text after "Name"
        after_name = full_text[name_index + len("Name"):].strip()
        # Take first 4–6 words after "Name"
        words = after_name.split('Date')
        if len(words) >= 2:
            name = words[0]
            # name = " ".join(words[:5])  # Adjust this number if needed
    
    return {
        "name": name,
        "arabic_name": arabic_name,
        "id": id_match[0] if id_match else "ID Not Found",
        'full_text': full_text
    }

def calculate_face_similarity(img1_path, img2_path):
    try:
        result = DeepFace.verify(img1_path, img2_path,model_name='ArcFace', enforce_detection=False)

        return round(result["distance"], 3), result["verified"], result["threshold"],result['model']
    except Exception as e:
        return str(e), False
