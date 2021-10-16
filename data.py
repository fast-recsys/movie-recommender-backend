from typing import List
from models import Movie
import pandas as pd

df_movies = pd.read_csv('./input/links.csv')

def get_movies(count: int, random: bool) -> List[Movie]:
  
  selection = df_movies.sample(count) if random else df_movies.head(count)
  movie_ids = selection.movieId
  movie_imdb_ids = selection.imdbId
  return [
    { "movie_id": mid, "imdb_id": imdb_id }
      for (mid, imdb_id) in zip(movie_ids, movie_imdb_ids)
  ]
