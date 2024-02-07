# First Time Setup

## Project Setup Instructions

To properly configure the environment for this project, you will need to create a `.env` file in the root directory. This file should contain the necessary API keys and configuration details for various services. Below is a template for the `.env` file with placeholders for the values you need to provide:

```
# Application Secret
SECRET_KEY=your_secret_key

# Database Configuration
SQLALCHEMY_DATABASE_URI=sqlite:///path_to_your_sqlite.db

# File Upload Service
UPLOAD_URL=https://prod-upload-langchain.fly.dev

# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key

# Redis Configuration
REDIS_URI=redis://your_redis_host:your_redis_port

# Pinecone Configuration
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV_NAME=your_pinecone_environment_name
PINECONE_INDEX_NAME=your_pinecone_index_name

# LangFuse Configuration
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
```

Please follow these steps to configure your project environment:

1. **Create Accounts & Obtain API Keys:** You will need to create accounts on the respective platforms (OpenAI, Pinecone, LangFuse) and generate API keys for each service.

2. **Configure the `.env` File:** Fill in the placeholders in the `.env` template with your actual API keys and configuration details.

3. **Place the `.env` File:** Ensure the `.env` file is located in the root directory of the project for the application to access these configurations during runtime.

By setting up the `.env` file as described, you will provide your project with the necessary credentials and configurations to interact with external services and databases. This setup is crucial for the full functionality of the application.

## Using Pipenv [Recommended]

```
# Install dependencies
pipenv install

# Create a virtual environment
pipenv shell

# Initialize the database
flask --app app.web init-db

```

## Using Venv [Optional]

These instructions are included if you wish to use venv to manage your evironment and dependencies instead of Pipenv.

```
# Create the venv virtual environment
python -m venv .venv

# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
flask --app app.web init-db
```

# Running the app [Pipenv]

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
pipenv shell
```

Then:

```
flask --app app.web init-db
```

# Running the app [Venv]

_These instructions are included if you wish to use venv to manage your evironment and dependencies instead of Pipenv._

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
inv dev
```

### To run the worker

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
inv devworker
```

### To run Redis

```
redis-server
```

### To reset the database

Open a new terminal window and create a new virtual environment:

```
# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate
```

Then:

```
flask --app app.web init-db
```
