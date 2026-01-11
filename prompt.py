from embedding import generateEmbedding, completion
from index import parseFromDoc
import frontmatter
import ollama
from supabase_client import supabase    

def build_full_prompt(query, docs_context):
    prompt_boilerplate = "Answer the question posed in the user query section using the provided context"
    user_query_boilerplate = "USER QUERY: "
    document_context_boilerplate = "CONTEXT: "
    final_answer_boilerplate = "Final Answer: "

    filled_prompt_template = (
        f"{prompt_boilerplate}\n"
        f"{user_query_boilerplate} {query}\n"
        f"{document_context_boilerplate} {docs_context}\n"
        f"{final_answer_boilerplate}"
    )

    return filled_prompt_template
def mergeDocs(responses):
    list_of_contents = []
    responses = responses.data
    for response in responses:
        content = parseFromDoc(response['id'])
        list_of_contents.append(str(content.content))    
    return "\n".join(list_of_contents)
def runPromt(query):
    vector = generateEmbedding(query)
    responses = (
        supabase.rpc("match_documents",{
            "query_embedding": vector,
            "match_threshold" : 0.2,
            "match_count": 3
        })
        .execute()
    )
    contents = mergeDocs(responses)
    filledPrompt = build_full_prompt(query,contents)
    completion(filledPrompt)

runPromt("How to initialize a new Expo project")