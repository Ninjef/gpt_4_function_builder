from src.create_task.prompt_constants import PROMPT_JSON_EXAMPLE

def get_task_prompt(task_type: str, desired_action: str):
    if task_type == "input":
        return input_task_prompt(desired_action)
    elif task_type == "passthrough":
        return passthrough_task_prompt(desired_action)
    else:
        raise ValueError("task_type must be either 'input' or 'passthrough'")

def input_task_prompt(desired_action: str):
    return f"""
We're going to build a task that can be recognized by both the frontend and backend of our application. Everything necessary to accomplish this will be stored in a valid JSON object with no trailing commas. The frontend will need a section in the JSON object describing the user inputs, their types, expected outputs of the task, and the name of the task. The backend will need a section in the JSON object that is a python function, written as one long string, which takes the user inputs as arguments and accomplishes the task that is written by the user for this task. The python function we will create should always be called "main_function". We will write the python function code to accomplish this task importing all the libraries that are needed, and should not miss a single one, and the function will return a single variable that is a pandas dataframe. The python code will accept all the variables in the JSON object. The user inputs should be comprehensive, so as to ensure the user can fully configure the functionality, unless the user explicitly asks that a variable or set of variables be "static".

An template for the JSON object we'll create follows:
{PROMPT_JSON_EXAMPLE}
Task:
{desired_action}

JSON Object:
"""

def passthrough_task_prompt(desired_action: str):
    return f"""
We're going to build a task that can be recognized by both the frontend and backend of our application. Everything necessary to accomplish this will be stored in a valid JSON object with no trailing commas. The frontend will need a section in the JSON object describing the user inputs, their types, expected outputs of the task, and the name of the task. The backend will need a section in the JSON object that is a python function, written as one long string, which takes the user inputs as arguments and accomplishes the task that is written by the user for this task. The python function we will create should always be called "main_function". We will write the python function code to accomplish this task importing all the libraries that are needed above the function, and the function will return a single variable that is a pandas dataframe. The user inputs should be comprehensive, so as to ensure the user can fully configure the functionality, unless the user explicitly asks that a variable or set of variables be "static". The python code will accept all the variables in the JSON object, but it will also accept another variable that is not in the JSON object, which will be a pandas dataframe called "input1". This final input variable ("input1") is never in the JSON object, because the user does not configure it.

An template for the JSON object we'll create follows:
{PROMPT_JSON_EXAMPLE}

Task:
{desired_action}

JSON Object:
"""