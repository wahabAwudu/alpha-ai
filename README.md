# Alpha AI

The beginning of my journey to become a great Generative AI and Prompt Engineer.

In this project, I aspire to use some AI tools and platforms such as...
* [LangChain](https://python.langchain.com/docs/get_started/introduction)
* [OpenAI](https://openai.com)
* [Datastax AstraDB](https://www.datastax.com/)
* [Datasets from Huggingface](https://huggingface.co/)

..to train some pre-defined datasets.

## Aims and Goals
* Build my fundamental knowledgebase on Generative AI
* Understand vector embeddings and how they play a key part in achieving accurate and well-trained data.
* Prepare me with the skills I need to contribute to open-source projects.
* Equip me with the pre-requisite skills I need to help with company projects.
* Build my personal ideas around AI to speed up the growth of the commercial, manufacturing, security, government, and tech sectors.


## Set up `.env` file

1. Sign up on [Open AI and Generate API keys](https://platform.openai.com/account/api-keys)

*Make sure you copy the api keys before closing the modal on the page. and save it in the `.env` file as `OPENAI_API_KEY`*

2. If you want use the Huggingface utility, create an account on [Datastax and create a vectors database](https://docs.datastax.com/en/astra/astra-db-vector/get-started/quickstart.html).

The following ENV variable values can be obtained from the Datastax when you create your first vector database. `However, these are only required if you wish to use the Huggingface utility`.

* `ASTRA_DB_ID`
* `ASTRA_DB_KEYSPACE`
* `ASTRA_CLIENT_ID`
* `ASTRA_CLIENT_SECRET`
* `ASTRA_CLIENT_TOKEN`
* `ASTRA_SECURE_CONNECT_BUNDLE`


## Installation - Python Virtual Environment

Make sure python is installed and then run:
```
make venv
```
This will create a new virtual environment in a `venv` directory.


To activate the virtual environment, run:
```
make activate
```
For windows, use 
```
make activate-win
```

Next, run:
```
make install
```
This will install all dependecies from the `requirements.txt` file.


Finally, to start the application, run:
```
make run
```
This will start the application using [streamlit](https://streamlit.io).

*Note: if you get an error, make sure you have an `.env` file, or create one based on `.env.example`.*


## Installation - Native with Python

Install dependencies by running:

```
pip install -r requirements.txt
```

This will install all dependecies from the `requirements.txt` file.

Then run the application with streamlit:

```
streamlit run main.py
```

