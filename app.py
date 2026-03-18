import pickle
import html
import streamlit as st
import requests


st.set_page_config(page_title="NextWatch", layout="wide")

st.markdown(
        """
        <style>
            .main .block-container {
                max-width: 1580px;
                padding-top: 0.3rem;
                padding-left: 2.2rem;
                padding-right: 2.2rem;
                padding-bottom: 2rem;
            }
            .app-title {
                margin-bottom: 0.2rem;
                font-size: 2.25rem;
                text-align: center;
                margin-top: 0.5rem;
                color: var(--text-color);
            }
            .app-subtitle {
                color: var(--text-color);
                opacity: 0.78;
                margin-bottom: 1.2rem;
                font-size: 1.05rem;
                text-align: center;
            }
            .input-gap {
                margin-top: 0.6rem;
                margin-bottom: 0.9rem;
            }
            .button-gap {
                margin-top: 0.4rem;
                margin-bottom: 1.2rem;
            }
            .selectbox-wrapper {
                max-width: 600px;
                margin: 0 auto;
            }
            .button-wrapper {
                max-width: 600px;
                margin: 0 auto;
            }
            .section-title {
                margin-top: 1.2rem;
                margin-bottom: 0.9rem;
                font-size: 1.55rem;
                color: var(--text-color);
            }
            .movie-card {
                max-width: 250px;
                margin: 0 auto;
                text-align: center;
            }
            .movie-card-poster {
                width: 100%;
                height: 360px;
                object-fit: cover;
                border-radius: 0.55rem;
                display: block;
            }
            .movie-card-title {
                margin-top: 0.55rem;
                min-height: 3rem;
                max-height: 3rem;
                text-align: center;
                font-weight: 600;
                line-height: 1.45rem;
                font-size: 1rem;
                overflow: hidden;
                display: -webkit-box;
                -webkit-line-clamp: 2;
                -webkit-box-orient: vertical;
                color: var(--text-color);
            }
            .sidebar-section {
                margin-bottom: 2.2rem;
            }
            .sidebar-title {
                font-size: 1.5rem;
                font-weight: 800;
                margin-bottom: 0.85rem;
                margin-top: 0;
                color: var(--text-color);
                letter-spacing: -0.02em;
            }
            .sidebar-desc {
                font-size: 0.9rem;
                color: var(--text-color);
                opacity: 0.82;
                line-height: 1.6;
                margin-bottom: 0;
                font-weight: 500;
            }
            .sidebar-divider {
                height: 1px;
                background: linear-gradient(to right, transparent, rgba(148, 163, 184, 0.55), transparent);
                margin: 2rem 0;
            }
            .sidebar-stat {
                background: var(--secondary-background-color);
                border: 1px solid rgba(148, 163, 184, 0.35);
                padding: 1.2rem;
                border-radius: 0.75rem;
                box-shadow: 0 1px 3px rgba(15, 23, 42, 0.05);
                transition: all 0.3s ease;
            }
            .sidebar-stat:hover {
                border-color: rgba(148, 163, 184, 0.55);
                box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
            }
            .sidebar-stat-label {
                font-size: 0.8rem;
                color: var(--text-color);
                opacity: 0.72;
                margin-bottom: 0.5rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }
            .sidebar-stat-value {
                font-size: 2rem;
                font-weight: 800;
                color: var(--text-color);
                letter-spacing: -0.02em;
            }
            .sidebar-dev {
                font-size: 0.85rem;
                margin-bottom: 0.6rem;
            }
            .sidebar-dev-label {
                color: var(--text-color);
                opacity: 0.72;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }
            .sidebar-dev-name {
                font-weight: 700;
                color: var(--text-color);
                font-size: 1.05rem;
                margin-top: 0.4rem;
            }
            .sidebar-link {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                margin-top: 1rem;
                padding: 0.7rem 1.2rem;
                background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
                border: none;
                border-radius: 0.6rem;
                text-decoration: none;
                font-size: 0.9rem;
                font-weight: 600;
                color: #ffffff !important;
                transition: all 0.3s ease;
                box-shadow: 0 2px 8px rgba(59, 130, 246, 0.25);
            }
            .sidebar-link:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 16px rgba(59, 130, 246, 0.35);
                background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
                color: #ffffff !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
)

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
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=59b306e04c87471e61ddc1e0250e38e6&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


st.sidebar.markdown('<div class="sidebar-section"></div>', unsafe_allow_html=True)
st.sidebar.markdown('<h2 class="sidebar-title">📽️ NextWatch</h2>', unsafe_allow_html=True)
st.sidebar.markdown(
    '<p class="sidebar-desc">A content-based movie recommendation system built with machine learning to suggest similar movies.</p>',
    unsafe_allow_html=True,
)

movies = pickle.load(open('web/model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('web/model/similarity.pkl', 'rb'))

st.sidebar.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
st.sidebar.markdown(
    '<div class="sidebar-stat"><div class="sidebar-stat-label">📊 Movies in Dataset</div><div class="sidebar-stat-value">'
    + f'{len(movies):,}' +
    '</div></div>',
    unsafe_allow_html=True,
)
st.sidebar.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
st.sidebar.markdown(
    '<div class="sidebar-dev"><span class="sidebar-dev-label">👨‍💻 Developer</span></div>',
    unsafe_allow_html=True,
)
st.sidebar.markdown(
    '<div class="sidebar-dev-name">Lakitha Viraj</div>',
    unsafe_allow_html=True,
)
st.sidebar.markdown(
    '<a href="https://github.com/lakithav/content-based-movie-recommender" target="_blank" class="sidebar-link">🔗 GitHub Repository</a>',
    unsafe_allow_html=True,
)
   
st.markdown('<h1 class="app-title">NextWatch</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="app-subtitle">Find your next favorite movie in seconds.</p>',
    unsafe_allow_html=True,
)

movie_list = movies['title'].values

st.markdown('<div class="selectbox-wrapper">', unsafe_allow_html=True)
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="input-gap"></div>', unsafe_allow_html=True)

st.markdown('<div class="button-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="button-gap"></div>', unsafe_allow_html=True)
recommend_clicked = st.button(
    '🎬 Get Recommendations',
    type='secondary',
    use_container_width=True,
)
st.markdown('</div>', unsafe_allow_html=True)

if recommend_clicked:
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    st.markdown(
        f'<h3 class="section-title">Recommended for {selected_movie}</h3>',
        unsafe_allow_html=True,
    )

    columns = st.columns(5, gap="medium")
    for index, column in enumerate(columns):
        with column:
            safe_title = html.escape(recommended_movies_name[index])
            st.markdown(
                (
                    '<div class="movie-card">'
                    f'<img class="movie-card-poster" src="{recommended_movies_poster[index]}" alt="{safe_title} poster">'
                    f'<div class="movie-card-title">{safe_title}</div>'
                    '</div>'
                ),
                unsafe_allow_html=True,
            )

