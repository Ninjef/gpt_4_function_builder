def get_single_completion_from_openai(openai_key: str, prompt: str, model: str = "text-davinci-003", total_tokens: int = 250):
    import openai

    model = model or "text-davinci-003"
    openai.api_key = openai_key
    max_tokens = get_max_tokens(prompt, total_tokens)

    print(f'Calling openai with model {model} and max_tokens {max_tokens}')
    if "gpt-4" in model.lower():
        # TODO: this should technically be tested, but it'd be expensive without a mock openai api
        completion = openai.ChatCompletion.create(model=model, max_tokens=max_tokens, temperature=0.5, messages=[
            {
                "role": "system", "content": "You are an expert in python coding and the JSON format. You will always respond with a valid JSON object, and that JSON object will have a property for a python function. The python function will work out of the box as long as the required packages are installed."
            },
            {
                "role": "user", "content": prompt
            }
        ])
        return completion.choices[0].message["content"]
    else:
        completion = openai.Completion.create(model=model, prompt=prompt, max_tokens=max_tokens, temperature=0.5)
        return completion.choices[0].text

def get_max_tokens(prompt: str, total_tokens: int = 250):
    import tiktoken
    enc = tiktoken.encoding_for_model("gpt-4")
    tokens = len(enc.encode(prompt))

    return max(total_tokens - tokens, 0)