# Movie Recommender Backend

[More information about the project](https://community.wandb.ai/t/creating-a-movie-recommender/190)

## Local Development

Start the server locally:

```shell
$ uvicorn main:app --reload
```

## Endpoints

### Create a user

```
POST /users

Response:
{
  id: 123
}
```

The ID returned by the endpoint can be used for user-specific operations, e.g. rating new movies and generating recommendations.

### Get movies not rated by a user

```
GET /users/{id}/unrated

Response:
{
  movies: [
    { "id": 1, "title": "Movie 1", thumbnail_url: "...", genres: ["..."] },
    { "id": 2, "title": "Movie 2", thumbnail_url: "...", genres: ["..."] },
    { "id": 3, "title": "Movie 3", thumbnail_url: "...", genres: ["..."] }
  ]
}
```

The endpoint returns 3 movies not rated by the user at a time. Each time the endpoint is hit, a different set of movies is returned (i.e. the movies are shuffled).

### Get details of single movie

```
GET /movies/{id}

Response:
{
  "id": 123,
  "title": "Movie title",
  "thumbnailUrl": "https://...",
  "genres": ["...", ".."]
}
```

### Store user movie ratings

```
POST /users/{id}/ratings

Payload:
{
  ratings: [
    { "movie_id": 1, "rating": 4 },
    { "movie_id": 2, "rating": 1 },
    { "movie_id": 3, "rating": 5 }
  ]
}
```

### Get user movie ratings

```
GET /users/{id}/ratings

Response:
{
  ratings: [
    { "movie_id": 1, "rating": 4 },
    { "movie_id": 2, "rating": 1 },
    { "movie_id": 3, "rating": 5 }
  ]
}
```

### Get movie recommendations for a user

```
GET /users/{id}/recommendations?top=3

Response:
{
  recommendations: [
    { "movie_id": 1, "movie_name": "Movie 1", "match": 0.987 },
    { "movie_id": 2, "movie_name": "Movie 2", "match": 0.727 },
    { "movie_id": 3, "movie_name": "Movie 3", "match": 0.589 },
  ]
}
```

The endpoint returns 3 recommendations by default unless an explicit number is specified using the `top` query parameter.

## Todo

- Add latest movies and series not in the MovieLens25 dataset. Collect user ratings for a new user rating dataset with latest movies and series.
