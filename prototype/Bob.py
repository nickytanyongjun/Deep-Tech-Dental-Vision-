import google.generativeai as genai
import tkinter as tk
from tkinter import filedialog
from PIL import Image

# Put your Gemini API key here
genai.configure(api_key="My Api Key")

# Load Gemini vision model
model = genai.GenerativeModel("gemini-2.5-flash")

# Open file picker
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Dental X-Ray Image",
    filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
)

if not file_path:
    print("No image selected.")
    exit()

# Open image
image = Image.open(file_path)

print("Analyzing dental X-ray...\n")

try:
    response = model.generate_content([
        """
Estimate the age of the person from this dental X-ray.

Use:
- tooth eruption
- wisdom teeth development
- root formation
- jaw maturity

Reply in this format:

Estimated Age: __

Reason:
- ...
- ...
""",
        image
    ])

    print("===== AI RESPONSE =====\n")
    print(response.text)

except Exception as e:
    print("Error:", e)
