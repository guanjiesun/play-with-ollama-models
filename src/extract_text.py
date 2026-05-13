from ollama import chat
from pathlib import Path

def main():
    """
    extract text from an image file
    """
    image_path = Path('image.png')
    stream = chat(
        model='qwen3.5:9b',
        messages=[{'role': 'user', 'content': '提取图片中的文字', 'images': [image_path]}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":
    main()
