import uuid
from decouple import config
# from astrapy import create_client, http_methods

from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import openai
from langchain.embeddings import OpenAIEmbeddings

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

from datasets import load_dataset


# setup cassandra db cluster from astra
cloud_config = {
    "secure_connect_bundle": config("ASTRA_DB_BUNDLE_PATH")
}
auth_provider = PlainTextAuthProvider(config("ASTRA_CLIENT_ID"), config("ASTRA_CLIENT_SECRET"))
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
astra_db_session = cluster.connect()

# initiate open ai llm
llm = openai.OpenAI(openai_api_key=config("OPENAI_API_KEY"))
emb = OpenAIEmbeddings(openai_api_key=config("OPENAI_API_KEY"))


# connect embedding with cassandra instance from astra.
datastore = Cassandra(
    embedding=emb,
    session=astra_db_session,
    keyspace=config("ASTRA_DB_KEYSPACE"),
    table_name="alpha_emb"
)

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

