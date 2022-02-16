from functools import lru_cache
from typing import Any, List, Optional
from fastapi import Depends
import pandas as pd
import httpx

from config import Settings, get_settings

from models.movie import MovieBase, MoviePublic


@lru_cache
def get_movie_df() -> Any:
    df_movies = pd.read_csv("./input/links.csv")
    return df_movies


@lru_cache
def get_local_movie_df() -> Any:
    df = pd.read_csv("./input/movies.csv")
    return df


async def get_movie_details_from_tmdb(
    tmdbId: int, settings: Settings = Depends(get_settings)
) -> MoviePublic:
    print(settings)
    async with httpx.AsyncClient() as client:
        response = await client.get(
            settings.tmdb_base_url + f"/movie/{tmdbId}?api_key={settings.tmdb_api_key}"
        )
        response_json = response.json()
        return MoviePublic(
            id=tmdbId,
            title=response_json["original_title"],
            thumbnail_url=f"{settings.tmdb_images_base_url}{response_json['poster_path']}",
        )


async def get_movie_details(id: int, df_movies=Depends(get_movie_df)) -> MoviePublic:

    movie_row = df_movies.loc[df_movies["movieId"] == id]
    tmdbId = int(movie_row["tmdbId"])
    movie = await get_movie_details_from_tmdb(tmdbId=tmdbId, settings=get_settings())

    # Replace tmdbId with dataset ID
    movie.id = id

    return movie


async def get_unrated_movie_details(
    movies_rated: List[int], df_movies=get_movie_df()
) -> List[MoviePublic]:

    unrated_df = df_movies[~df_movies["movieId"].isin(movies_rated)]

    unrated_df = unrated_df.sample(3)

    unrated_movie_ids = list(unrated_df["movieId"])

    return [await get_movie_details(id, df_movies) for id in unrated_movie_ids]


def get_local_movie_details(id: int) -> MovieBase:
    df = get_local_movie_df()
    df = df.loc[df["movieId"] == id]
    return MovieBase(id=df.values[0][0], title=df.values[0][1])
