from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import LLMChain
from langchain.vectorstores.faiss import FAISS
from .config import get_open_ai_embeddings, init_open_ai

emb = get_open_ai_embeddings()


def get_youtube_transcript(video_url):
    # extract transcript from youtube video
    loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=True)
    transcript = loader.load()

    # split the transcript into different chunks.
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    # save it on a vectors embedding database.
    db = FAISS.from_documents(docs, emb)
    return db


def get_response_from_query(db, query, k=4):
    docs = db.similarity_search(query, k=k)
    docs_pages_content = " ".join([doc.page_content for doc in docs])
    llm = init_open_ai(0.5, "text-davinci-003")

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="""
        Answer the following question: {question}
        By searching the following video transcript: {docs}
        Only use factual information from the transcript to answer the question.
        If you don't have enough information to answer the question, simply say "I don't know".
        Your answers should be detailed.
    """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    resp = chain.run(question=query, docs=docs_pages_content)
    return resp.replace("\n", "")

if __name__ == "__main__":
    print(get_youtube_transcript(
        "https://www.youtube.com/watch?v=EJHPltmAULA"
    ))
