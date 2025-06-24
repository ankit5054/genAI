from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# CoT
SYSTEM_PROMPT='''
    You are helpful assistant who is specialized in resolving query.
    You work on START, PLAN, ACTION AND OBSERVE mode.
'''

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT}
    ]
)

print(response.choices[0].message.content)