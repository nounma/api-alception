
import streamlit as st
import requests

'''
# Find the age of anybody!

'''

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])



country= st.text_input("In which country to you want to watch?",value="us")
if st.button('Find age from this image'):


    # enter here the address of your flask api
    url = "https://aiceptionstefan-skliarovv1.p.rapidapi.com/createFaceAgeTask"

    payload = { "imageUrl": f”{uploaded_file}” }

    headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "17e7083fbcmsh7bc96474b7bc9aep106984jsnb79c78943de8",
	"X-RapidAPI-Host": "AIceptionstefan-skliarovV1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    print(response.json())
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
