from embeddings import get_file, get_text_chunks, create_embeddings,load_embeddings
import streamlit as st

# when file is uploaded by user, create new vector data for that file
def create_new_vector_db(file):
    with st.spinner("Creating vector data"):
        text = get_file(file)
        text_chunks = get_text_chunks(text)
        # vectordb = create_embeddings(text_chunks)
        vectordb = load_embeddings()
    return vectordb, text_chunks

def handle_file_upload(file):
    if file:
        vectoredb, text_chunks = create_new_vector_db(file)
        return vectoredb,text_chunks

    else:                             
        pass

def rrf(bm25_results, k=1):
    merged_scores = {}
    for doc_chunk, score in bm25_results:
        merged_scores[doc_chunk] = score

    sorted_docs = sorted(merged_scores.items(), key=lambda item: item[1], reverse=True)
    final_results = [{"content": doc_chunk.page_content, "metadata": doc_chunk.metadata} for doc_chunk, score in sorted_docs[:k]]
    return final_results




