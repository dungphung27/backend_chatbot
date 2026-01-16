from embedding import completion
def summarize_query_history(query_history):
    # Lấy danh sách câu hỏi của user từ history
    

    query_text = "\n".join([f"- {q}" for q in query_history])

    prompt = f"""
You are an AI assistant.
Given the following list of user queries, identify the main topics that are searched most frequently.
Group similar queries into the same topic and summarize them in a short, clear bullet list.

User queries:
{query_text}

Output format:
- Topic 1: short description
- Topic 2: short description
- Topic 3: short description
"""

    response = completion(prompt)
    return response
    