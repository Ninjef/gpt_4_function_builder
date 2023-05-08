from pathlib import Path

USER_TASKS_PATH = Path('user_tasks') if "task_service" not in str(Path('user_tasks').absolute().parent) else Path('../user_tasks')
TEMP_FLOW_ID = "temp_flow_id"
DEFAULT_OPENAI_MODEL_TO_USE = [
    None,
    'gpt-4',
    'text-davinci-003'
][1]
