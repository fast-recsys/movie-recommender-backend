# Movie Recommender Backend

[More information about the project](https://community.wandb.ai/t/creating-a-movie-recommender/190)

## Endpoints

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
