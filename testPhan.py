import ollama
import sys

def chatbot_router():
    print("--- Đang khởi động và nạp mô hình vào RAM... ---")
    
    try:
        # Load sẵn mô hình phanloai và llama3
        ollama.generate(model='phanloai', prompt='', keep_alive=-1)
        ollama.generate(model='llama3:8b', prompt='', keep_alive=-1)
        print("--- Hệ thống đã sẵn sàng! ---")
    except Exception as e:
        print(f"Lỗi khi load model: {e}")
        return

    print("(Gõ 'exit' hoặc 'quit' để thoát)")
    print("-" * 40)

    # 1. Danh sách từ khóa "bắt buộc" phải có để được coi là chuyên môn
    # Nếu không chứa từ nào trong này, chúng ta mặc định là "Ngoài lề"
    tu_khoa_chuyen_mon = [
        "lỗi", "hỏng", "lag", "bug", "không chạy", "đơ", "quay tròn", "404", "500", # Bug
        "voucher", "giảm giá", "khuyến mãi", "ưu đãi", "sale", "mã", "tặng",       # Marketing
        "tư vấn", "hỏi", "địa chỉ", "ship", "bao giờ", "đổi trả", "giá", "liên hệ" # Hỗ trợ
    ]

    while True:
        user_input = input("\nBạn: ").strip()
        
        if user_input.lower() in ['exit', 'quit', 'thoát']:
            print("Tạm biệt!")
            break
        if not user_input:
            continue

        try:
            # BƯỚC 1: KIỂM TRA TỪ KHÓA TRƯỚC (QUAN TRỌNG)
            # Nếu câu quá ngắn hoặc không có từ khóa liên quan đến dịch vụ, chuyển thẳng cho Llama3
            kiem_tra_tu_khoa = any(word in user_input.lower() for word in tu_khoa_chuyen_mon)
            
            # BƯỚC 2: GỌI MODEL PHÂN LOẠI
            nhan_res = ollama.generate(model='phanloai', prompt=user_input, stream=False)
            nhan_lower = nhan_res['response'].strip().lower().replace(".", "")

            # BƯỚC 3: LOGIC QUYẾT ĐỊNH
            # Chỉ coi là chuyên môn nếu:
            # (Model nói là chuyên môn) VÀ (Câu hỏi có từ khóa chuyên môn) VÀ (Không phải nhãn "ngoài lề")
            is_chuyen_mon = False
            found_label = ""

            if "bug" in nhan_lower and kiem_tra_tu_khoa:
                is_chuyen_mon = True
                found_label = "Bug"
            elif "marketing" in nhan_lower and kiem_tra_tu_khoa:
                is_chuyen_mon = True
                found_label = "Marketing"
            elif ("hỗ trợ" in nhan_lower or "ho tro" in nhan_lower) and kiem_tra_tu_khoa:
                is_chuyen_mon = True
                found_label = "Hỗ trợ khách hàng"

            # BƯỚC 4: TRẢ LỜI
            if is_chuyen_mon:
                print(f"-> [Hệ thống]: Nhận diện yêu cầu thuộc nhóm: {found_label}")
                # Ở đây bạn có thể thêm phản hồi mẫu của hệ thống nếu muốn
            else:
                # Nếu AI báo "ngoài lề" hoặc không thỏa mãn điều kiện từ khóa
                print("-> [AI Tự do]: Đang trả lời...")
                res_tu_do = ollama.generate(model='llama3:8b', prompt=user_input, stream=True)
                
                print("AI trả lời: ", end="", flush=True)
                for chunk in res_tu_do:
                    print(chunk['response'], end="", flush=True)
                print() 

        except Exception as e:
            print(f"Lỗi xử lý: {e}")

if __name__ == "__main__":
    chatbot_router()