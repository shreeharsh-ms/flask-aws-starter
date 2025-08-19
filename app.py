from flask import Flask, render_template, request, redirect
from utils.s3_helper import upload_file_to_s3, list_files_in_s3

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

if __name__ == "__main__":
    app.run(debug=True)
