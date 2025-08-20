from flask import Flask, render_template, request, redirect, jsonify

from utils.s3_helper import upload_file_to_s3, list_files_in_s3
import logging


app = Flask(__name__)


@app.route("/")
def index():
    return redirect("/upload")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            upload_file_to_s3(file, file.filename)
            return redirect("/gallery")
    return render_template("upload.html")

@app.route("/gallery")
def gallery():
    files = list_files_in_s3()
    return render_template("gallery.html", files=files)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

@app.route("/handle-file", methods=["POST"])
def handle_file():
    data = request.json
    filename = data.get("filename")
    if filename:
        app.logger.info(f"Received notification for file: {filename}")  # Use app.logger instead of print
        process_file(filename)
        return jsonify({"message": f"Processed file {filename}"}), 200
    else:
        return jsonify({"error": "Filename missing"}), 400

def process_file(filename):
    app.logger.info(f"Processing file: {filename}") 