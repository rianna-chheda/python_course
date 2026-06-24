import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.set_page_config(
   page_title="AI Career Advisor",
   page_icon="🎓",
   layout="centered"
)

st.title("🎓 AI Career Advisor")
st.write("Get career guidance powered by Gemini AI.")

llm = ChatGoogleGenerativeAI(
   model="gemini-2.5-flash",
   temperature=0.7
)

prompt = PromptTemplate(
   input_variables=["profession"],
   template="""
You are an expert AI Career Advisor.

Analyze the profession: {profession}

Provide the response in the following format:

1. Required Skills
   - Technical Skills
   - Soft Skills

2. Learning Roadmap
   - Beginner Level
   - Intermediate Level
   - Advanced Level

3. Career Opportunities
   - Job Roles
   - Industries

4. Future Scope
   - Industry Demand
   - Emerging Trends

Give practical and industry-oriented advice.
"""
)

parser = StrOutputParser()

career_chain = prompt | llm | parser

profession = st.text_input("Enter a profession:", placeholder="Example: Data Scientist")

# Button
if st.button("Get Career Advice"):

   if profession:

      with st.spinner("Generating career advice..."):
            result = career_chain.invoke(
               {"profession": profession}
            )

      st.success("Career Advice Generated!")

      st.markdown("## AI Career Advisor")
      st.write(result)

   else:
      st.warning("Please enter a profession.")