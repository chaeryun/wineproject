import io
import pandas as pd
import json
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from scipy import spatial
import numpy as np
'''
df1 = pd.read_json('wine1.json')
df2 = pd.read_json('sim1.json')
df3 = pd.read_json('weather.json')
df4 = pd.read_json('us_wine.json')
'''

# 많이 찾는 와인
def reco_color_reviews(color="red", n=5):
    df1 = pd.read_json('./reco/wine1.json')
    df3 = df1.copy()
    df4 = df3[df3['color'] == color]
    df4 = df4.sort_values('reviews', ascending=False).head(n)
    return df4.wine_id.tolist()

# 평점 높은 순
def reco_color_average(color="red", n=5):
    df1 = pd.read_json('./reco/wine1.json')
    df3 = df1.copy()
    df4 = df3[df3['color'] == color]
    df4 = df4.sort_values('average', ascending=False).head(n)
    return df4.wine_id.tolist()

def reco_likes(wine_id,n=5):
    df1 = pd.read_json('./reco/wine1.json')
    df2 = pd.read_json('./reco/sim1.json')
    df1 = df1.copy()
    df2 = df2.copy()
    df2.pop('wine')
    df2.pop('color')
    df2.set_index("id", inplace=True)
    df2_cosine = cosine_similarity(df2, df2)
    df2_similarity = pd.DataFrame(df2_cosine)
    for i in range(len(df2_similarity)):
        df2_similarity.iloc[i][i] = 0
    result = df2_similarity[df1['wine_id'][wine_id]].sort_values(ascending=False)[:n]
    array = np.array(result.index.values)
    return list(array)

# 빈티지 점수 에측 기반 와인 추천
def weather(vintage=2021):
    df3 = pd.read_json('./reco/weather.json')
    df4 = pd.read_json('./reco/us_wine.json')
    grape = str(df3[vintage].idxmax())
    list1=[]
    list1.append(grape)
    list2 = []
    for i in range(520):
        if (df4['grapes'][i]) == list1:
            a = df4.loc[i,'wine_id']
            list2.append(a)
    if vintage == 2019:
        return list2[4:7]
    else:
        return list2[:3]