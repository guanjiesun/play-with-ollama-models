"""
前提条件
1. Ollama 必须已安装并正在运行
2. 下载（拉取）一个模型以供库使用： ollama pull <模型名称>，例如：ollama pull qwen3.5:9b

"""

from ollama import chat

def main():
    """
    get streaming response from local LLM model
    """
    stream = chat(
        model='qwen3.5:9b',
        messages=[{'role': 'user', 'content': 'RPA 工程师的典型工作流'}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":
    main()
