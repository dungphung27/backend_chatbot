from embedding import completion
def refine_long_query(long_query):
    prompt = f"""
You are a query rewriting system for semantic search.

Task:
- Rewrite the input into a short, clear search query.
- Keep important actions (e.g. install, support, performance).
- Keep important context (e.g. OS, hardware).
- Remove greetings and filler words.
- Do NOT explain.
- Output ONE single line only.

Input:
{long_query}

Search query:
"""
    response = completion(prompt)

    return response


# test_queries = [
#     "Chào bạn, mình muốn cài Docker trên Ubuntu 22.04 nhưng không biết có cần bật virtualization trong BIOS không?",
#     "Mình đang tìm cách cài ROS2 Humble trên Ubuntu 20.04, có cần gỡ ROS1 trước không?",
#     "Cho mình hỏi là Windows 11 có chạy được WSL2 không và cần bật những tính năng gì?",
#     "Mình đang dùng Mac M1, liệu có chạy được Ollama không và có bị chậm không?",
#     "Mình có GPU RTX 3050, chạy LLaVA có ổn không hay phải giảm batch size?",
#     "Cho hỏi RTX 3060 12GB thì fine-tune Llama2 7B có đủ VRAM không?",
#     "Mình đang phân vân không biết nên dùng embedding model nào cho tiếng Việt, có gợi ý không?",
#     "Ollama có hỗ trợ chạy multi-GPU không hay chỉ 1 GPU?",
#     "Code Python của mình bị lỗi segmentation fault khi dùng numpy, không hiểu tại sao?",
#     "Mình build C++ project bằng CMake trên Windows thì bị lỗi linker, có cách fix không?",
#     "Chạy Flask app thì bị port 5000 already in use, xử lý thế nào?",
#     "Tại sao code React của mình render rất chậm khi list có 10k phần tử?",
#     "Mình đang làm hệ thống RAG nhưng kết quả search không chính xác lắm, có cách nào cải thiện không?",
#     "Vector database nào nhẹ, dễ deploy cho project nhỏ?",
#     "Có nên dùng chunk size lớn hay nhỏ khi làm embedding tài liệu?",
#     "Làm sao để route câu hỏi ngắn sang search, câu dài sang summarize?",
#     "Submap trong Cartographer là gì và tại sao lại cần dùng nó?",
#     "Làm sao phát hiện loop closure trong SLAM mà không dùng ROS?",
#     "Particle filter khác gì pose graph optimization trong SLAM?",
#     "Chào bạn, mình đang làm đồ án về robot tự hành trong nhà, có dùng LIDAR và SLAM, nhưng bản đồ bị drift nhiều khi đi xa, mình không dùng ROS mà code tay, vậy có cách nào giảm drift và phát hiện loop closure không?"
# ]

# for i, q in enumerate(test_queries, 1):
#     optimized = refine_long_query(q)
#     print(f"\n{i}. Original: {q}")
#     print(f"   Optimized: {optimized}")
