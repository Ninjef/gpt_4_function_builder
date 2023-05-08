from flask import Flask, render_template, request

from src.create_task.create_new_task import create_new_task
from src.create_task.commit_task_to_folder import commit_task_to_folder

from src.constants import USER_TASKS_PATH

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main_page():
    return render_template("index.html")

@app.route('/api/get_data', methods=['GET'])
def get_data():
    return {"message": "Hello World!"}

# make task should take in a json object with the following structure:
# {
#   "desired_action": "action_name",
#   "task_type": "task_type"
# }
@app.route('/api/task/create', methods=['POST'])
def make_task():
    import os
    try:
        response_body = request.get_json()
    except Exception as error:
        return {"message": "Error parsing request body: {}".format(error)}, 400

    desired_action = response_body.get("desired_action")
    if not desired_action:
        return {"message": "No desired_action provided"}, 400

    task_type = response_body.get("task_type")
    if not task_type:
        return {"message": "No task_type provided"}, 400

    openai_key = os.environ.get("OPENAI_KEY")
    if not openai_key:
        return {"message": "No OPENAI_KEY provided"}, 400

    try:
        task_definition, task_uuid = create_new_task(task_type=task_type, desired_action=desired_action, openai_key=openai_key)
    except Exception as error:
        return {"message": "Error creating new task: {}".format(error)}, 500

    try:
        commit_task_to_folder(task_definition=task_definition, task_uuid=task_uuid)
    except Exception as error:
        return {"message": "Error committing task to folder: {}".format(error)}, 500

    return {"task_id": "{}".format(task_uuid), "task_name": task_definition["task_name"], "message": "Task Created!"}

if __name__ == "__main__":
    app.run(debug=True, port=8000)
