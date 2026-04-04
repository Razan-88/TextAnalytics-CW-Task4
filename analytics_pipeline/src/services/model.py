import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sentence_transformers import SentenceTransformer

class SentenceEmbeddingTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model_name = model_name
        self.model = SentenceTransformer(self.model_name)
        
    def fit(self, X, y=None):
        return self
        
    def transform(self, X):
        X_list = [str(text) if pd.notnull(text) else "" for text in X]
        return self.model.encode(X_list, show_progress_bar=True)