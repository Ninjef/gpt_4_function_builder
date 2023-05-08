from dotenv import load_dotenv

from src.create_task.create_new_task import create_new_task

load_dotenv()

# TODO: This test costs money. We should mock out the OpenAI call or make it easy to disable this test easily.
def test_can_get_input_task_metadata_and_code():
    import os
    openai_key = os.environ.get("OPENAI_KEY")
    new_task, task_uuid = create_new_task(task_type="input", desired_action="read a csv file", openai_key=openai_key)

    assert task_uuid is not None
    assert len(task_uuid) > 0
    assert type(task_uuid) == str

    assert new_task is not None
    task_keys = new_task.keys()

    assert "task_name" in task_keys
    assert len(new_task["task_name"]) > 0

    assert "metadata" in task_keys

    assert "python_function" in task_keys
    python_function = new_task["python_function"]
    assert "def" in python_function
    assert "\n" in python_function

    metadata = new_task["metadata"]
    assert "user_inputs" in metadata.keys()
    assert "packages_used" in metadata.keys()

    user_inputs = metadata["user_inputs"]
    assert len(user_inputs.keys()) > 0

    packages_used = metadata["packages_used"]
    assert len(packages_used) > 0
