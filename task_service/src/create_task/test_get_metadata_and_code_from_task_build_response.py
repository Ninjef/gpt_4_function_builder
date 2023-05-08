from src.create_task.get_metadata_and_code_from_task_build_response import get_metadata_and_code_from_task_build_response, remove_common_unparsable_json_characteristics

def test_config_and_code_are_present_and_correct():
    # Note: this test is a bit brittle, but it's a good start
    #  TODO: make this test more robust

    llm_response_1, expected_output = get_llm_response_and_expected_output_1()
    actual_output = get_metadata_and_code_from_task_build_response(llm_response_1)
    assert actual_output == expected_output

def test_ability_to_remove_common_unparsable_json_characteristics():
    double_escaped_newline = "\\n"
    temporary_token_for_double_escaped_newline = "<<!%*<<DOUBLE_ESCAPED_NEWLINE>>!%*>>"
    mock_task_build_response = """
{"some": "slightly more",
    "complicated": {
        "json": "stuff",
        "and": "things",
        "with": [
            "a",
            "list",
            "inside",
        ],
    },
    "and": "some other stuff",
    "python_function": "def main_function():\\n    print(\'hello world\')"
    }
"""
    mock_task_build_response_no_newlines = mock_task_build_response.replace(double_escaped_newline, temporary_token_for_double_escaped_newline).replace('\n', '').replace(temporary_token_for_double_escaped_newline, double_escaped_newline).strip("\\n").strip("\n")
    assert remove_common_unparsable_json_characteristics(mock_task_build_response_no_newlines).replace("\n", "").replace(" ", "") == """
   {"some": "slightly more",
    "complicated": {
        "json": "stuff",
        "and": "things",
        "with": [
            "a",
            "list",
            "inside"
        ]
    },
    "and": "some other stuff",
    "python_function": "def main_function():\\n    print(\'hello world\')"
    }
""".replace("\n", "").replace(" ", "")


def get_llm_response_and_expected_output_1():
    llm_response_1 = '{\n    "task_name": "Postgres Table Reader",\n    "user_inputs": {\n        "column_name": "string",\n        "operator": "string",\n        "value": "string",\n        "host": "string",\n        "port": "int",\n        "database": "string",\n        "table": "string",\n        "username": "string",\n        "password": "string"\n    },\n   "packages_used": [\n       "pandas",\n       "sqlalchemy"\n   ],\n  "python_function": "def main_function(column_name, operator, value, host, port, database, table, username, password):\\n    import pandas as pd\\n    from sqlalchemy import create_engine\\n    engine = create_engine(\'postgresql://{username}:{password}@{host}:{port}/{database}\')\\n    df = pd.read_sql_table(\'{table}\', engine, columns=[column_name, operator, value])\\n    return df"}'
    expected_output = {
        "task_name": "Postgres Table Reader",
        "metadata": {
            "user_inputs": {
                "column_name": "string",
                "operator": "string",
                "value": "string",
                "host": "string",
                "port": "int",
                "database": "string",
                "table": "string",
                "username": "string",
                "password": "string"
            },
            "packages_used": [
                "pandas",
                "sqlalchemy"
            ]
        },
        "python_function": """def main_function(column_name, operator, value, host, port, database, table, username, password):\n    import pandas as pd\n    from sqlalchemy import create_engine\n    engine = create_engine(\'postgresql://{username}:{password}@{host}:{port}/{database}')\n    df = pd.read_sql_table(\'{table}\', engine, columns=[column_name, operator, value])\n    return df"""
    }
    return llm_response_1, expected_output