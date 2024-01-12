#--------------------------------------------#

import google.generativeai as genai

GOOGLE_API_KEY="YOUR_API_KEY"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

text = input("input: ")
response = model.generate_content(text)

print(response.text.replace('**', ''))

#--------------------------------------------#
