import os
import uuid
import pandas as pd
from flask import Flask, render_template, request, Response, send_from_directory, jsonify

# Initialize the Flask app and specify the templates folder
app = Flask(__name__, template_folder='templates')

# Home route: Displays login form or handles login submission
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # Show the login form
        return render_template('form.html')
    elif request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        password = request.form.get('password')

        # Simple authentication check
        if username == 'laxneth' and password == 'password':
            return 'SUCCESS'
        else:
            return 'FAILURE'

# File upload handler
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    # Handle plain text files
    if file.content_type == 'text/plain':
        return file.read().decode()
    
    # Handle Excel files (xlsx or xls)
    elif file.content_type in [
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/vnd.ms-excel"]:
        df = pd.read_excel(file)
        return df.to_html()

    # Unsupported file type
    else:
        return f"Unsupported file type: {file.content_type}"

# Convert uploaded Excel file to CSV and return it as a download
@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files.get('file')
    
    if not file:
        return "No file uploaded", 400

    try:
        df = pd.read_excel(file)
    except Exception as e:
        return f"Error reading file: {str(e)}", 500

    csv_data = df.to_csv()

    return Response(
        csv_data,
        mimetype='text/csv',
        headers={
            "Content-Disposition": "attachment; filename=results.csv"
        }
    )

# Convert Excel file to CSV and save it locally
@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
    file = request.files['file']
    df = pd.read_excel(file)

    # Create 'downloads' directory if it doesn't exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    # Generate a unique filename and save CSV
    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads', filename))

    # Render download page with filename info
    return render_template('download.html', filename=filename)

# Serve the saved CSV file for download
@app.route("/download/<filename>")
def download(filename):
    downloads_dir = os.path.join(os.getcwd(), 'downloads')
    return send_from_directory(downloads_dir, filename, download_name='result.csv')

# Handle POST requests with JSON payload (e.g., from JavaScript)
@app.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']

    # Save JSON data into a file
    with open("file.txt", 'w') as f:
        f.write(f'{greeting},{name}')
    
    # Return success response
    return jsonify({'message': 'Successfully written!'})

# Run the Flask development server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5444, debug=True)
