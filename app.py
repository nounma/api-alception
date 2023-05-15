
import streamlit as st
import requests

'''
# Find the age of anybody!

'''

uploaded_file = st.text_input("Image URL",value="https://hips.hearstapps.com/hmg-prod/images/britney-spears-deletes-instagram-again-after-family-drama-1655461718.jpg?crop=0.750xw:0.542xh;0.128xw,0.0224xh&resize=1200:*")
if st.button('Find age from this image'):

	url = "https://aiceptionstefan-skliarovv1.p.rapidapi.com/createFaceAgeTask"

	payload = { "imageUrl": f"{uploaded_file}"}

	headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "17e7083fbcmsh7bc96474b7bc9aep106984jsnb79c78943de8",
	"X-RapidAPI-Host": "AIceptionstefan-skliarovV1.p.rapidapi.com"
	}

	response = requests.post(url, data=payload, headers=headers)

	print(response.json())

