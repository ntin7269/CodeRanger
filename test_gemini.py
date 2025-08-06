import google.generativeai as genai

genai.configure(api_key="AIzaSyCegnTdDjnaHhbEDjHm5jTY2giqyVIKd14")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("say hello in 3 languages")
print(response.text)
