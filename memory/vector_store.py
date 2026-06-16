import chromadb

client = chromadb.PersistentClient(path="./memory_db")

collection = client.get_or_create_collection(
    name="chat_memory"
)

def save_memory(text):

    collection.add(
        documents=[text],
        ids=[str(collection.count())]
    )


def get_memories(query, n=3):

    results = collection.query(
        query_texts=[query],
        n_results=n
    )

    if results["documents"]:
        return "\n".join(results["documents"][0])

    return ""