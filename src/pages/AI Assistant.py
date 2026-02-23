import streamlit as st
from openai import OpenAI

#############################################################
# enable vector database search to search for similar prompts#
#############################################################
__import__("pysqlite3")
import sys

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
import chromadb

########
# Header#
########
st.set_page_config(page_title="Help")
st.title("Ask syllabus related questions here!")

###########################
# API KEY - make it secret#
###########################
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

#############################################
# File Input for Prompt and Output Parameters#
#############################################
with open(r"src/rules.txt", "r", encoding="utf-8") as f:
    rules = f.read()

with open(r"src/content.txt", "r", encoding="utf-8") as f:
    content = f.read()

################################################################################
# Open chroma client to store the prompt and input data to use for search later#
################################################################################
chroma = chromadb.PersistentClient(path=".chroma")
col = chroma.get_or_create_collection(name="tradeapp")


###########################################################################
# Embed the text and set it to a numeric vector for easier search retrieval#
###########################################################################
def embed(text):
    return (
        client.embeddings.create(model="text-embedding-3-small", input=text)
        .data[0]
        .embedding
    )


###########################################################################
# If collection or search database is empty, add in embedding of 2 files
# Make sure this collection is never empty during search
###########################################################################
if col.count() == 0:
    col.add(
        ids=["rules", "content"],
        documents=[rules, content],
        embeddings=[embed(rules), embed(content)],
        metadatas=[{"source": "content"}, {"source": "rules"}],
    )


######################################################################
# Use chroma to embed the user input and return top 8 similar prompts#
# Then concatenate into 1 single context string for the Chatbot#
######################################################################
def retrieve(query, k=8):
    res = col.query(query_embeddings=[embed(query)], n_results=k)
    docs = res["documents"][0] if res.get("documents") else []
    return "\n\n".join(docs)


################################################################################
# Conserve chat history so that every new input has been contextualised by the AI
################################################################################
if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

##############################
# Provide chat input field box#
##############################
prompt = st.chat_input("Insert your queries here", max_chars=6767)

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    context = retrieve(prompt, k=8)

    #####################
    # Instructing the Bot#
    #####################
    system = (
        "You are a accredited investor teaching trading to teenagers "
        "Use ONLY the context provided. If the answer is not in the context, please use ur own sources with relevant citations.\n\n"
        "CONTEXT:\n"
        f"{context}"
    )

    msgs = [{"role": "system", "content": system}] + st.session_state.messages

    ########################
    # Setting up the Chatbot#
    ########################
    with st.chat_message("assistant"):

        def gen():
            stream = client.chat.completions.create(
                model="gpt-4o-mini", messages=msgs, stream=True
            )
            for event in stream:
                delta = event.choices[0].delta
                if delta and delta.content:
                    yield delta.content

        full = st.write_stream(gen())

    st.session_state.messages.append({"role": "assistant", "content": full})
