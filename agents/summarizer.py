from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def summarize(text):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": f"""
You are an AI Research Assistant.

Summarize the following article in:
- 5 bullet points
- Key takeaways
- Simple language

Article:

{text}
"""
            }
        ]
    )

    return response.choices[0].message.content