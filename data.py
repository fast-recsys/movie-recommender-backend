from typing import List, Optional
from fastapi import Depends
import pandas as pd
import httpx

from config import Settings, get_settings

from models.movie import MoviePublic


def get_movie_df():
    df_movies = pd.read_csv('./input/links.csv')
    return df_movies

async def get_movie_details_from_tmdb(
    tmdbId: int,
    settings: Settings = Depends(get_settings)
) -> Optional[MoviePublic]:
    print(settings)
    async with httpx.AsyncClient() as client:
        response = await client.get(settings.tmdb_base_url + f"/movie/{tmdbId}?api_key={settings.tmdb_api_key}")
        response_json = response.json()
        return MoviePublic(id=tmdbId, title=response_json['original_title'], thumbnail_url=f"{settings.tmdb_images_base_url}{response_json['poster_path']}")



async def get_movie_details(
    id: int,
    df_movies=Depends(get_movie_df)
) -> Optional[MoviePublic]:

    movie_row = df_movies.loc[df_movies["movieId"] == id]
    if movie_row.empty:
        return None

    tmdbId = int(movie_row["tmdbId"])
    movie = await get_movie_details_from_tmdb(tmdbId=tmdbId, settings=get_settings())

    # Replace tmdbId with dataset ID
    if movie is not None:
        movie.id = id

    return movie


async def get_unrated_movies(movies_rated: List[int]) -> List[MoviePublic]:
    return []
