🖼️ AI Image Generator

A simple Text-to-Image Generation App built with FastAPI, Streamlit, and OpenAI’s DALL·E 3 API.
This project lets you input a text prompt and generates an image in real time.

🚀 Features

Generate high-quality images from text prompts.

FastAPI backend serving an API endpoint for image generation.

Streamlit frontend for an interactive UI.

Easy integration with OpenAI’s image models (DALL·E 3).

🛠️ Tech Stack

FastAPI – backend REST API.

Streamlit – frontend UI.

OpenAI API – for text-to-image generation.

Python-dotenv – environment variable management.

📂 Project Structure
├── api.py        # FastAPI backend (exposes /text-to-image endpoint)
├── app.py        # Streamlit frontend
├── .env          # Environment file (contains OPENAI_API_KEY)

⚙️ Installation & Setup
1. Clone the repo
git clone https://github.com/KaanSezen1923/text-to-image-generator.git
cd text-to-image-generator

2. Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Add your API key

Create a .env file in the root directory:

OPENAI_API_KEY=your_api_key_here

4. Run the backend (FastAPI)
uvicorn api:app --reload

5. Run the frontend (Streamlit)
streamlit run app.py

🔗 API Endpoint
GET /text-to-image/{query}

Generates an image from a text prompt.

Example request:

GET http://localhost:8000/text-to-image/Astronaut riding a horse


Example response:

{
  "image": "https://generated-image-url.com/example.png"
}

🎨 Demo

Open the Streamlit UI at http://localhost:8501.

Enter a description (e.g., "Astronaut riding a horse") and click Generate.

The generated image will appear on the page.

<img width="1919" height="1018" alt="image" src="https://github.com/user-attachments/assets/a3ead841-5e82-4eb0-8b7f-ef08dd0213a2" />

<img width="1916" height="1013" alt="image" src="https://github.com/user-attachments/assets/e40d6115-1a89-4465-9cd5-d9b8c9628590" />



📌 Future Improvements

 Add support for multiple image sizes.

 Allow batch generation (more than 1 image at once).

 Save generated images locally or to cloud storage (S3/Google Drive).

 Add user authentication.

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a PR.

📜 License

This project is licensed under the MIT License.
