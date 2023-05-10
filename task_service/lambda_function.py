from src.create_task.create_new_task import create_new_task


def lambda_handler(event, context):
    import os

    desired_action = "read text from a given url and output it into a dataframe"
    if not desired_action:
        return {"message": "No desired_action provided"}, 400

    task_type = "input"
    if not task_type:
        return {"message": "No task_type provided"}, 400

    openai_key = os.environ.get("OPENAI_KEY")
    if not openai_key:
        return {"message": "No OPENAI_KEY provided"}, 400

    try:
        task_definition, task_uuid = create_new_task(task_type=task_type, desired_action=desired_action, openai_key=openai_key)
    except Exception as error:
        return {"message": "Error creating new task: {}".format(error)}, 500

    import boto3

    dashless_task_uuid = task_uuid.replace("-", "")

    bucket_name = "chimera-user-tasks"
    metadata_json_filename = "metadata.json"
    python_filename = "function.py"
    s3_folder = f"test_tasks/{dashless_task_uuid}/"

    metadata_json_path = s3_folder + metadata_json_filename
    python_path = s3_folder + python_filename

    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=metadata_json_path, Body=task_definition['metadata'])
    s3.Bucket(bucket_name).put_object(Key=python_path, Body=task_definition['python_function'])

    return {"event": dir(event), "context": dir(context), "task_definition": task_definition, "task_uuid": task_uuid}
