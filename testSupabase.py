import os
from dotenv import load_dotenv
from supabase import create_client
import ollama

# Load biến môi trường
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Thiếu biến môi trường Supabase!")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

print("✅ Kết nối Supabase thành công")
data = {
    "content": "Hello Supabase từ Python"
}

res = supabase.table("test_table").insert(data).execute()
print(res)
