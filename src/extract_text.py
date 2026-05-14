from ollama import chat
from pathlib import Path

def main():
    """
    extract text from an image file
    """
    image_path = Path('../static/image1.png')
    stream = chat(
        model='qwen3.5:2b',
        messages=[{'role': 'user', 'content': '提取图片中的文字', 'images': [image_path]}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":
    import time
    start = time.time()
    try:
        main()
    except Exception as e:
        print(e)
    end = time.time()
    print(f'\n\n程序运行 {round(end-start, 2)}s')
