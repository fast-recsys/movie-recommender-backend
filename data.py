from typing import List
from models import Movie
import pandas as pd

df_movies = pd.read_csv('./input/movies.csv')

def get_movies(count: int, random: bool) -> List[Movie]:
  
  selection = df_movies.sample(count) if random else df_movies.head(count)
  movie_ids = selection.movieId
  movie_titles = selection.title
  return [
    { "movie_id": mid, "name": title }
      for (mid, title) in zip(movie_ids, movie_titles)
  ]
