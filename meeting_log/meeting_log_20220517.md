# 1. Meeting Log

### #ERD 수정

* 기획서에 명시된 대로, community의 기능을 추가하기 위하여 ERD 수정 작업에 들어갔다.
  * 주요 수정 작업
    * 영화와 commnunity의 분리 ( 영화 리뷰 작성 페이지를 새로 생성, 기존 Detail에서 리뷰 제거)




## #Model에 데이터값 받아오기

* 최초 DB에 저장할 값을 받아오기 위해, api 요청으로 JSON파일을 받아왔다.
* 받아온 JSON data를 loaddata를 통해 movies 및 genre 필드에 대해 적용을 시켰다.



**과정 중 어려웠던 점**

* loaddata중, model을 지정문제
  * 'movie.genre'로 이어주려 하였으나, 앞에서 지칭하는 movie가 클래스명이 아니라, app_name이라 'moives.genre'로 이어주어야 작동하였다.
* Foreinkey constraint failed
  * movie data를 loaddata를 하였으나, 위와 같은 에러가 발생하여 적용되지 않았다. 확인해 본 결과, 참조하는 genre에 data가 없어, 적용되지 않았다.
  * genre관련된 data를 입력해주어 해결하였다.



### # Model 변경

* CRUD community를 따로 생성함과 동시에, Detail에서 표시되는 영화에 대한 리뷰는 다른 모델을 생성하여 관리하는 것으로 결정하였다. 따라서 와이어 프레임 Detail페이지에서 변경사항은 X, Community페이지를 새로 생성하게 되었다. 



### # 와이어프레임 변경사항

* 메인 페이지에서 영화 추천 목록 송출



### # 영화 리스트 가져오기

**현재 상영 영화 리스트 가져오기**

* 현재 상영 리스트를 api 요청 후, 개봉일 기준
* 개봉 날짜를 문자열로 슬라이싱해 현재 날짜를 datetime 값을 이용해 비교
  * 최소 개봉 2주 이내의 영화를 리스트에 추가
  * 14일 이전일 경우 이전 달까지 계산
  * ex) 현재 5월 1일 일 경우 4월 16일 이후 개봉한 영화부터 리스트에 추가

* 해당하는 영화 중에 10개의 영화 가져오기

- 영화가 10개가 되지 않는 경우 처리하기

**개봉 예정 영화 리스트 가져오기**

* 전체 영화 정보 중에 현재 날짜 이후에 출시하는 영화 리스트 출력
  * datetime으로 받아온 날짜의 이후 날짜를 슬라이싱해서 조건에 맞는 객체 리스트에 추가

* 해당하는 영화 중 10개의 영화 가져오기
* 영화가 10개가 되지 않는 경우 처리하기



### 영화 추천 알고리즘 설계

* 사용자가 가입할 때 관심있는 선호하는 장르를 여러 개 선택할 수 있음.
* 영화들 중에 사용자가 선호하는 장르 종류가 많이 해당되면 우선 순위가 높아져 가장 앞에 출력



### 영화 추천 알고리즘



```python
user_likes_genre = [28, 37, 80] # 유저가 좋아하는 장르 id 값

    total_range = 0 # range 변수

    for movie in serializer.data:
        genres = movie['genres'] # 영화가 보유한 장르 리스트

        count = 1 # 확률 가중치

        for genre in genres: # 영화 보유 장르에 대해
            if genre in user_likes_genre: # 유저가 좋아하는 장르 id 값이 일치할때마다 4배 적용
                count = count << 4 # 0개 일치: 1 1개 일치: 16 2개 일치: 256 3개 일치: 4096

        lottery_list.append((total_range, total_range + count - 1, movie)) # total range 값, movie 튜플로 append
        total_range += count # total_range값 증가
```

* 영화가 보유한 장르 리스트와 유저가 좋아하는 장르리스트를 비교하여, 일치하는 갯수를 파악한다.
* 일치하는 갯수에 따라, 가중치를 적용하여 범위를 설정후 append를 한다.
  * 각 범위는 movie가 가지는 범위가 된다.
* totoal_range는 가중치가 누적되어 형성된 전체 범위가 된다.



```python
for _ in range(20): # 숫자 추첨 20번
        number_list.append(randint(0, total_range - 1))
    
    lot_len = len(lottery_list) # 추첨 항목 크기
    
    
    for number in number_list: # 추첨 번호 소속 범위 탐색
        middle = (lot_len - 1) // 2 # 이진 탐색 middle 값
        left = 0 # 좌
        right = lot_len - 1 # 우
        while True: 
            if lottery_list[middle][0] > number: # 최소값보다 작으면, right, middle값 갱신
                right = middle - 1
                middle = (right + left) // 2
                continue
            elif lottery_list[middle][1] < number: # 최대값보다 크면, left, middle값 갱신
                left = middle + 1
                middle = (right + left) // 2
                continue
            else: # 범위 만족시 while문 탈출
                break
        # 중복 체크
        if not lottery_list[middle][2]['id'] in recommend_check:
            recommend_list.append(lottery_list[middle][2]) # 찾은 movie append
            recommend_check.append(lottery_list[middle][2]['id'])
```

* 0부터 total_range 까지의 범위의 숫자를 20번 뽑아, number_list에 append한다.
* 이진 탐색을  통해 숫자가 가리키는 movie 범위를 찾는다.
* 이후, 중복 체크를 하여 이미 들어있는 movie id값이 recommend_check 안에 없을 경우, recommend_list에 movie를, recommend_check에 movie id값을 append한다.

 ```python
     if len(recommend_list) > 10:
         return Response(recommend_list[:10])
     return Response(recommend_list)
 ```

* 추천 리스트 길이가 10개 초과일 경우, 슬라이싱하여 10개로, 이하일 경우, 리스트를 그대로 반환한다.





### # 향후 과제

* account 관련 serializer 작성하기, 각 serializer 정상 작동 여부 확인하기

