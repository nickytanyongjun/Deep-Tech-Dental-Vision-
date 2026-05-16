import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from PIL import Image
import io

app = Flask(__name__)

# --- Configuration ---
# In a professional app, use environment variables: os.getenv("GEMINI_API_KEY")
API_KEY = "AIzaSyCkH2hiqSJNes31u7GOqbatmdaY9KbXAjE" 
genai.configure(api_key=API_KEY)

# Using the May 2026 stable release
model = genai.GenerativeModel("gemini-2.5-flash")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    file = request.files['image']
    try:
        img = Image.open(file.stream)
        
        prompt = """
        Estimate the age of the person from this dental X-ray.
        Analyze specifically: tooth eruption, wisdom teeth development, root formation, and jaw maturity.
        
        Return the result in Markdown format with clear headers.
        answer me ythe years old and the reason only.
        """
        
        response = model.generate_content([prompt, img])
        return jsonify({"result": response.text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)