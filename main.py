from google import genai
import os
from openai import OpenAI

client = genai.Client()


response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print("gemini: " + response.text)



##Chatgpt
#client = OpenAI()

#Response = client.responses.create(
#    model="gpt-5",
#    input="Write a one-sentence bedtime story about a unicorn."
#)

#print("chatgpt: " + response.output_text)

##Deepseek
#client = OpenAI(api_key=os.environ.get(''), base_url="https://api.deepseek.com")

#response = client.chat.completions.create(
    #model="deepseek-chat",
    #messages=[
        #{"role": "system", "content": "You are a helpful assistant"},
        #{"role": "user", "content": "Hello"},
    #],
    #stream=False
#)

#print(response.choices[0].message.content)