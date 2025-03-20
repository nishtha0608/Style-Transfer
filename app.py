from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Ensure upload folder exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload', methods=['POST'])
def upload():
    if 'content-image' not in request.files or 'style-image' not in request.files:
        return jsonify({"error": "Missing files"}), 400

    content_file = request.files['content-image']
    style_file = request.files['style-image']

    if content_file.filename == '' or style_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(content_file.filename) or not allowed_file(style_file.filename):
        return jsonify({"error": "Invalid file type"}), 400

    # Save uploaded files
    content_filename = secure_filename(content_file.filename)
    style_filename = secure_filename(style_file.filename)
    content_path = os.path.join(app.config['UPLOAD_FOLDER'], content_filename)
    style_path = os.path.join(app.config['UPLOAD_FOLDER'], style_filename)
    content_file.save(content_path)
    style_file.save(style_path)

    # Load images
    content_image = plt.imread(content_path)
    style_image = plt.imread(style_path)

    # Preprocess images
    content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.0
    style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.0
    style_image = tf.image.resize(style_image, (256, 256))

    # Load TF-Hub model
    hub_module = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

    # Apply style transfer
    outputs = hub_module(tf.constant(content_image), tf.constant(style_image))
    stylized_image = outputs[0].numpy()[0]

    # Save stylized image
    stylized_filename = 'stylized_output.png'
    stylized_path = os.path.join(app.config['UPLOAD_FOLDER'], stylized_filename)
    plt.imsave(stylized_path, stylized_image)

    # Return URLs to the frontend
    return jsonify({
        "content_image": f"/uploads/{content_filename}",
        "style_image": f"/uploads/{style_filename}",
        "stylized_image": f"/uploads/{stylized_filename}",
    })

if __name__ == '__main__':
    app.run(debug=True)