import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

st.title("CHATBOT API PROJECT!")

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

user_input = st.text_input(
    "Enter your question:",
    placeholder="Type your question here..."
)

if user_input:

    if user_input.lower() == "quit":
        st.warning("Goodbye!")

    else:
        response = model.generate_content(user_input)

        st.success("AI Response:")
        st.success(response.text)