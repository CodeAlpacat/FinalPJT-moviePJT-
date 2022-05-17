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



**개봉 예정 영화 리스트 가져오기**

* Upcoming 영화 리스트를 api 요청 후, 현재 시각 기준 이후에 개봉 예정인 영화리스트 만을 받아왔다.



**추천 영화 리스트 가져오기**

* 



### # 향후 과제

* Vue 생성후, 프로젝트 폴더 구성 그래프 작성하기
