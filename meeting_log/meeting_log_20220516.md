# 1. Meeting Log

### #ERD Based Model.py 작성

* 220511 작성된 ERD를 기준으로 Model.py를 작성하였다.
* 작성하는 과정 중, 불필요한 Diagram Node 들을 ManyToMany 관계로 정리하여 간략화 하였다.

![Prototype01-수정1 drawio](https://user-images.githubusercontent.com/97648026/168594834-9730da6c-9779-4014-a95a-5fb9acdc85d4.png)



### # Serializers를 이용한 요청확인

* 작성된 모델에 `django_seed`를 이용하여 더미 데이터를 추가

* 작성된 모델을 바탕으로 serializer 생성, api요청을 통한 Json 'GET' 확인

**GET MovieList**

![image](https://user-images.githubusercontent.com/97648026/168596194-945d3308-86bb-49c3-8212-8abc8f0d739a.png)

**GET Movie**

![image](https://user-images.githubusercontent.com/97648026/168596095-4a64a3e1-fe07-4372-9c8d-a0046b51c839.png)



### # Movie 정보 요청 및 DB 데이터 생성

* TMDB API를 이용하여, 추천 영화 페이지 1~300까지 요청한다.
* 요청되어 받은 JSON을 통하여 필요한 정보를 필터링하여 DB에 저장한다.
* Detail을 통하여 얻어지는 추가 정보들은 필요할 때 axios를 통해 api 요청을 하거나, DB 저장시 필요한 정보를 추가 요청하여 확보한다.





### # 향후 과제

* Vue 생성후, 프로젝트 폴더 구성 그래프 작성하기

