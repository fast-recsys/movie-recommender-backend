# Movie Recommender Backend

[More information about the project](https://community.wandb.ai/t/creating-a-movie-recommender/190)

## Local Development

Start the server locally:

```shell
$ uvicorn app.main:app --reload
```

### Connection to database

You need to have an instance of MongoDB running. The easiest way to do this is using Docker:

```
$ docker run -p 27017:27017 mongo
```

Update the `.env` file with the connection URL:

```
MONGODB_URL="mongodb://localhost:27017"
```

### TMDB integration

To fetch URLs for movie posters, you need to get a free TMDB API key (See: https://developers.themoviedb.org/3/getting-started) and set it as the value for `TMDB_API_KEY` in the `.env` file.

See https://developers.themoviedb.org/3/configuration/get-api-configuration for more details about the `TMDB_IMAGES_BASE_URL` key.

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
