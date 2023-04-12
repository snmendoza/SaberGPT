# flake8: noqa
import streamlit as st


def faq():
    st.markdown(
        """
# FAQ
## How does SaberGPT work?
When you upload a document, it will be divided into smaller chunks 
and stored in a special type of database called a vector index 
that allows for semantic search and retrieval. In order to save this, 
you must provide an API key as well as a local directory where this database 
can be saved. 


## What do the numbers mean under each source?
For a PDF document, you will see a citation number like this: 3-12. 
The first number is the page number and the second number is 
the chunk number on that page. For DOCS and TXT documents, 
the first number is set to 1 and the second number is the chunk number.

## Are the answers 100% accurate?
No, the answers are not 100% accurate. KnowledgeGPT uses GPT-3 to generate
answers. GPT-3 is a powerful language model, but it sometimes makes mistakes 
and is prone to hallucinations. Also, KnowledgeGPT uses semantic search
to find the most relevant chunks and does not see the entire document,
which means that it may not be able to find all the relevant information and
may not be able to answer all questions (especially summary-type questions
or questions that require a lot of context from the document).

But for most use cases, KnowledgeGPT is very accurate and can answer
most questions. Always check with the sources to make sure that the answers
are correct.
"""
    )
