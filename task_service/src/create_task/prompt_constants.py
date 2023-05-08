PROMPT_JSON_EXAMPLE = """
{
    "task_name": <the task's name>,
    "task_text": <text of the task>,
    "user_inputs": {
        "variable1": {"type": "string", "description": "//description of what this variable does"},
        "variable2":  {"type": "int", "description": "//description of what this variable does"},
        "variable3": {"type": "date", "description": "//description of what this variable does"}
        //etc...
    },
   "example_input_and_output_parameters": {
       "variable1": "john smith",
       "variable2": 15,
       "variable3": "17 Apr 2022"
      //etc...
   },
  "example_input_and_output_datasets": {
     "input1": {"columns": ["country", "state", "population"], "values": [["USA", "USA", "UK"],  ["CO", "AL", "Scotland"], [219893, 3828, 48382]]},
    "output1": {"columns": ["country", "total_population"], "values": [["USA", "UK"], [1231921, 129934]]}
  }
   "packages_used": [
       "pandas",
       "requests",
       "pillow",
       etc...
   ],
  "python_function": "def main_function(column_name, operator, value, input1):\n    import pandas as pd\n    df = input1\n#etc..."
}
"""