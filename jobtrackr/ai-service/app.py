from flask import Flask, request, jsonify
from utils.resume_parser import parse_resume

app = Flask(__name__)

@app.route('/uploadResume', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        resume_data = parse_resume(file)
        return jsonify(resume_data), 200

if __name__ == '__main__':
    app.run(debug=True)