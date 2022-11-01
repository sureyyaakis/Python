#iNSERT AND DELETE ITEM IN THE LIST 

fav_movies = ["Sandlot", "Godfather", "Dune"]

print(len(fav_movies))

fav_movies.append("Iron Man")

print(len(fav_movies))

fav_movies.insert(1, "Batman")

print(fav_movies)

del(fav_movies[2])
print(fav_movies)

del(fav_movies[0])
print(fav_movies)

del(fav_movies[0])
print(fav_movies)

del(fav_movies[0])
print(fav_movies)
