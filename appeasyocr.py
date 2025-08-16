
import streamlit as st
#import cv2
import os
from PIL import Image
from utilseasyocr import calculate_face_similarity, read_text_from_image

st.set_page_config(layout="centered")
st.title("📸 Emirates ID Verification App")

image_dir = "captured_images"
os.makedirs(image_dir, exist_ok=True)

def capture_image(filename):
    cap = cv2.VideoCapture(0)
    st.info("Press SPACE to capture, ESC to exit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Camera not working.")
            break
        cv2.imshow("Capture - Press SPACE", frame)
        key = cv2.waitKey(1)
        if key % 256 == 27:  # ESC
            break
        elif key % 256 == 32:  # SPACE
            cv2.imwrite(filename, frame)
            st.success(f"Saved to {filename}")
            break
    cap.release()
    cv2.destroyAllWindows()

page = st.sidebar.selectbox("Select Page", ["1️⃣ Upload Selfie", "2️⃣ Upload Emirates ID", "3️⃣ Verify Identity"])

if page == "1️⃣ Upload Selfie":
    selfie = st.file_uploader('Upload your photo:', type=["jpg", "jpeg", "png"])
    if selfie:
        selfie_path = f"{image_dir}/selfie.jpg"
        with open(selfie_path, "wb") as f:
            f.write(selfie.getbuffer())
        st.image(selfie_path, caption="Photo Uploaded")
    # selfie = st.camera_input("Capture your face selfie:")
    # if selfie:
    #     selfie_path = f"{image_dir}/selfie.jpg"
    #     with open(selfie_path, "wb") as f:
    #         f.write(selfie.getbuffer())
    #     st.image(selfie_path, caption="Selfie captured")

elif page == "2️⃣ Upload Emirates ID":
    eid_image = st.file_uploader("Upload your Emirates ID image:", type=["jpg", "jpeg", "png"])
    if eid_image:
        id_path = f"{image_dir}/emirates_id.jpg"
        with open(id_path, "wb") as f:
            f.write(eid_image.getbuffer())
        st.image(id_path, caption="Emirates ID uploaded")

# elif page == "2️⃣ Capture Emirates ID":
#     eid_image = st.camera_input("Capture your Emirates ID:")
#     if eid_image:
#         id_path = f"{image_dir}/emirates_id.jpg"
#         with open(id_path, "wb") as f:
#             f.write(eid_image.getbuffer())
#         st.image(id_path, caption="Emirates ID captured")

elif page == "3️⃣ Verify Identity":
    selfie_path = f"{image_dir}/selfie.jpg"
    id_path = f"{image_dir}/emirates_id.jpg"
    if os.path.exists(selfie_path) and os.path.exists(id_path):
        with st.spinner("Comparing faces..."):
            distance, match, threshold, model1 = calculate_face_similarity(selfie_path, id_path)
            st.metric("Face Match", "✅ Match" if match else "❌ Not a Match")
            similarity_score =  max(0, min(100, (1 - distance / threshold) * 100))
            st.write(f"Distance : {distance:.2f}")
            st.write(f"Face Similarity Score : {similarity_score:.2f}%")
           
        with st.spinner("Reading ID text..."):
            extracted = read_text_from_image(id_path)
            st.write(f"**Name:** {extracted['name']}")
            st.write(f"**Arabic Name:** {extracted['arabic_name']}")
            st.write(f"**Document Number:** {extracted['id']}")
    else:
        st.warning("Please capture both selfie and ID image first.")
