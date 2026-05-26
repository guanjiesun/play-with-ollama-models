from ollama import chat
from pathlib import Path

INPUT_DIR = Path(__file__).parent.parent / 'inputs'

def main():
    """
    extract text from an image file
    """
    image_path = INPUT_DIR / 'image.png'
    stream = chat(
        model='qwen3.5:2b',
        messages=[{'role': 'user', 'content': '提取图片中的文字', 'images': [image_path]}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
