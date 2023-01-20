- c  
  movie.genres 인덱스 오류
  장르 분류가 b처럼 둘만 있는게 영화마다 개수가 다름
  따라서 `'genre_names' : []` 비워놓고
  따로 `g_ids`로 `genre_ids`를 받아오고 장르 id랑 비교해서
  `genre_names`에 넣어줌

  ``` python
  g_ids = movie.get('genre_ids')
  for id in g_ids :
      movie_imp_info['genre_names'].append(genres_dict[id])
  ```

  - d  
    id를 가져와서 다른 폴더의 개별 json 파일에 접근해 revnue정보를 가져온다