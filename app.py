from file_system import FileSystem
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
fs = FileSystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    files = request.files.getlist('files[]')
    for file in files:
        filename = file.filename
        fs.upload_file(filename)
    return jsonify({'message': 'Files uploaded successfully.'})

@app.route('/delete', methods=['POST'])
def delete_file():
    filename = request.form['filename']
    if not filename:
        return jsonify({'message': 'Please enter a filename to delete.'})
    if filename not in fs.files:
        return jsonify({'message': 'File does not exist.'})
    fs.delete_file(filename)
    return jsonify({'message': 'File deleted successfully.'})

@app.route('/delete_all', methods=['POST'])
def delete_all_files():
    if not fs.files:
        return jsonify({'message': 'There are no files to delete.'})
    fs.files = []  # Empty the list of files
    return jsonify({'message': 'All files deleted successfully.'})

@app.route('/list')
def list_files():
    files = fs.list_files()
    return render_template('list.html', files=files)

if __name__ == '__main__':
    app.run(debug=True)
