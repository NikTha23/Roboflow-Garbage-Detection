# from inference_sdk import InferenceHTTPClient

# CLIENT = InferenceHTTPClient(
#     api_url="https://serverless.roboflow.com",
#     api_key="YOUR_API_KEY"
# )

# result = CLIENT.infer(
#     "YOUR_IMAGE.jpg",
#     model_id="garbage-classification-3-p6zyg/1"
# )
import os

from dotenv import load_dotenv
from inference_sdk import InferenceHTTPClient

load_dotenv()

API_KEY = os.getenv("ROBOFLOW_API_KEY")
MODEL_ID = os.getenv("ROBOFLOW_MODEL_ID")

print("API key loaded:", bool(API_KEY))
print("Model ID:", MODEL_ID)

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=API_KEY
)


def run_inference(image_path):

    result = CLIENT.infer(
        image_path,
        model_id=MODEL_ID
    )

    return result


if __name__ == "__main__":

    result = run_inference("test.jpg")

    print("\n========== RESULT ==========\n")
    print(result)