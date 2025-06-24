from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Write a one-sentence bedtime story about a unicorn."
)
print("Vector Embedding",response)
print("Vector Embedding length",len(response.data[0].embedding))
