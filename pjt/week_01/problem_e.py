import json

def dec_movies(movies) :
    dec_release = list()
    for movie in movies :
        id = movie.get('id')
        info = json.load(open(f"data/movies/{id}.json", encoding='utf-8'))
        release_mon = info.get("release_date")[5:7]
        title = info.get("title")
        if release_mon == "12" :
            dec_release.append(title)
    return dec_release
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
