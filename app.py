import streamlit as st
import requests


st.set_page_config(page_title="Image Generator", page_icon=":camera:", layout="wide")

st.title("Image Generator")
st.write("Generate images from text using the Qwen-Image model.")

query = st.text_input("Enter a description for the image:", "Astronaut riding a horse")

if st.button("Generate"):
    try:
        response = requests.get(f"http://localhost:8000/text-to-image/{query}").json()
        print(response)
        
        if "image" in response:

            st.image(response.get("image"), caption=f"Generated image for: {query}", use_column_width=True)
        else:
            st.error("Image not found in the response.")
    except Exception as e:
        st.error(f"Error: {str(e)}")
