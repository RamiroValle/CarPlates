import boto3
import json
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
client = boto3.client(service_name='lambda', region_name='us-east-1', endpoint_url="http://serverless:3002",
                      aws_access_key_id="123", aws_secret_access_key="123")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"]
)


@app.get("/")
async def get_model(plate: str):
    params = {
        'FunctionName': 'carNameProvider-dev-api',
        'InvocationType': 'RequestResponse',
        'Payload': json.dumps({'plate': plate}).encode('UTF-8'),
    }
    response = client.invoke(**params)
    if response.get('StatusCode') == 200:
        resp = json.loads(response['Payload'].read().decode("UTF-8"))
        if resp.get('statusCode') == 200:
            model = json.loads(resp['body'])['model']
            return f"The model is {model}"
    return "Could not find the model for the requested plate"
