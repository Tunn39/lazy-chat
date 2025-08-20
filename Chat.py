#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install streamlit openai


# In[3]:


import streamlit as st
from openai import OpenAI
import os

# Make sure your API key is set in your environment
# Example (Linux/Mac): export OPENAI_API_KEY="sk-proj-xxxx..."
# Example (Windows PowerShell): setx OPENAI_API_KEY "sk-proj-xxxx..."

client = OpenAI()

def rewrite_professional(message: str) -> str:
    """
    Rewrite message with a firm, professional tone and clear boundaries.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or "gpt-4o", "gpt-5" if available
        messages=[
            {"role": "system", "content": "Rewrite text in a firm, professional tone with clear boundaries."},
            {"role": "user", "content": message}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()


# --- Streamlit App UI ---
st.set_page_config(page_title="Professional Rewriter", page_icon="💼")

st.title("💼 Professional Message Rewriter")
st.write("Type your message below and get a firm, professional rewrite with clear boundaries.")

user_input = st.text_area("✍️ Your message:", height=150)

if st.button("Rephrase"):
    if user_input.strip():
        rewritten = rewrite_professional(user_input)
        st.subheader("✅ Professional Rewrite")
        st.success(rewritten)
    else:
        st.warning("Please enter a message first.")


# In[4]:


jupyter nbconvert --to script ProfessionalRewriter.ipynb


# In[ ]:




