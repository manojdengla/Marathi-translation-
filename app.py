
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '')

    response = requests.post("https://libretranslate.de/translate", data={
        'q': text,
        'source': 'en',
        'target': 'mr',  # Marathi
        'format': 'text'
    })

    if response.status_code == 200:
        translated_text = response.json()['translatedText']
        return jsonify({'translatedText': translated_text})
    else:
        return jsonify({'error': 'Translation failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
