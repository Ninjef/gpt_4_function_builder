# Python API Coding Sample  

## Video of me building this:
https://youtu.be/yafzBesUDgQ
This shows a few things:
1. How I can use TDD (Test Driven Development) to write software. With the exception of a few functions, I wrote the tests first, and iterated on the code until the tests passed.
2. How I can build new software efficiently by going from experimentation (failing/learning fast) to implementation in a highly iterative manner.

## Overview  
This is a sample of a Python API that can be used to create and run Python tasks. It uses OpenAI's GPT-4 API to generate Python code from natural language descriptions of tasks.  

Due to privacy concerns, I cannot share the full repo. This repo is a subset of the full repo, and is meant to demonstrate my coding style and ability to work with Python and APIs.  
## Context  
- This code was completed in 9 hours over 4 days.  
- This is an example of my POC code, meaning it was designed to be fast to iterate upon, and not to be production ready.  
- The backend, or `task_service` section is ready to be deployed as an AWS lambda function, or run as a local api.
- What I would do to make this production ready:  
  - Standardize the API request validation and response format  
  - Add API security using a securely generated token (JWT)  
  - Use a formatting library like Black, and a linting library like Flake8  
  - Abstract logical code away from the API requests  
  - Reorganize the code / tests to follow a standard pattern  
  - Make more comprehensive types  
  - Add tests for the API itself  
  - Add more testing around edge cases and exceptions  
  - Add a CI/CD pipeline  

# API  
A set of endpoints for creating python tasks + metainfo about those tasks using natural language, as well as running those tasks.  

## API Requirements  
- [ ] Python `3.11`  

## Setup API  

From a clean Python environment with pip installed:  
`pip install -r task_service/requirements-dev.txt`  
`cp .example.env ./.env`  

Add your Open AI key to the .env  

## Run API  
`cd task_service`  
`python app.py`  

## Run Tests  
`pytest task_service`  
Note: some tests cost money as some of them call the acutal OpenAi API for completions. They don't use the most expensive models though.  

# Client  
Does nothing except display a test button right now.  

## Client Requirements  
- [ ] NPM `9.6`  
- [ ] Node `v20.0`  

## Run Client  
`cd client`  
`npm install`  
`npm run dev-client`  
Open a new terminal  
`npm run start-tool-service`  

## API Examples  
Example API request:  

`POST http://localhost:8000/api/task/create`  
Body:  
```
{   
    "desired_action": "given a dataset containing a bunch of text, extract the most important topics from each text",  
    "task_type": "passthrough"  
}  
```

On successful response, a folder with a UUID will be generated under ./user_tasks/<the_uuid>. That folder will contain a `function.py` file and a `metadata.json` file.  
