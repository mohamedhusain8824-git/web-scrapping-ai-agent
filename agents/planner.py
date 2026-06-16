from agents.chat import chat_agent
from agents.summarizer import summarize
from agents.search_agent import search_agent

def route(query):

    q = query.lower()

    # Search Agent
    if q.startswith("search"):
        return search_agent(query)

    # Summarizer Agent
    elif q.startswith("summarize"):
        return summarize(query)

    # Chat Agent
    else:
        return chat_agent(query)