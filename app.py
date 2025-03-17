import os
import time
import tempfile
import requests
import streamlit as st
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from huggingface_hub import login

# Load environment variables
load_dotenv(find_dotenv())
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

st.set_page_config(page_title="Image-to-Story Converter", page_icon="🖼️")
# Login to Hugging Face API
login(token=HUGGINGFACE_API_TOKEN)

css_code = """
<style>
    
    h1, h2, h3 {
        color: #333;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
    }
</style>
"""

# Cache pipelines for better performance
@st.cache_resource
def load_description_pipeline():
    return pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

@st.cache_resource
def load_text_generation_pipeline():
    return pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")

description_pipeline = load_description_pipeline()
text_gen_pipeline = load_text_generation_pipeline()

# Function to show progress bar
def progress_bar(duration: int):
    progress_text = "Processing... Please wait"
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(duration):
        time.sleep(0.04)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(0.5)
    my_bar.empty()

# Generate text from an image
def generate_text_from_image(image_path: str) -> str:
    result = description_pipeline(image_path)
    return result[0]['generated_text']  # Adjust based on the output format

# Generate a short story from the extracted text
def generate_story_from_text(scenario: str) -> str:
    prompt_template = f"""
    Write a short story based on the following scenario. The story should be engaging, concise, and imaginative, with a maximum of 50 words. Avoid any additional commentary or explanation.\n
    SCENARIO: {scenario}\n
    STORY:\n
    """
    result = text_gen_pipeline(prompt_template, max_new_tokens=100, do_sample=True)
    return result[0]['generated_text'].strip()  # Remove any leading/trailing whitespace


# Generate speech from text using Hugging Face API
def generate_speech_from_text(message: str) -> str:

    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    response = requests.post(API_URL, headers=headers, json={"inputs": message})
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".flac")
    temp_audio.write(response.content)
    return temp_audio.name

# Streamlit App
st.markdown(css_code, unsafe_allow_html=True)



# Main UI
st.header("📖 Image-to-Story Converter")
uploaded_file = st.file_uploader("Upload an image (JPG)", type=["jpg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    progress_bar(50)

    # Process the image
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_file_path = temp_file.name

    # Generate description
    scenario = generate_text_from_image(temp_file_path)
    story = generate_story_from_text(scenario)
    audio_path = generate_speech_from_text(story)

    st.subheader("Generated Image Scenario")
    st.write(scenario)

    st.subheader("Generated Short Story")
    st.write(story)

    st.subheader("🎵 Generated Audio")
    st.audio(audio_path)