import google.generativeai as genai

genai.configure(api_key="AIzaSyCkH2hiqSJNes31u7GOqbatmdaY9KbXAjE")

for model in genai.list_models():
    print(model.name)