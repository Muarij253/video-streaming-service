from flask import Flask, request, send_file, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'videos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_video():
    video = request.files['video']
    path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(path)
    return jsonify({"message": "Video uploaded", "path": path})

@app.route("/videos", methods=["GET"])
def list_videos():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify(files)

@app.route("/stream/<filename>")
def stream_video(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    return send_file(path, mimetype='video/mp4')

if __name__ == "__main__":
    app.run(debug=True)
