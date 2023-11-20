import uuid
from decouple import config
# from astrapy import create_client, http_methods

from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from datasets import load_dataset
from config import init_astra_vector_db, init_open_ai

datastore = init_astra_vector_db()
llm = init_open_ai(0.5)


def extract_huggingface_data():
    
    print("Loading dummy data")
    # fetch a specific dataset from huggingface hub.
    # https://pypi.org/project/datasets/
    # https://huggingface.co/datasets
    new_dataset = load_dataset("Biddls/Onion_News", split="train")
    headlines = new_dataset["text"][:50]

    print("Generate embeddings and store in AstraDB")
    datastore.add_texts(headlines)

    vector_data = VectorStoreIndexWrapper(vectorstore=datastore)

    first_question = True
    while True:
        if first_question:
            query_text = input("\nEnter your question (or type 'quit' to exit): ")
            first_question = False
        else:
            query_text = input("\nWhat's your next question (or type 'quit' to exit): ")
    
        if query_text.lower() == "quit":
            break

        print(f"QUESTION: {query_text}")
        answer = vector_data.query(query_text, llm=llm).strip()
        print(f"ANSWER: {answer}\n")

        print("DOCUMENTS BY RELEVANCE:")
        for doc, score in datastore.similarity_search_with_score(query_text, k=4):
            print(f"{score} {doc.page_content[:60]}")

