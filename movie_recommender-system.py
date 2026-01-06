import pandas as pd
import numpy as np
import ast
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load datasets
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merge dataframes
df = movies.merge(credits, on="title")

# Select relevant columns
df = df[["id", "popularity", "title", "overview", "genres", "keywords", "cast", "crew"]]

# Data cleaning
df.dropna(inplace=True)

# Helper functions for data transformation
def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i["name"])
    return L

def convertCast(obj):
    L = []
    ct = 0
    for i in ast.literal_eval(obj):
        if ct != 3:
            L.append(i["name"])
            ct += 1
        else:
            break
    return L

def convertCrew(obj):
    L = []
    for i in ast.literal_eval(obj):
        if i["job"] == "Director":
            L.append(i["name"])
    return L

# Apply transformations
df["genres"] = df["genres"].apply(convert)
df["keywords"] = df["keywords"].apply(convert)
df["cast"] = df["cast"].apply(convertCast)
df["crew"] = df["crew"].apply(convertCrew)
df["overview"] = df["overview"].apply(lambda x: x.split())

# Remove spaces from names to avoid ambiguity
df["genres"] = df["genres"].apply(lambda x: [i.replace(" ", "") for i in x])
df["cast"] = df["cast"].apply(lambda x: [i.replace(" ", "") for i in x])
df["keywords"] = df["keywords"].apply(lambda x: [i.replace(" ", "") for i in x])
df["crew"] = df["crew"].apply(lambda x: [i.replace(" ", "") for i in x])


# Create tags column
df["tags"] = df["overview"] + df["genres"] + df["keywords"] + df["cast"] + df["crew"]

# Create new dataframe with essential columns
new_df = df[["id", "title", "tags"]]

# Process tags column
new_df["tags"] = new_df["tags"].apply(lambda x: " ".join(x))
new_df["tags"] = new_df["tags"].apply(lambda x: x.lower())

# Stemming
ps = PorterStemmer()
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

new_df["tags"] = new_df["tags"].apply(stem)

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(new_df["tags"]).toarray()

# Calculate cosine similarity
similarity = cosine_similarity(vectors)

# Recommendation function
def recommend(movie):
    try:
        movie_index = new_df[new_df["title"] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        print(f"Recommendations for {movie}:")
        for i in movies_list:
            print(new_df.iloc[i[0]].title)
    except IndexError:
        print(f"Movie '{movie}' not found in the dataset.")

# Example usage
recommend("Batman Begins")

# Save the processed dataframe and similarity matrix
pickle.dump(new_df.to_dict(), open("movies_dict.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

print("\nPickle files 'movies_dict.pkl' and 'similarity.pkl' have been created.")