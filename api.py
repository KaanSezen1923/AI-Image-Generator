from fastapi import FastAPI, HTTPException
from openai import OpenAI
import os
from dotenv import load_dotenv
import base64
import time
import boto3


load_dotenv()
app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
aws_access_key = os.getenv("AWS_ACCESS_KEY")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION", "us-east-1")

s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region
        )

bucket_name="generatedimages1923"

@app.get("/text-to-image/{query}")
def text_to_image(query: str):
    try:
        result = client.images.generate(
            model="dall-e-3",
            prompt=query,
            size="1024x1024",
            n=1,
            response_format="b64_json"
        )
        image_b64 = result.data[0].b64_json
        file_bytes = base64.b64decode(image_b64)
        unix_time = int(time.time())
        filename = f"{unix_time}.png"
        
        s3_client.put_object(
            Bucket=bucket_name,
            Key=filename,
            Body=file_bytes,
            ContentType="image/png"
        )
        
        print(f"✅ Image saved as {filename} in S3 bucket {bucket_name}")
        return {"image":f"https://{bucket_name}.s3.{aws_region}.amazonaws.com/{filename}"}

        

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


