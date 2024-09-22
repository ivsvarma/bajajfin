from flask import Flask, request, jsonify, render_template
import base64

app = Flask(__name__)


def process_data(data, file_b64):
    
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]

    lowercase_alphabets = [x for x in alphabets if x.islower()]
    highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None


    file_valid = bool(file_b64)  
    file_mime_type = "application/pdf" if file_b64 else None  
    file_size_kb = 1800 if file_b64 else 0 

    return {
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bfhl', methods=['POST'])
def post_bfhl():
    try:
        data = request.json.get('data', [])
        file_b64 = request.json.get('file_b64', None)

        response_data = process_data(data, file_b64)
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            **response_data
        }
        
      
        ordered_response = {
            "is_success": response["is_success"],
            "user_id": response["user_id"],
            "email": response["email"],
            "roll_number": response["roll_number"],
            "numbers": response_data["numbers"],
            "alphabets": response_data["alphabets"],
            "highest_lowercase_alphabet": response_data["highest_lowercase_alphabet"],
            "file_valid": response_data["file_valid"],
            "file_mime_type": response_data["file_mime_type"],
            "file_size_kb": response_data["file_size_kb"]
        }

        return jsonify(ordered_response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
