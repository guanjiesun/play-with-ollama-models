from ollama import chat

def main():
    stream = chat(
        model='qwen3:8b',
        messages=[{'role': 'user', 'content': '如何将 AI 与 RPA 融合？'}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":
    main()
