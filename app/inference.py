import pandas as pd
from fastai.collab import *
from fastai.tabular.all import *
from torch import nn
from app.data import get_local_movie_recommendations_df

learn = load_learner("ml_model/movie-recommender.pkl")

def get_recommendations(user_id: int, user_matrix: list[tuple(int, int)]):
    # corresponding to userid get rating
    #calclulate cosine similarity and return top K predictions
    user_ratings_dicts = []
    for (movie_id, movie_rating) in user_matrix:
        user_ratings_dicts.append({"user": user_id, "movie": movie_id, "rating": movie_rating})
    
    movie_bias = learn.model.i_bias.weight.squeeze()
    idxs = movie_bias.argsort(descending=True)[:5]
    movie_factors = learn.model.i_weight.weight

    ratings = get_local_movie_recommendations_df()
    new_ratings = ratings.append(user_ratings_dicts, ignore_index=True)
    crosstab = pd.crosstab(new_ratings['user'], new_ratings['movie'], values=new_ratings['rating'], aggfunc='sum').fillna(0)

    other_users = crosstab.values[:-1]
    new_user = crosstab.values[-1].reshape(1, -1)
    similarities = nn.CosineSimilarity()(tensor(other_users), tensor(new_user))

    top5 = similarities.topk(5)

    user_vectors = learn.u_weight.weight[1+top5.indices,:]
    new_user_vector = user_vectors.mean(dim=0, keepdim=True)    

    user_biases = learn.u_bias.weight[1+top5.indices,:]
    new_user_bias = user_biases.mean()
    pred_ratings = torch.matmul(new_user_vector, xlearn.i_weight.weight.T) + xlearn.i_bias.weight.T + new_user_bias
    top5_ratings = pred_ratings.topk(5)

    recommendations = learn.classes['title'][top5_ratings.indices.tolist()[0]]

    return recommendations
