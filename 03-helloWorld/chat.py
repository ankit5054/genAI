from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"user","content":"Hey, my name is Ankit."},
        {"role":"assistant","content":"Hi there, how can I assist you."},
        {"role":"user","content":"Whats my name?"},
    ]
    
)

print(response.choices[0].message.content)