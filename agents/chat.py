from groq import Groq
from dotenv import load_dotenv
import os

from memory.vector_store import (
    save_memory,
    get_memories
)

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def chat_agent(query):

    memories = get_memories(query)

    prompt = f"""
Previous Memory:

{memories}

Current User Message:

{query}

Use memory when relevant.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content

    save_memory(f"User: {query}")
    save_memory(f"Assistant: {answer}")

    return answer