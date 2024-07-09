import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Is Jaws a correct answer to the question Which movie was the first to feature a color sequence?")
print(response.text)