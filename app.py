import os

from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

from inference import run_inference


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )


@app.route("/predict", methods=["POST"])
def predict():

    if "image" not in request.files:

        return render_template(
            "index.html",
            error="No image selected."
        )

    image = request.files["image"]

    if image.filename == "":

        return render_template(
            "index.html",
            error="Please select an image."
        )

    filename = secure_filename(image.filename)

    image_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    image.save(image_path)

    # Call your existing Roboflow inference code
    result = run_inference(image_path)

    predictions = result.get("predictions", [])

    return render_template(
        "index.html",
        image=filename,
        predictions=predictions
    )


if __name__ == "__main__":

    app.run(debug=True)