def commit_task_to_folder(task_definition: dict, task_uuid: str):
    from pathlib import Path
    from src.constants import USER_TASKS_PATH

    expected_user_tasks_path = Path(USER_TASKS_PATH)
    expected_init_file_path = Path(expected_user_tasks_path, '__init__.py')

    if not expected_user_tasks_path.exists():
        expected_user_tasks_path.mkdir(parents=True, exist_ok=True)
    if not expected_init_file_path.exists():
        with open(expected_init_file_path, 'w') as init_file:
            init_file.write('')

    task_folder_path = Path(USER_TASKS_PATH, task_uuid)
    task_folder_path.mkdir(parents=True, exist_ok=True)

    task_metadata_path = Path(task_folder_path, 'metadata.json')
    task_function_path = Path(task_folder_path, 'function.py')
    task_init_path = Path(task_folder_path, '__init__.py')

    import json
    with open(task_metadata_path, 'w') as metadata_file:
        json.dump(task_definition['metadata'], metadata_file)

    with open(task_function_path, 'w') as function_file:
        function_file.write(task_definition['python_function'])

    with open(task_init_path, 'w') as init_file:
        init_file.write('')
