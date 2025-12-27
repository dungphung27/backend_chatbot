# github: https://raw.githubusercontent.com/expo/expo/refs/heads/main/docs/pages/get-started/start-developing.mdx
# page: https://docs.expo.dev/get-started/start-developing/
import requests
import frontmatter
import ollama

def parseFromDoc(slug):
    url = f"https://raw.githubusercontent.com/expo/expo/refs/heads/main/docs/pages/{slug}.mdx"
    res = requests.get(url)
    res.raise_for_status()  # báo lỗi nếu 404
    text = requests.get(url).text
    post = frontmatter.loads(text)
    return post
def handleDoc(slug):
    data = parseFromDoc(slug)

slug = "get-started/start-developing"
post = parseFromDoc(slug)
print(post)
# print(post.content)
