import io
import pandas as pd
import numpy as np
import json
from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import cosine_similarity
import math
from numpy import dot 
from numpy.linalg import norm 
import numpy as np

#pip install scikit-learn
#pip install scipy

df = pd.read_json('./reco/wine_final.json')
df2 = pd.read_json('./reco/cos.json')

# 평점 높은 와인 추천
def reco_color_average(color= "red", n=5):
    df1 = df.copy()
    df1[df1['color'] == '${color}}']
    df1 = df1.sort_values(by="average", ascending=False).groupby("color").head(n)
    df2 = df1.sort_values(by=["color", "average"], ascending=[True, False])
    return df2.wine_id.tolist()
#print(reco_color_average('port',10))
# reco_color_average('red',10)
# reco_color_average('white',10)
# reco_color_average('',10)
# reco_color_average('white',10)



# 사람들이 많이 찾았던 와인
def reco_color_reviews(color= "red", n=5):
    df1 = df.copy()
    df1[df1['color'] == '${color}}']
    df1 = df1.sort_values(by="reviews", ascending=False).groupby("color").head(n)
    df2 = df1.sort_values(by=["color", "reviews"], ascending=[True, False])
    return df2.wine_id.tolist()
#print(reco_color_reviews('rose',5))



# 찜 기반 추천 와인
def reco_likes(wine_id,n=5):
    df2.set_index('wine_id', inplace=True)
    df2_cosine = cosine_similarity(df2, df2)
    df2_similarity = pd.DataFrame(df2_cosine)
    for i in range(len(df2_similarity)):
        df2_similarity.iloc[i][i] = 0
    result = df2_similarity[df['wine_id'][wine_id]].sort_values(ascending=False)[:n]
    array = np.array(result.index.values)
    return list(array)
#print(reco_likes(42,10))


