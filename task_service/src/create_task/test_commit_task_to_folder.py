import pytest

from src.create_task.commit_task_to_folder import commit_task_to_folder
from src.constants import USER_TASKS_PATH

def teardown_user_tasks():
    import shutil
    sub_files_and_directories = USER_TASKS_PATH.iterdir()
    tool_folders_to_delete = [file_path for file_path in sub_files_and_directories if file_path.name != '__init__.py']
    for path in tool_folders_to_delete:
        if path.is_dir():
            shutil.rmtree(path)

def teardown_user_tasks_from_root():
    import shutil
    if USER_TASKS_PATH.exists():
        shutil.rmtree(USER_TASKS_PATH)

def test_can_user_tasks_folder_gets_created_if_not_exists():
    from pathlib import Path
    try:
        teardown_user_tasks_from_root()

        task_definition, task_uuid = get_task_and_task_uuid()
        expected_user_tasks_path = Path(USER_TASKS_PATH)
        expected_init_file_path = Path(expected_user_tasks_path, '__init__.py')

        commit_task_to_folder(task_definition, task_uuid)
        assert expected_user_tasks_path.exists()
        assert expected_init_file_path.exists()

    except Exception as error:
        pytest.fail(error)
    finally:
        teardown_user_tasks()

def test_can_commit_task_to_foler():
    from pathlib import Path

    try:
        teardown_user_tasks()

        task_definition, task_uuid = get_task_and_task_uuid()
        expected_task_folder_path = Path(USER_TASKS_PATH, task_uuid)

        commit_task_to_folder(task_definition, task_uuid)
        assert expected_task_folder_path.exists()

        expected_task_metadata_path = Path(expected_task_folder_path, 'metadata.json')
        expected_task_function_path = Path(expected_task_folder_path, 'function.py')
        expected_task_init_path = Path(expected_task_folder_path, '__init__.py')

        assert expected_task_metadata_path.exists()
        assert expected_task_function_path.exists()
        assert expected_task_init_path.exists()


    except Exception as error:
        pytest.fail(error)
    finally:
        teardown_user_tasks()

def test_can_commit_task_details_to_task_files():
    from pathlib import Path
    import json

    try:
        teardown_user_tasks()

        task_definition, task_uuid = get_task_and_task_uuid()
        expected_task_folder_path = Path(USER_TASKS_PATH, task_uuid)

        commit_task_to_folder(task_definition, task_uuid)
        expected_task_metadata_path = Path(expected_task_folder_path, 'metadata.json')
        expected_task_function_path = Path(expected_task_folder_path, 'function.py')
        expected_task_init_path = Path(expected_task_folder_path, '__init__.py')

        assert expected_task_metadata_path.exists()
        assert expected_task_function_path.exists()
        assert expected_task_init_path.exists()
        # test the contents of each file

        with open(expected_task_metadata_path, 'r') as metadata_file:
            metadata = json.load(metadata_file)
        
        assert metadata == task_definition['metadata']

        with open(expected_task_function_path, 'r') as function_file:
            function = function_file.read()
        
        assert function == task_definition['python_function']


    except Exception as error:
        pytest.fail(error)
    finally:
        teardown_user_tasks()


def get_task_and_task_uuid():
    import json

    task_json_str = '{"task_name": "Read In Data From Database", "metadata": {"user_inputs": {"database_name": "string", "table_name": "string", "column_name": "string", "operator": "string", "value": "string"}, "packages_used": ["pandas", "psycopg2"]}, "python_function": "def main_function(database_name, table_name, column_name, operator, value):\\n    import pandas as pd\\n    import psycopg2\\n    conn = psycopg2.connect(database_name)\\n    cursor = conn.cursor()\\n    query = \'SELECT * FROM \' + table_name + \' WHERE \' + column_name + \' \' + operator + \' \' + value + \';\' \\n    df = pd.read_sql(query, conn)\\n    return df"}'
    task_uuid = '13347989-5dd8-45da-a81c-4282dc3c0c7e'
    task_json = json.loads(task_json_str)

    return task_json, task_uuid