from decouple import config
from langchain.llms.openai import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from langchain.vectorstores.cassandra import Cassandra


def init_open_ai(temperature=0.7, model=None):
    if model:
        return OpenAI(
            api_key=config("OPENAI_API_KEY"),
            temperature=temperature,
            model=model
        )
    return OpenAI(api_key=config("OPENAI_API_KEY"), temperature=temperature)

def get_open_ai_embeddings():
    return OpenAIEmbeddings(openai_api_key=config("OPENAI_API_KEY"))


def init_astra_vector_db():
    # setup cassandra db cluster from astra
    cloud_config = {
        "secure_connect_bundle": config("ASTRA_SECURE_CONNECT_BUNDLE")
    }
    auth_provider = PlainTextAuthProvider(config("ASTRA_CLIENT_ID"), config("ASTRA_CLIENT_SECRET"))
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    astra_db_session = cluster.connect()

    emb = get_open_ai_embeddings()
    
    # connect embedding with cassandra instance from astra.
    datastore = Cassandra(
        embedding=emb,
        session=astra_db_session,
        keyspace=config("ASTRA_DB_KEYSPACE"),
        table_name="alpha_emb"
    )
    return datastore

