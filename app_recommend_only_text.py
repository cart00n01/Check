import pandas as pd
import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # users input movie index is fetched
    distances = similarity[movie_index]  # user's input movie's similarity distance array is fetched
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))  # here dataframe which was saved as movie_dict.pkl in wb from is loaded
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

# selected_movie_name (it is variable) saves the movies selected
selected_movie_name = st.selectbox(
    'Select the movies',
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)

    for i in recommendations:
        st.write(i)
