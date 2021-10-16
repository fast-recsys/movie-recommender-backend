# Movie Recommender Backend

[More information about the project](https://community.wandb.ai/t/creating-a-movie-recommender/190)

## Local Development

Start the server locally:

```shell
$ uvicorn main:app --reload
```

## Endpoints


### Get random movies for user to rate

```
GET /movies?shuffle=True&limit=3

Response:
{
  movies: [
    { "movie_id": 1, "movie_name": "One Flew Over the Cukoo's Next" },
    { "movie_id": 2, "movie_name": "One Flew Over the Cukoo's Next" },
    ...
    { "movie_id": 3, "movie_name": "One Flew Over the Cukoo's Next" }
  ]
}
```

### Get details of single movie

```
GET /movies/{movie_id}

Response:

{
  "imdbId": 123,
  "thumbnailUrl": "https://...",
  "genres": ["...", ".."]
}
```

### Get movie recommendations

```
POST /recommend

Sample payload:
{
  "user_ratings": [
    { "movie_id": 15, "rating": 1 },
    { "movie_id": 16, "rating": 1 },
    { "movie_id": 18, "rating": 5 },
    { "movie_id": 19, "rating": 4 },
    { "movie_id": 242, "rating": 3 }
  ]
}

```

## Todo

- Add latest movies and series not in the MovieLens25 dataset. Collect user ratings for a new user rating dataset with latest movies and series.
