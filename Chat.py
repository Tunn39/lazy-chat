import streamlit as st
from openai import OpenAI
import os

# Use API key from Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def rewrite_professional(message: str) -> str:
    """Rewrite message in firm, professional tone with clear boundaries."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Rewrite text in a firm, professional tone with clear boundaries."},
            {"role": "user", "content": message}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

# --- Streamlit UI ---
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
