import google.generativeai as genai

genai.configure(api_key="My APi Key")

for model in genai.list_models():
    print(model.name)
