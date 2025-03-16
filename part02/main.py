import os

import requests

from dotenv import load_dotenv

load_dotenv()

headers = {
    "Ocp-Apim-Subscription-Key": os.getenv("AZURE_SPEECH_KEY"),
    "Content-Type": "application/json"
}

body = {
    "contentUrls": [os.getenv("BLOB_URL")],
    "locale": "en-US",
    "displayName": "Meeting Recording Transcriber Demo",
    "properties": {
        "diarizationEnabled": True,
        "diarization": {
            "speakers": {
                "minCount": 4,
                "maxCount": 4
            }
        }
    }
}

job_response = requests.post(
    os.getenv("ENDPOINT"),
    headers=headers,
    json=body
)

if job_response.status_code == 201:
    job_data = job_response.json()
    print(job_data)
    job_id = job_data["self"].split("/")[-1]
    print(f"Batch job started with ID {job_id}")
else:
    print(f"Something went wrong: {job_response.text} ({job_response.status_code})")
