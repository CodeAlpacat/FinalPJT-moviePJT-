![image](https://user-images.githubusercontent.com/97648026/170070287-cbed1e07-d24c-4a2b-811e-7c784283b2e5.png)

----

![image](https://user-images.githubusercontent.com/90893428/170520482-514b79de-db75-43df-9db4-147bbb0eafc8.png)



----



# 🌳#1 Get Started

> 서버 설치 및 실행

```bash
$ git clone (repo주소)
---- 하위 폴더 이동
$ python -m venv venv (가상 환경 생성)
$ source venv/Scripts/activate (해당 터미널 삭제 및 다시 생성으로 대체 가능)
$ pip install -r requirements (장고 및 설치패키지)

$ python manage.py migrate (데이터베이스에 모델 반영)
$ python manage.py loaddata movies/genre.json movies/movie_data.json(데이터 불러오기)

$ python manage.py runserver (서버 실행)
```



#  🌳#2 개요

### 🌱#2-1 Vue

```
함무바라~
│
├── README.md
├── dist
├── node_modules
├── public
│   ├── favicon.io
│   └── index.html
├── src
│   ├── api
|	|	└── drf.js
│   ├── assets
|	|	├── logo.png
|	|	└── logo.svg
|	├── components
|	|	├── AccountsErrorList.vue
|	|	├── ArticleForm.vue
|	|	├── ArticleView.vue
|	|	├── CardMovieViewItem.vue
|	|	├── CardMovieViewItemVueper.vue
|	|	├── CardView.vue
|	|	├── CardViewItem.vue
|	|	├── CommentView.vue
|	|	├── DescriptionDetail.vue
|	|	├── DetailDialog.vue
|	|	├── GenreBasedRecommendation.vue
|	|	├── GenreBasedRecommendationsCard.vue
|	|	├── MovieTrailer.vue
|	|	├── OverviewDetail.vue
|	|	├── ReviewDetail.vue
|	|	├── ReviewView.vue
|	|	├── UserLikedArticles.vue
|	|	└── UserPostedArticles.vue
|	├── plugins
|   │	└── vuetify.js
|   ├── router
|   |	└── index.js
|   ├── sass
|   |	└── variables.scss
|   ├── styles
|   |	└── generic
|	|		└── _reset.scss
|	├── views
|	|	├── ArticleDetailView.vue
|	|	├── ArticleEditView.vue
|	|	├── ArticleNewView.vue
|	|	├── CommunityView.vue
|	|	├── HomeView.vue
|	|	├── LoginView.vue
|	|	├── LoginView.vue
|	|	├── LogoutView.vue
|	|	├── MovieView.vue
|	|	├── NotFound404.vue
|	|	├── ProfileCommunityView.vue
|	|	├── ProfileEditFormView.vue
|	|	├── ProfileView.vue
|	|	├── SignupView.vue
|	|	└── StartView.vue
│   ├── App.vue
|	└── main.js
├── .gitignore
├── babel.config.js
├── jsconfig.json
├── package.json
└── vue.config.js
```



### 🌱#2-2 Template & Components

![캡처](https://user-images.githubusercontent.com/90893428/170507617-8740e5dc-5ba2-4bda-9257-498553388611.PNG)



### 🌱#2-3 E-R Diagram

![erd](https://user-images.githubusercontent.com/90893428/170515249-12688140-9d3d-481d-aed5-96cf4c0be061.PNG)



### 🌱#2-4 목표

- DB relation 및 UI 구조 세부 설계 및 기능 구체화

- 유저가 직접 선택한 장르들을 기반으로 적절한 영화 추천 알고리즘 구현
- 백로그(MeetingLog) 작성 및 빠르고 짧은 시간의 스프린트로 기능 단위 구현 후 피드백
- 백엔드와 프론트엔드 지식 습득을 위한 기능 단위 교차 역할 배분
- 외부 라이브러리 및 CSS 애니메이션 속성을 이용한 반응형 & 현대적인 인터렉티브 웹 어플리케이션 제작
- 사용자 경험 극대화를 위한 DB 관계 설계
- 디버깅 실력 향상을 위한 컴포넌트 병합 테스트

​	

### 🌱#2-5 팀원 및 업무 분담 내역

| <img src="https://user-images.githubusercontent.com/90893428/170524805-d72feec8-a6c8-43be-800d-f94e7b3bba3e.png" width="300" height="300"/> | <img src="https://user-images.githubusercontent.com/90893428/170525087-c94938ed-2474-4ecb-b887-db413ce39e8b.png" width="250" height="250"/> |
| :----------------------------------------------------------- | :----------------------------------------------------------: |
| **프론트엔드** 카드 등 컴포넌트 제작 및 & 인증 페이지 / 세부 기능 구현 |        ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ        |
| **백엔드** 추천 & 더보기 기능 등 세부 DB 구현 및 API 설계    |                                                              |

# 🌳#3 핵심 기능 & 디자인



# 🌳#4 느낀 점

