
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pathlib import Path
import uuid

from model import load_silkworm_model
from predict import predict_silkworm
from recommendation import recommend_mulberry

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

# Load the trained AI model once when the application starts
model = load_silkworm_model()


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    recommendation = None
    image_url = None
    error = None

    if request.method == "POST":

        if "image" not in request.files:
            error = "Please select a silkworm image."

        else:
            file = request.files["image"]

            if file.filename == "":
                error = "No image selected."

            elif not allowed_file(file.filename):
                error = "Please upload a JPG, JPEG, or PNG image."

            else:
                try:
                    original_name = secure_filename(file.filename)
                    unique_name = f"{uuid.uuid4().hex}_{original_name}"

                    image_path = UPLOAD_FOLDER / unique_name
                    file.save(image_path)

                    prediction = predict_silkworm(
                        image_path, model
                    )

                    recommendation = recommend_mulberry()

                    image_url = f"/static/uploads/{unique_name}"

                except Exception as e:
                    error = f"Could not process the image: {e}"

    return render_template(
        "index.html",
        prediction=prediction,
        recommendation=recommendation,
        image_url=image_url,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from pathlib import Path
import uuid

from model import load_silkworm_model
from predict import predict_silkworm
from recommendation import recommend_mulberry

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "static" / "uploads"

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

# Load the trained AI model once when the application starts
model = load_silkworm_model()


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    recommendation = None
    image_url = None
    error = None

    if request.method == "POST":

        if "image" not in request.files:
            error = "Please select a silkworm image."

        else:
            file = request.files["image"]

            if file.filename == "":
                error = "No image selected."

            elif not allowed_file(file.filename):
                error = "Please upload a JPG, JPEG, or PNG image."

            else:
                try:
                    original_name = secure_filename(file.filename)
                    unique_name = f"{uuid.uuid4().hex}_{original_name}"

                    image_path = UPLOAD_FOLDER / unique_name
                    file.save(image_path)

                    prediction = predict_silkworm(
                        image_path, model
                    )

                    recommendation = recommend_mulberry()

                    image_url = f"/static/uploads/{unique_name}"

                except Exception as e:
                    error = f"Could not process the image: {e}"

    return render_template(
        "index.html",
        prediction=prediction,
        recommendation=recommendation,
        image_url=image_url,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
