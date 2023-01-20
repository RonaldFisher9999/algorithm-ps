import json
from pprint import pprint


def movie_info(movies, genres) :
    genres_dict = dict()
    for genre in genres :
        genres_dict[genre['id']] = genre['name']
    # pprint(genres_dict)
    movies_imp_info = list()
    for movie in movies :
        movie_imp_info = {'genre_names' : [],
                          'id' : movie.get('id'),
                          'overview' : movie.get('overview'),
                          'poster_path' : movie.get('poster_path'),
                          'title' : movie.get('title'),
                          'vote_average' : movie.get('vote_average')}
        g_ids = movie.get('genre_ids')
        for id in g_ids :
            movie_imp_info['genre_names'].append(genres_dict[id])
        movies_imp_info.append(movie_imp_info)
    return movies_imp_info
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
