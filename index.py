# github: https://raw.githubusercontent.com/expo/expo/refs/heads/main/docs/pages/get-started/start-developing.mdx
# page: https://docs.expo.dev/get-started/start-developing/
import requests
import frontmatter
import ollama
from supabase_client import supabase
from slugs import slugs
from embedding import generateEmbedding
def parseFromDoc(slug):
    url = f"https://raw.githubusercontent.com/expo/expo/refs/heads/main/docs/pages/{slug}.mdx"
    res = requests.get(url)
    res.raise_for_status()  
    text = res.text
    post = frontmatter.loads(text)
    return post
def handleDoc(slug):
    data = parseFromDoc(slug)
    # embedding = ollama.embed(
    #     model='embeddinggemma',
    #     input=data.content
    # )
    embedding = generateEmbedding(data.content)
    print(embedding)  
    title = data.metadata['title']
    url = f"https://docs.expo.dev/{slug}"
    print(data.metadata['title'])
    supabase.table("docs").insert({
        "title": title,
        "vector": embedding,
        "url": url,
        "id": slug
    }).execute()
def handleAllDocs():
    for slug in slugs:
        handleDoc(slug)


# handleAllDocs()
# print(post.content)
