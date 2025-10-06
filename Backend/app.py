# app.py
import os
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)
MODEL_PATH = "models/flower_model.keras"


# Load model once on startup
model = None
class_indices = None

def load():
    global model, class_indices
    model = load_model(MODEL_PATH)

    # Load class names from data/flowers folder
    data_dir = "data/flowers"
    if os.path.isdir(data_dir):
        classes = sorted([d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))])
        class_indices = {i: c for i, c in enumerate(classes)}
    else:
        class_indices = None

# ---------- ROUTES ----------
@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/index")
def index_page():
    return render_template("index.html")

@app.route("/model")
def model_page():
    return render_template("model.html")

@app.route("/dataset")
def dataset_page():
    return render_template("dataset.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/results")
def results_page():
    return render_template("results.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

# ---------- IMAGE PROCESSING ----------
def prepare_image(image, target_size=(224,224)):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    arr = img_to_array(image)
    arr = tf.keras.applications.mobilenet_v2.preprocess_input(arr)
    arr = np.expand_dims(arr, axis=0)
    return arr

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"success": False, "error": "No image uploaded"}), 400
    file = request.files["image"]
    if file.filename == "":
        return jsonify({"success": False, "error": "Empty filename"}), 400

    try:
        image = Image.open(file.stream)
        x = prepare_image(image)
        preds = model.predict(x)[0]
        top_idx = int(np.argmax(preds))
        confidence = float(preds[top_idx])

        if class_indices is not None:
            label = class_indices.get(top_idx, str(top_idx))
        else:
            label = str(top_idx)

        return jsonify({
            "success": True,
            "prediction": label,
            "confidence": round(confidence, 4)
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    load()
    app.run(host="0.0.0.0", port=5000, debug=True)
