from chatbot import API_KEY
import streamlit as st
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Movie Recommendation System")

st.title("🎬 Movie Recommendation System")

movie_name = st.text_input("Enter Movie Name")

if st.button("Search Movie"):

    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={OMDB_API_KEY}"

    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":

        st.header(data["Title"])

        if data["Poster"] != "N/A":
            st.image(data["Poster"], width=300)

        st.write("⭐ IMDb Rating:", data["imdbRating"])
        st.write("🎭 Genre:", data["Genre"])
        st.write("🎬 Actors:", data["Actors"])
        st.write("📅 Released:", data["Released"])
        st.write("📝 Plot:", data["Plot"])

        prompt = f"""
        Write a short movie review in 100 words.

        Movie: {data['Title']}
        Genre: {data['Genre']}
        Plot: {data['Plot']}
        IMDb Rating: {data['imdbRating']}
        """

        review = model.generate_content(prompt)

        st.subheader("🤖 Gemini AI Review")
        st.write(review.text)

    else:
        st.error("Movie not found.")