import pandas as pd
import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d5b91dd69da1f8ed0c23be82a1844484'.format(movie_id))  # getting details of movie from movie id
    data = response.json()  # converting the details of movie to json
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']  # we are fetching the poster path of the movie


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # users input movie index is fetched
    distances = similarity[movie_index]  # user's input movie's similarity distance array is fetched
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        #movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))  # here dataframe which was saved as movie_dict.pkl in wb from is loaded
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

# selected_movie_name (it is variable) saves the movies selected
selected_movie_name = st.selectbox(
    'Select the movies',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

# error ocurred while directly loading pandas dataframe so we converted df to dictonary as in above coe
# '''movies_list = pickle.load(open('movies.pkl','rb'))
# movies_list = movies_list['title'].values
# option = st.selectbox(
#     "Select the movies",
#     movies_list
# )'''
