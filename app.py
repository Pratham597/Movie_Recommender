import streamlit as st 
import pickle
import requests

API_KEY = st.secrets["API_KEY"]

# Fetch the poster of the movie from TMDB API
def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id,API_KEY)
    response=requests.get(url)
    return "https://image.tmdb.org/t/p/w500/"+response.json()['poster_path']

# Recommend function to get similar movies and their posters
def recommend(movie,movies,similarity):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    similar_movies=[]
    movies_posters=[]
    for i in movie_list:
      movie_id=movies.iloc[i[0]].id
      similar_movies.append(movies.iloc[i[0]].title)
      movies_posters.append(fetch_poster(movie_id))

    return similar_movies,movies_posters


# Load the movies list and similarity matrix
movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))


# Extracting movie title from movies
movies_list=movies['title'].values
option = st.selectbox(
    'Select a movie:',
    movies_list
)


st.set_page_config(
    page_title="Movie Recommender",
    layout="wide"
)

st.markdown("""
<style>
.movie-card {
    background-color: #1e1e1e;
    padding: 12px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    transition: transform 0.3s;
}
.movie-card:hover {
    transform: scale(1.05);
}
.movie-title {
    font-size: 16px;
    font-weight: 600;
    margin-top: 10px;
    color: white;
}
</style>
""", unsafe_allow_html=True)


st.markdown("<h1 style='text-align:center;'>Movie Recommender System</h1>", unsafe_allow_html=True)

st.markdown(f"""
<p style='text-align:center; font-size:18px;'>
You selected: <b>{option}</b>
</p>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns([3,1,3])
with col2:
    recommend_clicked = st.button("Recommend",use_container_width=True)

if recommend_clicked:
    st.markdown("---")
    st.subheader("Recommended Movies")

    similar_movies, movies_posters = recommend(option, movies, similarity)

    cols = st.columns(5) 

    for idx, (movie, poster) in enumerate(zip(similar_movies, movies_posters)):
        with cols[idx % 5]:
            st.markdown(
                f"""
                <div class="movie-card">
                    <img src="{poster}" style="width:100%; border-radius:12px;">
                    <div class="movie-title">{movie}</div>
                </div>
                """,
                unsafe_allow_html=True
            )




