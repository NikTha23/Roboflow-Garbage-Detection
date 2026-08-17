# ♻️ Roboflow Garbage Detection

A simple **AI-based garbage detection web application** built with **Python, Flask, and Roboflow**.

The project uses a Roboflow garbage classification/object-detection dataset containing **10,464 images across 7 classes**. A trained Roboflow model is accessed through the **Roboflow Inference SDK**, while Flask provides a simple web interface for uploading images and displaying predictions.

## 🚀 Project Overview

The application follows this workflow:

```text
Roboflow Dataset
       ↓
Dataset Version
       ↓
Model Training
       ↓
Trained Roboflow Model
       ↓
Roboflow Inference SDK
       ↓
Flask Application
       ↓
Upload Image
       ↓
Garbage Detection
       ↓
Class + Confidence
```

## 📊 Dataset

The project uses the **Garbage Classification 3** dataset from Roboflow Universe.

**Dataset:** Garbage Classification 3

**Roboflow Dataset:**
https://universe.roboflow.com/doersons-workspace/garbage-classification-3-p6zyg

### Dataset information

* **Images:** 10,464
* **Classes:** 7
* **Task:** Object Detection
* **Platform:** Roboflow

### Classes

```text
1. PAPER
2. PLASTIC
3. GLASS
4. METAL
5. CARDBOARD
6. CLOTH
7. BIODEGRADABLE
```

## 🛠️ Technologies Used

* Python 3.11
* Flask
* Roboflow
* Roboflow Inference SDK
* Python-dotenv
* Pillow
* HTML
* CSS

## 📁 Project Structure

