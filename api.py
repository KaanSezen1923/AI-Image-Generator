from fastapi import FastAPI, HTTPException
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/text-to-image/{query}")
def text_to_image(query: str):
    try:
        result = client.images.generate(
            model="dall-e-3",
            prompt=query,
            size="1024x1024",
            n=1,
        )
        image_url = result.data[0].url
        return {"image": image_url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
