import io
import pandas as pd
import json
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from scipy import spatial
import numpy as np

df1 = pd.read_json('wine1.json')
df2 = pd.read_json('sim1.json')
df3 = pd.read_json('weather.json')
df4 = pd.read_json('us_wine.json')


# 많이 찾는 와인
def reco_color_reviews(color="red", n=5):
    global df1
    df3 = df1.copy()
    df4 = df3[df3['color'] == color]
    df4 = df4.sort_values('reviews', ascending=False).head(n)
    return df4.wine_id.tolist()


# print(reco_color_reviews('port'))
# print(reco_color_reviews('red', 7))
# print(reco_color_reviews('white', 7))
# print(reco_color_reviews('sparkling', 7))
# print(reco_color_reviews('rose', 7))

# 평점 높은 순


def reco_color_average(color="red", n=5):
    global df1
    df3 = df1.copy()
    df4 = df3[df3['color'] == color]
    df4 = df4.sort_values('average', ascending=False).head(n)
    return df4.wine_id.tolist()


# print(reco_color_average('port'))
# print(reco_color_average('red', 7))
# print(reco_color_average('white', 7))
# print(reco_color_average('sparkling', 7))
# print(reco_color_average('rose', 7))




def reco_likes(wine_id,n=5):
    global df1
    global df2
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
#print(reco_likes(2,10))


# 빈티지 점수 에측 기반 와인 추천
def weather(vintage=2021):
    global df3
    global df4
    grape = str(df3[vintage].idxmax())
    list1=[]
    list1.append(grape)
    list2 = []
    for i in range(520):
        if (df4['grapes'][i]) == list1:
            a = df4.loc[i,'wine_id']
            list2.append(a)
    return list2[:3]
# print(weather(2019))
# print(weather(2020))
# print(weather(2021))



