import pickle
import streamlit as st
import requests

def recommend(movie):
  index = movies[movies['title'] == movie].index[0]
  distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
  recommended_movies_name = []
  recommended_movies_poster = []
  for i in distances[1:6]:
    movie_id = movies.iloc[i[0]].movie_id
    recommended_movies_name.append(movies.iloc[i[0]].title)
    recommended_movies_poster.append(fetch_poster(movie_id))
  return recommended_movies_name, recommended_movies_poster

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=<<api_key>>&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
   


st.header("Movie Recommendation System")

movies = pickle.load(open('web/model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('web/model/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

if st.button('Recommend'):
    recommened_movies_name,recommened_movies_poster = recommend(selected_movie)
