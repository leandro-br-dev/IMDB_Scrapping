from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# Search for the TV series by title
results = ia.search_movie('matrix')
movie_id = results[0].movieID

# get a movie and print its director(s)
the_matrix = ia.get_movie(movie_id)
for director in the_matrix['directors']:
    print(director['name'])

# show all information that are currently available for a movie
print(sorted(the_matrix.keys()))

# show all information sets that can be fetched for a movie
print(ia.get_movie_infoset())

# update a Movie object with more information
ia.update(the_matrix, ['technical'])
# show which keys were added by the information set
print(the_matrix.infoset2keys['technical'])
# print one of the new keys
print(the_matrix.get('tech'))