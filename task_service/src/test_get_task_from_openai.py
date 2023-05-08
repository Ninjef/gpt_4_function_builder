from dotenv import load_dotenv
from src.call_openai import get_single_completion_from_openai, get_max_tokens

load_dotenv()
# NOTE: These tests cost actual money - but they're pretty cheap. Just don't run them on a loop or anything crazy like that!
def test_openai_request_succeeds():
    import os
    openai_key = os.environ.get("OPENAI_KEY")
    completion = get_single_completion_from_openai(openai_key, prompt="Write a number between 1 and 50", model="text-davinci-001")
    completion2 = get_single_completion_from_openai(openai_key, prompt="Write a number between 100 and 150", model="text-davinci-001")
    
    assert int(completion) > 0 and int(completion) <= 50
    assert int(completion2) > 99 and int(completion2) <= 150


def test_get_max_tokens_gets_expected_positive_token_number_a():
    prompt = "Write a number between 1 and 50"
    total_tokens = 500
    expected_max_tokens = 491

    assert get_max_tokens(prompt, total_tokens) == expected_max_tokens

def test_get_max_tokens_gets_expected_positive_token_number_b():
    prompt = "This is going to be a longer prompt that will take up more tokens, so buckele up, because we're heading to token town!"
    total_tokens = 500
    expected_max_tokens = 472

    assert get_max_tokens(prompt, total_tokens) == expected_max_tokens

def test_get_max_tokens_returns_zero_if_prompt_is_longer_than_total_tokens():
    prompt = "This is going to be a longer prompt that will take up more tokens, so buckele up, because we're heading to token town!"
    total_tokens = 8
    expected_max_tokens = 0

    assert get_max_tokens(prompt, total_tokens) == expected_max_tokens