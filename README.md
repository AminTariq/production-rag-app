# production-rag-app

This is a production grade implementation of the RAG model for question answering.

## Requirements

- Python 3.12 or later

#### Install Python using MiniConda

1) Download and Install MiniConda from [here](https://www.anaconda.com/docs/getting-started/concepts/anaconda-or-miniconda#quick-command-line-install)
2) Create a new enviroment using the following command:
```bash
$ conda create -n production-rag-app python=3.12
```
3) Activate the environment:
```bash
$ conda activate production-rag-app
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables 

```bash
$ cp .env.example .env
```

Set your enviroment variables in the `.env` file. 

## Run Docker Compose Services

```bash
$ sudo docker compose up -d
```

## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 4000
```

## POSTMAN Collection

Download the POSTMAN collection from [/assets/production-rag-app.postman_collection.json](/assets/production-rag-app.postman_collection.json)