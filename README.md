
# 📸 Emirates ID Verification App
This project is a Streamlit web app for verifying identity using a selfie compared against an uploaded Emirates ID.
It uses:

* DeepFace (ArcFace model) for face similarity comparison

* EasyOCR for extracting text (English + Arabic) from the Emirates ID

* OpenCV & Streamlit for image handling/capturing

## 🚀 Features
* Upload or capture a selfie

* Upload or capture an Emirates ID card

* Automatic face verification using DeepFace (ArcFace model)

* Extracts:

    * English Name

    * Arabic Name

    * Emirates ID Number

* Displays similarity score & verification result

## 📂 Project Structure
`text`

`
.`

`├── appeasyocr.py       # Main Streamlit app`

`├── utilseasyocr.py     # OCR & Face verification utilities`

`└── captured_images/    # Folder where uploaded images are stored`
`(created automatically)`


## ⚙️ Installation
### 1️⃣ Clone the repository
`bash`

`git clone https://github.com/<your-username>/emirates-id-verification.git
cd emirates-id-verification`
### 2️⃣ Create & activate a virtual environment (recommended)
`bash`

`python -m venv venv`

`source venv/bin/activate   # On macOS/Linux`

`venv\Scripts\activate      # On Windows`

### 3️⃣ Install dependencies
`bash`

`pip install -r requirements.txt`

## 📦 Requirements
Here’s what you’ll need in requirements.txt:

`text`

`streamlit`

`opencv-python`

`pillow`

`easyocr`

`deepface`

`numpy`

(You may also need torch & torchvision manually for EasyOCR if not installed automatically.)

## ▶️ Running the App
Start the Streamlit app:

`bash`

`streamlit run appeasyocr.py`

The app will launch in your browser (default: http://localhost:8501).

## 🖼️ Usage Flow
1. Go to Upload Selfie → upload or capture your photo

2. Go to Upload Emirates ID → upload or capture the Emirates ID image

3. Go to Verify Identity →

    * Compares faces

    * Extracts Emirates ID details (Name, Arabic Name, ID Number)

    * Shows verification status & similarity score

# ⚠️ Notes
* The app creates a folder captured_images/ automatically for storing uploaded images.

* Face matching uses DeepFace with ArcFace (fast & accurate).

* OCR works for both Arabic & English text on Emirates ID.

* OpenCV camera input is included but commented out; you can enable it if needed.

# 🛠️ Future Improvements
* More robust Arabic text extraction logic

* Support for additional Emirates ID fields (expiry date, nationality, etc.)

* Dockerfile for containerized deployment

* Enable built-in st.camera_input for easier Streamlit-native capturing

# 👨💻 Author
Developed by Thamanna Hafeez