```text
Roboflow_Garbage_Detection/
│
├── app.py
├── inference.py
├── .env
├── .gitignore
├── requirements.txt
│
├── test.jpg
│
├── uploads/
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## 📄 File Description

### `app.py`

The main Flask application.

Responsibilities:

* Starts the Flask server
* Displays the web page
* Receives uploaded images
* Saves uploaded images
* Calls the inference function
* Sends predictions to the HTML page

### `inference.py`

Contains the Roboflow inference code.

It:

* Loads the Roboflow API key
* Loads the Roboflow model ID
* Creates the `InferenceHTTPClient`
* Sends the input image to Roboflow
* Receives prediction results

### `.env`

Stores sensitive configuration values.

Example:

```env
ROBOFLOW_API_KEY=YOUR_ROBOFLOW_API_KEY
ROBOFLOW_MODEL_ID=garbage-classification-3-p6zyg/1
```

**Never upload `.env` to GitHub.**

### `requirements.txt`

Contains the Python dependencies required by the project.

### `templates/index.html`

The frontend page where the user:

* Selects an image
* Uploads the image
* Starts garbage detection
* Views prediction results

### `static/style.css`

Contains the styling for the Flask web interface.

### `uploads/`

Stores images uploaded through the web application.

## ⚙️ Installation

### 1. Clone or download the project

Open PowerShell and move to the project directory:

```powershell
cd C:\Users\user\Desktop\Roboflow_Garbage_Detection
```

### 2. Create a Python 3.11 environment

Roboflow's inference SDK requires a supported Python version. Python 3.11 is recommended for this project.

Using Anaconda:

```powershell
conda create -n roboflow python=3.11 -y
```

Activate the environment:

```powershell
conda activate roboflow
```

Verify:

```powershell
python --version
```

Expected:

```text
Python 3.11.x
```

### 3. Install dependencies

Run:

```powershell
python -m pip install -r requirements.txt
```

## 🔑 Roboflow API Configuration

Create a Roboflow API key from your Roboflow account.

Then create a `.env` file in the project root:

```env
ROBOFLOW_API_KEY=YOUR_API_KEY
ROBOFLOW_MODEL_ID=garbage-classification-3-p6zyg/1
```

Replace:

```text
YOUR_API_KEY
```

with your own API key.

### Security

Never write your API key directly inside Python code.

Do not commit:

```text
.env
```

to GitHub.

The `.gitignore` file should contain:

```text
.env
venv/
__pycache__/
*.pyc
uploads/*
```

## 🧠 How Inference Works

The core inference code uses the Roboflow SDK:

```python
from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=API_KEY
)

result = CLIENT.infer(
    image,
    model_id=MODEL_ID
)
```

The process is:

```text
Input Image
     ↓
PIL Image
     ↓
InferenceHTTPClient
     ↓
Roboflow Server
     ↓
Trained Model
     ↓
Object Detection
     ↓
Prediction Result
```

## 🧪 Test Inference Without Flask

Before starting the web application, you can test the inference code directly.

Place an image named:

```text
test.jpg
```

in the project root:

```text
Roboflow_Garbage_Detection/
│
├── inference.py
├── test.jpg
└── ...
```

Run:

```powershell
python inference.py
```

The program sends the image to the Roboflow model and prints the prediction result.

A result may contain information such as:

```text
Class: plastic
Confidence: 0.91
Bounding Box:
x
y
width
height
```

## 🌐 Run the Flask Application

Once the inference test works, start Flask:

```powershell
python app.py
```

You should see:

```text
* Running on http://127.0.0.1:5000
```

Open your browser:

```text
http://127.0.0.1:5000
```

## 🖥️ Using the Application

### Step 1

Open:

```text
http://127.0.0.1:5000
```

### Step 2

Click:

```text
Choose File
```

### Step 3

Select a garbage image.

### Step 4

Click:

```text
Detect Garbage
```

### Step 5

The application sends the image to the Roboflow model.

### Step 6

The detected objects and confidence scores are displayed on the webpage.

Example:

```text
Detection Results

PLASTIC
Confidence: 91.42%

CARDBOARD
Confidence: 87.16%
```

## 🔄 Complete Application Workflow

```text
             USER
               │
               ▼
        Upload Image
               │
               ▼
          index.html
               │
               ▼
            app.py
               │
               ▼
        Save Image
        to uploads/
               │
               ▼
        inference.py
               │
               ▼
      Roboflow Inference SDK
               │
               ▼
        Roboflow Server
               │
               ▼
       Trained Detection Model
               │
               ▼
          Predictions
               │
               ▼
            app.py
               │
               ▼
          index.html
               │
               ▼
       Display Results
```

## 🎯 Project Objectives

The main objectives are:

1. Use a large Roboflow dataset.
2. Create a dataset version.
3. Train an object detection model.
4. Access the trained model using the Roboflow Inference SDK.
5. Build a Python inference program.
6. Integrate inference into a Flask application.
7. Allow users to upload images.
8. Display detected garbage classes and confidence scores.

## 📚 What This Project Demonstrates

This project demonstrates the complete basic computer-vision workflow:

```text
Dataset
   ↓
Annotation
   ↓
Dataset Version
   ↓
Model Training
   ↓
Model
   ↓
Inference
   ↓
Web Application
```

It is suitable for demonstrating:

* Roboflow datasets
* Dataset versions
* Object detection
* Model training
* Model inference
* Python integration
* Flask integration
* API-based AI inference

## 🐛 Troubleshooting

### `ModuleNotFoundError: No module named 'inference_sdk'`

Make sure the correct Conda environment is active:

```powershell
conda activate roboflow
```

Check:

```powershell
python --version
```

Then install:

```powershell
python -m pip install inference-sdk
```

### `401 Unauthorized`

Check:

* API key is correct
* API key has access to the model
* API key has not expired/revoked
* `.env` is being loaded

Test:

```powershell
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(bool(os.getenv('ROBOFLOW_API_KEY')))"
```

Expected:

```text
True
```

### `400 Malformed base64 input image`

Check that the input image is a valid image.

Run:

```powershell
python -c "from PIL import Image; img=Image.open('test.jpg'); print(img.format, img.size)"
```

Expected output:

```text
JPEG (640, 480)
```

If the image cannot be opened, replace `test.jpg` with a valid image.

## 🔐 Security

Never expose your Roboflow API key in:

* GitHub repositories
* README files
* Screenshots
* Public source code
* Frontend JavaScript
* Chat messages

Store the API key in `.env`.

Example:

```env
ROBOFLOW_API_KEY=YOUR_API_KEY
```

## 🚀 Future Improvements

The project can later be extended with:

* Bounding-box visualization
* Multiple image upload
* Batch inference
* Prediction history
* Confidence threshold controls
* Downloadable prediction results
* Camera/live detection
* Database integration
* User authentication
* Deployment to a cloud platform

## 👩‍💻 Author

**Nikitha Kantumuchu**

### Project Category

**Computer Vision / Artificial Intelligence**

### Domain

**Object Detection and Image Classification**

### Primary Platform

**Roboflow**

### Backend

**Python + Flask**
