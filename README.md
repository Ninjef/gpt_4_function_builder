# Python API Coding Sample  

## Overview  
This is a sample of a Python API that can be used to create and run Python tasks. It uses OpenAI's GPT-4 API to generate Python code from natural language descriptions of tasks.  

Due to privacy concerns, I cannot share the full repo. This repo is a subset of the full repo, and is meant to demonstrate my coding style and ability to work with Python and APIs.  

## Context  
- This code was completed in 4 days.  
- This is an example of my POC code, meaning it was designed to be fast to iterate upon, and not to be production ready.  
- I would like to bring attention to the TDD (Test Driven Development) approach I used to develop this. With the exception of a few functions, I wrote the tests first, and iterated on the code until the tests passed. This is a great way to ensure that the code is well tested, and that the code is written in a way that is easy to test, and easy to understand.
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

# API  
A set of endpoints for creating python tasks + metainfo about those tasks using natural language, as well as running those tasks.  

## API Requirements  
- [ ] Python `3.11`  

## Setup API  

From a clean Python environment:  
`cd task_service`  
`pip install -r requirements-dev.txt`  
`cd ..`  
`cp .example.env ./.env`  

Add your Open AI key to the .env  

## Run API  
`cd task_service python app.py`  

## Run Tests  
`pytest task_service`  
Note: some tests cost money as some of them call the acutal OpenAi API for completions. They don't use the most expensive models though.  

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
