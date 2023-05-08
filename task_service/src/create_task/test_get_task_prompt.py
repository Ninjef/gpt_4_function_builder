from src.create_task.get_task_prompt import get_task_prompt
from src.create_task.prompt_constants import PROMPT_JSON_EXAMPLE

def test_get_task_prompt_returns_expected_prompt_for_input_tool_type():
    expected_action = "pull in data from sqlite"
    tool_prompt = get_task_prompt("input", expected_action)
    assert len(tool_prompt) > 1000
    assert PROMPT_JSON_EXAMPLE.strip("\n").strip(" ").replace("\\n", "").replace(" ", "").replace("\n", "") in tool_prompt.strip("\n").strip(" ").replace("\\n", "").replace(" ", "").replace("\n", "")

    assert "return a single variable that is a pandas dataframe" in tool_prompt
    assert "final input variable" not in tool_prompt

    assert tool_prompt.find("JSON Object:") > tool_prompt.find(expected_action)
    assert expected_action in tool_prompt

def test_get_task_prompt_returns_expected_prompt_for_passthrough_tool_type():
    expected_action = "find the maximum value in a column"
    tool_prompt = get_task_prompt("passthrough", expected_action)
    assert len(tool_prompt) > 1000
    PROMPT_JSON_EXAMPLE.strip("\n").strip(" ").replace("\\n", "").replace(" ", "").replace("\n", "") in tool_prompt.strip("\n").strip(" ").replace("\\n", "").replace(" ", "").replace("\n", "")

    assert "return a single variable that is a pandas dataframe" in tool_prompt
    assert "final input variable" in tool_prompt
    assert tool_prompt.find("JSON Object:") > tool_prompt.find(expected_action)
    assert expected_action in tool_prompt