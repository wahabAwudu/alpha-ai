# Alpha AI

The beginning of my journey to become a great Generative AI and Prompt Engineer.

In this project, I aspire to use some of AI tools and platforms such as..
* [LangChain](https://python.langchain.com/docs/get_started/introduction)
* [OpenAI](https://openai.com)
* [Datastax AstraDB](https://www.datastax.com/)
* [Datasets from Huggingface](https://huggingface.co/)

..to train some pre-defined datasets.

## Aims and Goals
* Build my fundamental knowledgebase on Generative AI
* Understand vector embeddings and how it plays a key part in achieving acurate and well trained data.
* Prepare me with the skills I need to contribute to open source project.
* Provide me the pre-requisite skills I need to help company projects.
* Build my personal ideas around AI to speed up growth of the commercial, business, and tech sector.

## Installation - Poetry

The most efficient way to get up and running is to install [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

and then run:

```
make install
```

This will install all dependecies from the `pyproject.toml` file.

next, run:

```
make prep
```

This will activate a virtual environment with the installed dependencies you installed above and also set executable permissions on the file `main.py` file.

finally, run:
```
make run
```
This will execute the scripts in the `main.py` file.


*Note: if you get an error, make sure you have a `.env` file, or create one based on `.env.example`.*


## Installation - Native

Install dependencies by running:

```
pip3 install -r requirements.txt
```

This will install all dependecies from the `requirements.txt` file.

Then run the script:

```
python3 main.py
```

## Set up `.env` file

1. Sign up on [Open AI and Generate API keys](https://platform.openai.com/account/api-keys)

*Make sure you copy the api keys before closing the modal on the page. and save it in the `.env` file as `OPENAI_API_KEY`*

2. Create an account on [Datastax and create a vectors database](https://docs.datastax.com/en/astra/astra-db-vector/get-started/quickstart.html).

The following ENV variable values can be obtained from the Datastax when you create your first vector database.

* `ASTRA_DB_ID`
* `ASTRA_DB_REGION`
* `ASTRA_DB_KEYSPACE`
* `ASTRA_CLIENT_ID`
* `ASTRA_CLIENT_SECRET`
* `ASTRA_CLIENT_TOKEN`

Finally,
download the `astra db bundle zip` *(made available when you create your first Astra vector database)* into your project root directory `alpha/` then copy the file path of the zip file for the final environment variable `ASTRA_DB_BUNDLE_PATH`
