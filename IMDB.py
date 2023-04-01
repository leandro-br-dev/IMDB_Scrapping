import imdb

# Create an instance of the IMDb class
ia = imdb.IMDb()

# Search for the movie by title
results = ia.search_movie('The Shawshank Redemption')

# Get the movie ID for the first result
movie_id = results[0].movieID

# Get the movie details using the ID
movie = ia.get_movie(movie_id)

# Print the movie title and rating
print(movie['title'])
print(movie['rating'])
