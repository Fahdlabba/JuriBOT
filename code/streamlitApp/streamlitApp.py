import numpy as np
import cv2
import streamlit as st  
from models.gemini import getGeminiCompletion
from preprocessing.image import preprocessImage
from preprocessing.text import preprocessText
from models.ocr import getTextFromImage
import requests

def loadImageFromUrl(url):
    #get request to the url
    response = requests.get(url)
    #check if the request is valid
    if response.status_code != 200:
        st.write('Invalid URL')
    #convert the image to cv2 format
    img = np.array(bytearray(response.content), dtype=np.uint8)
    #decode the image
    img = cv2.imdecode(img, -1)
    return img
#function to display the extracted text and important information
def showExtraectAndInfo(uploadedImage,url):
    if st.button('Extract Text'):
        with st.spinner('Extracting text...'):
            if uploadedImage is not None or url:
                #check if the user uploaded an image or entered a url
                if url:
                    img_cv=loadImageFromUrl(url)   
                else:
                    img_cv = cv2.imdecode(np.fromstring(uploadedImage.read(), np.uint8), 1)
                #display the image
                st.image(img_cv, use_column_width=True)
                #preprocess the image
                img_cv=preprocessImage(img_cv)
                #extract the text from the image
                arabic_text=getTextFromImage(img_cv)
                #get the important information from the text
                response=getGeminiCompletion(arabic_text)
                st.header('Extracted Text')
                #display the extracted text
                st.write(preprocessText(arabic_text))
                st.header('Important Information')
                #check if the response is a dictionary or a string
                if(type(response)==dict):
                    for key in response:
                        st.header(f':{key}')
                        st.write(response[key])
                else : 
                    st.write(response)
            else:
                st.write('Please upload an image first')

def main():
    st.set_page_config(page_title='Arab Document OCR', page_icon = "📰", initial_sidebar_state = 'auto')
    st.title('Arab Document Juridique OCR ')
    st.header('Upload an image to extract the text and important information.')
    st.header("Online Image URL")
    url =st.text_input('Enter the URL of the image')
    st.header('Local Image Upload')
    uploadedImage=st.file_uploader('Upload an image', type=['jpg', 'png', 'jpeg',"webp"])
    showExtraectAndInfo(uploadedImage,url)


