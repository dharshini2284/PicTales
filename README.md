# PicTales

PicTales is a GenAI-powered image-to-speech web application that transforms static images into vivid audio storytelling. It integrates state-of-the-art models from Hugging Face and OpenAI, leveraging LangChain for seamless orchestration. Built using Streamlit for a user-friendly interface, this project aims to enhance accessibility and provide an engaging way to interpret images.

## 🔍 Features

- **Image Captioning:** Generates a descriptive caption for the uploaded image using BLIP (Bootstrapping Language-Image Pretraining).
- **Story Generation:** Transforms the image caption into a creative and engaging story using OpenAI's GPT model.
- **Speech Conversion:** Converts the generated story into natural-sounding speech using Bark, a text-to-audio model.
- **User Interface:** A clean and interactive interface built with Streamlit for effortless user experience.

## ⚙️ Tech Stack

- **Frontend:** Streamlit
- **Image Captioning:** BLIP model from Hugging Face
- **Story Generation:** OpenAI GPT model via LangChain
- **Text-to-Speech:** Bark model
- **Orchestration:** LangChain for chaining model outputs

## 🚀 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/dharshini2284/PicTales.git
   cd PicTales
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set API Keys**
   Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## 📷 How It Works

1. **Upload an Image**  
   The user uploads an image through the Streamlit interface.

2. **Generate Caption**  
   The BLIP model creates a caption describing the image.

3. **Create a Story**  
   The caption is passed to OpenAI’s GPT model using LangChain, which generates a vivid narrative.

4. **Convert to Speech**  
   The story is transformed into speech using the Bark TTS model.

5. **Playback**  
   The final audio story is played back to the user in the app.

## 📌 Example Use Cases

- Making images more accessible to visually impaired individuals.
- Generating engaging content for children based on pictures.
- Enhancing user experience in digital galleries or educational tools.

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues for suggestions, bugs, or feature requests.
