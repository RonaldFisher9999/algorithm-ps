# from pprint import pprint
import json


def max_revenue(movies) :
    max_rev = 0
    max_rev_title = ""
    for movie in movies :
        id = movie.get('id')
        info = json.load(open(f"data/movies/{id}.json", encoding='utf-8'))
        rev = info.get("revenue")
        title = info.get("title")
        if max_rev < rev :
            max_rev = rev
            max_rev_title = title
    return max_rev_title
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
