from ollama import chat

def main():
    """
    get streaming response from local LLM model
    """
    stream = chat(
        model='qwen3.5:9b',
        messages=[{'role': 'user', 'content': '如何成为一名优秀的 RPA 工程师？'}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":
    main()
