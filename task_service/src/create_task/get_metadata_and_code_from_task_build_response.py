def get_metadata_and_code_from_task_build_response(task_build_response: str):
    import json
    # TODO: This isn't the best way to do this, but it works for now
    double_escaped_newline = "\\n"
    temporary_token_for_double_escaped_newline = "<<!%*<<DOUBLE_ESCAPED_NEWLINE>>!%*>>"

    response_without_newlines = task_build_response.replace(double_escaped_newline, temporary_token_for_double_escaped_newline).replace('\n', '').replace(temporary_token_for_double_escaped_newline, double_escaped_newline).strip("\\n").strip("\n")
    response_with_some_quirky_llm_json_ideas_cleaned_up = remove_common_unparsable_json_characteristics(response_without_newlines)
    task_build_response = json.loads(response_with_some_quirky_llm_json_ideas_cleaned_up)

    return {
        "task_name": task_build_response["task_name"],
        "metadata": {
            "user_inputs": task_build_response["user_inputs"],
            "packages_used": task_build_response["packages_used"]
        },
        "python_function": task_build_response["python_function"]
    }

def remove_common_unparsable_json_characteristics(task_build_response: str):
    import re
    clean_json_string = re.sub('(")[\s]*,[\s]*(}.*"python_function":\s*"def)', r'\1\2', task_build_response)
    clean_json_string = re.sub('(")[\s]*,[\s]*(].*"python_function":\s*"def)', r'\1\2', clean_json_string)
    clean_json_string = re.sub('(])[\s]*,[\s]*(}.*"python_function":\s*"def)', r'\1\2', clean_json_string)
    clean_json_string = re.sub('(])[\s]*,[\s]*(].*"python_function":\s*"def)', r'\1\2', clean_json_string)
    clean_json_string = re.sub('(})[\s]*,[\s]*(].*"python_function":\s*"def)', r'\1\2', clean_json_string)
    clean_json_string = re.sub('(})[\s]*,[\s]*(}.*"python_function":\s*"def)', r'\1\2', clean_json_string)
    return clean_json_string