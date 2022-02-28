from functools import lru_cache
from typing import Any, List, Optional
from fastapi import Depends, HTTPException, status
import pandas as pd
import httpx

from app.config import Settings, get_settings

from app.models.movie import MovieBase, MoviePublic


@lru_cache
def get_movie_df() -> Any:
    # TODO: Use calculated current path
    df_movies = pd.read_csv("./app/input/links.csv")
    return df_movies


@lru_cache
def get_local_movie_df() -> Any:
    # TODO: Use calculated current path
    df = pd.read_csv("./app/input/movies.csv")
    return df


def get_tmdb_id(id: int, df_movies=Depends(get_movie_df)) -> int:
    movie_row = df_movies.loc[df_movies["movieId"] == id]
    if movie_row.empty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    tmdbId = int(movie_row["tmdbId"])
    return tmdbId

@lru_cache
def get_local_movie_recommendations_df() -> Any:
    df = pd.read_csv("./app/input/ratings.csv")
    return df


async def get_movie_details_from_tmdb(
    tmdb_id: int = Depends(get_tmdb_id), settings: Settings = Depends(get_settings)
) -> MoviePublic:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            settings.tmdb_base_url + f"/movie/{tmdb_id}?api_key={settings.tmdb_api_key}"
        )
        response_json = response.json()
        return MoviePublic(
            id=tmdb_id,
            title=response_json["original_title"],
            thumbnail_url=f"{settings.tmdb_images_base_url}{response_json['poster_path']}",
        )

async def get_movie_details(
    id: int,
    movie: MoviePublic = Depends(get_movie_details_from_tmdb)
) -> MoviePublic:
    # Replace tmdbId with dataset ID
    movie.id = id

    return movie


async def get_unrated_movie_details(
    movies_rated: List[int], df_movies=get_movie_df() # TODO: use DI here!
) -> List[MoviePublic]:

    unrated_df = df_movies[~df_movies["movieId"].isin(movies_rated)]

    unrated_df = unrated_df.sample(3)

    unrated_movie_ids = list(unrated_df["movieId"])

    # FIXME: this doesn't work anymore - get_movie_details signature has changed
    return [await get_movie_details(id, df_movies) for id in unrated_movie_ids]


def get_local_movie_details(id: int) -> MovieBase:
    df = get_local_movie_df()
    df = df.loc[df["movieId"] == id]
    return MovieBase(id=df.values[0][0], title=df.values[0][1])
