from src.create_task.get_task_prompt import get_task_prompt
from src.call_openai import get_single_completion_from_openai
from src.create_task.get_metadata_and_code_from_task_build_response import get_metadata_and_code_from_task_build_response
from src.exceptions.api_exceptions import TaskCreationPromptException, OpenAiCompletionException, OpenAiResponseParsingException
from src.constants import DEFAULT_OPENAI_MODEL_TO_USE

def create_new_task(task_type: str, desired_action: str, openai_key: str, openai_model: str = DEFAULT_OPENAI_MODEL_TO_USE):
    try:
        llm_prompt = get_task_prompt(task_type=task_type, desired_action=desired_action)
    except Exception as error:
        raise TaskCreationPromptException("Error generating prompt: {}".format(error))

    try:
        llm_response = get_single_completion_from_openai(openai_key=openai_key, prompt=llm_prompt, total_tokens=1250, model=openai_model)
    except Exception as error:
        raise OpenAiCompletionException("Error generating response from OpenAI: {}".format(error))

    try:
        output_ready_for_writing = get_metadata_and_code_from_task_build_response(llm_response)
    except Exception as error:
        raise OpenAiResponseParsingException("Error parsing response from OpenAI: {}".format(error))

    import uuid
    task_uuid = str(uuid.uuid4())

    return output_ready_for_writing, task_uuid