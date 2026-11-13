from ollama import Client
from pathlib import Path

IMAGE_PATH = Path(__file__).parent.parent / 'inputs' / 'image1.png'
client = Client(host='http://127.0.0.1:11434')

def main():
    """
    extract text from an image file
    """
    print(f'图片路径：{IMAGE_PATH}')
    stream = client.chat(
        model='qwen3.5:2b',
        stream=True,
        messages=[
            {
                'role': 'user',
                'content': '提取图片中的文字，不要输出任何多余的内容。',
                'images': [IMAGE_PATH]
            },
        ],
    )

    print('图片内容：', end='', flush=True)
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

    print()

if __name__ == "__main__":
    main()
