import ollama
import base64
from ollama_client import ollama_client
def generate_image_description_with_llava(image_path, prompt):
    """
    Sử dụng LLaVA thông qua Ollama để mô tả nội dung hình ảnh.
    Args:
        image_path (str): Đường dẫn đến file ảnh.
        prompt (str): Câu hỏi bạn muốn hỏi LLaVA về bức ảnh.
    Returns:
        str: Mô tả/trả lời của LLaVA về bức ảnh.
    """
    try:
        with open(image_path, "rb") as f:
            image_data = f.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')

        response = ollama_client.chat(
            model='qwen3-vl:235b-cloud', # Hoặc phiên bản LLaVA bạn đã tải (ví dụ: llava:13b)
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                    'images': [encoded_image] # Truyền ảnh dưới dạng base64
                }
            ],
            options={
                'temperature': 0.2 # Giữ độ sáng tạo thấp để mô tả chính xác
            }
        )
        return response['message']['content']
    except Exception as e:
        return f"Lỗi khi gọi LLaVA: {e}"

# Ví dụ sử dụng:
image_file = "image.jpg"
question = "Hãy đọc nội dung có trong bức ảnh"
description = generate_image_description_with_llava(image_file, question)
print(description)