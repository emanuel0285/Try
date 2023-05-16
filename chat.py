#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

# Import your question-answering function
from my_question_answering_module import get_answer

# Streamlit app code
def main():
    st.title("Question and Answer Chatbot")

    # User input
    question = st.text_input("Ask a question")

    # Get answer and display
    if st.button("Get Answer"):
        answer = get_answer(question)
        st.write("Answer:", answer)

if __name__ == "__main__":
    main()


# In[ ]:




