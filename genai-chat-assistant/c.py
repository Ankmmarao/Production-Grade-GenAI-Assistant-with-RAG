import google.generativeai as genai

# Add your Gemini API key
genai.configure(api_key="AIzaSyCR75vobImYDFjdbosNV7rvhHMEt9AjDqg")

# List available models
for model in genai.list_models():
    
    if "generateContent" in model.supported_generation_methods:
        print(model.name)