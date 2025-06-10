from dotenv import load_dotenv
import os
import pickle
import streamlit as st
import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import requests
import streamlit as st  # if you're using Streamlit



load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return "https://image.tmdb.org/t/p/w500" + poster_path
        return "https://via.placeholder.com/500"
    except Exception as e:
        st.error(f"Error fetching movie poster: {e}")
        return "https://via.placeholder.com/500"


def recommend(movie):
    # Normalize movie title for better matching
    normalized_title = movie.lower().strip()

    if normalized_title not in movies['title'].str.lower().str.strip().values:
        st.error(f"Movie '{movie}' not found in the dataset.")
        return [], []

    index = movies[movies['title'].str.lower().str.strip() == normalized_title].index[0]

    # Create TF-IDF vectors from the tags
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(movies['tags'])

    # Calculate cosine similarity based on tags
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Get the pairwise similarity scores of all movies with that movie
    distances = list(enumerate(cosine_sim[index]))

    # Sort the movies based on the similarity scores
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:  # Get top 5 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


# Load the movies dataset
try:
    movies = pickle.load(open('D:\pycharm\Pycharm Projects\movie recommendation\movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies)
except Exception as e:
    st.error(f"Error loading movie data: {e}")
    st.stop()

st.header('Movie Recommender System')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    if recommended_movie_names:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])
        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])
    else:
        st.write("No recommendations available.")

if st.button("Exit"):
    st.write("You can close this tab or navigate away.")

