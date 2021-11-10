def get_genre(genres):
    tuple_list_genres = tuple()
    for tuple_genre in range(0, len(genres)):
        tuple_list_genres += genres[tuple_genre]
    str_list_genres = str()
    for str_genres in tuple_list_genres:
        str_list_genres += f'{str_genres}, '
    genre = set(str_list_genres.split(', '))
    return genre
