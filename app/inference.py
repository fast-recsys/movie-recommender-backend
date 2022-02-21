from fastai.collab import *
from fastai.tabular.all import *
from torch import nn
# from app.models.user_movies import Use

learn = load_learner("ml_model/movie-recommender-nn.pkl")

def get_recommendations(user_id):
    # corresponding to userid get rating
    
    #calclulate cosine similarity and return top K predictions
    pass
