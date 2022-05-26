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

- 사용자 경험 최적화를 위한 DB relation 및 UI 구조 세부 설계 및 기능 구체화
- 유저가 직접 선택한 장르들을 기반으로 적절한 영화 추천 알고리즘 구현
- 백로그(MeetingLog) 작성 및 빠르고 짧은 시간의 스프린트로 기능 단위 구현 후 피드백
- 백엔드와 프론트엔드 지식 습득을 위한 기능 단위 교차 역할 배분
- 외부 라이브러리 및 CSS 애니메이션 속성을 이용한 반응형 & 현대적인 인터렉티브 웹 어플리케이션 제작
- 디버깅 실력 향상을 위한 컴포넌트 병합 테스트



### 🌱#2-5 팀원 및 업무 분담 내역

| <img src="https://user-images.githubusercontent.com/90893428/170524805-d72feec8-a6c8-43be-800d-f94e7b3bba3e.png" width="300" height="300"/> | <img src="https://user-images.githubusercontent.com/90893428/170525087-c94938ed-2474-4ecb-b887-db413ce39e8b.png" width="250" height="250"/> |
| :----------------------------------------------------------- | :----------------------------------------------------------: |
| **프론트엔드** 카드 등 컴포넌트 제작 및 & 인증 페이지 / 세부 기능 구현 | **프론트 엔드** 메인 페이지 배경 영상, 커뮤니티 페이지, 모달 관련 세부 기능 구현 |
| **백엔드** 추천 & 더보기 기능 등 세부 DB 구현 및 API 설계    |   **백엔드** 추천 알고리즘 설계 및 날짜 표현 알고리즘 설계   |

# 🌳#3 핵심 기능 & 디자인



### 🌱#3 시작(팀명)

![ezgif com-gif-maker (5)](https://user-images.githubusercontent.com/97648026/170549375-e5ecf053-d593-41ce-b473-6537fa140df8.gif)

- 시작페이지에는 영화 페이지를 제작한 팀명의 애니메이션이 출력되고 메인페이지로 자동으로 이동합니다.

### 🌱#3-0 홈

![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/97648026/170546790-1902f63d-016b-4577-9023-1437b32f1ce1.gif)

![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/97648026/170546815-a594819e-6902-43e8-86c9-23b657b27f59.gif)

- 사용자가 회원가입시에 선택한 장르들을 기반으로 해당 장르들을 다수 포함한 영화를 추천하는 카드뷰를 보여줍니다.
- 3가지의 장르가 포함된 영화가 띄워질 가능성이 가장 높고, 해당하는 장르의 수에 기반해 순차적으로 나올 확률이 감소합니다.
- 현재 상영중인 영화 및 개봉 예정작들을 보여줍니다.
- 카드는 반응형으로 사용자의 화면 크기에 맞게 카드의 노출 갯수가 바뀝니다.
- 기본적으로 화면의 배경에는 명작 영화의 하이라이트 영상이 재생됩니다. 멈추고 싶을 시에 우측 상단 빈 공간을 클릭해 시청을 중단할 수 있습니다.

### 🌱#3-1 전체 영화

![ezgif com-gif-maker (7)](https://user-images.githubusercontent.com/97648026/170550913-c9c1a35a-60ad-4bb9-8684-b5880aa297b7.gif)

- 화면에는 10개 씩 영화가 노출되며, 더보기 버튼을 통해 영화를 추가로 조회할 수 있습니다.

- 각 카드는 등장할 때 플립 효과를 가집니다.

- 카드는 반응형으로 사용자의 화면 크기에 맞게 카드의 노출 갯수가 바뀝니다.

### 🌱#3-2 영화 검색 기능

![서치바](https://user-images.githubusercontent.com/90893428/170536900-de6aec9a-2948-453e-bf3d-b384cfea905a.PNG)

- 원하는 영화 정보를 얻기위해 검색을 통해 영화를 조회할 수 있습니다.
- 전체 영화에서 검색바와 연동되어 실시간으로 요청을 처리합니다.



### 🌱#3-3 게시글 작성

<img src="https://user-images.githubusercontent.com/90893428/170536897-81bba433-3400-4034-8e18-292c5088404c.PNG"/>

- 영화에 대한 자유로운 대화를 나누는 게시판입니다. 게시글 작성 및 페이지네이션을 구현했으며, 작성 날짜가 현재 기준으로 갱신됩니다. 
- 작성자를 클릭해 해당 유저의 프로필을 조회할 수 있습니다.



### 🌱#3-4 게시글 작성

<img src="https://user-images.githubusercontent.com/90893428/170536894-02ba3b4a-16a4-4567-b564-4ac036748745.PNG"/>

- 게시글의 제목 및 내용을 작성해 유저 및 게시글을 DB에 저장합니다.
- 작성한 게시글은 게시판에 즉각 반영되며 사용자만 수정 및 삭제가 가능합니다.



### 🌱#3-5 게시글 상세 및 댓글 작성

<img src="https://user-images.githubusercontent.com/90893428/170536899-281822b2-8771-4151-ad55-585eaa31051f.PNG"/>

- 댓글 작성 및 삭제를 할 수 있도록 구현했습니다.
- 개별 게시글의 좋아요를 누를 수 있으며, 좋아요를 누른 게시글은 개인 프로필 페이지에 보관됩니다.
- 우측 상단의 버튼을 통해 게시글을 삭제 및 수정할 수 있습니다.



### 🌱#3-6 로그인

<img src="https://user-images.githubusercontent.com/90893428/170536892-4676aad9-6e48-4e26-9d6e-87cd0f69aab7.PNG"/>

- 로그인 페이지 구현



### 🌱#3-7 회원가입

<img src="https://user-images.githubusercontent.com/90893428/170536883-dd2d04f0-a765-4f91-a38d-315b44a475a4.PNG"/>

- 회원가입 페이지입니다.
- 장르를 최대 3개 선택이 가능하며, 3개 이상 선택시에 경고창을 띄웁니다.
- 프로필 사진을 업로드 할 수 있습니다.



### 🌱#3-8 회원정보 수정

<img src="https://user-images.githubusercontent.com/90893428/170543039-f7a388ea-f901-4c03-b06d-2aebb29f7b78.PNG"/>

- 기존 정보가 기입된 회원정보 수정 페이지입니다.
- 프로필 사진 및 장르는 재업로드를 요구합니다.



### 🌱#3-9 프로필

<img src="https://user-images.githubusercontent.com/90893428/170536931-a570c4e4-8254-4864-b4a6-b031088cbcd5.PNG"/>

- 사용자 및 타인의 개인 프로필 페이지입니다.
- 사용자는 타인의 프로필을 팔로우 및 언팔로우할 수 있으며, 만약 스스로의 프로필일 경우 회원정보 수정 버튼이 활성화 됩니다.
- 아래에는 사용자가 리스트에 담아둔 영화의 목록이 표시됩니다.

<img src="https://user-images.githubusercontent.com/90893428/170536890-84602006-9e51-444b-97ca-c5007935c5de.PNG"/>

- 위와 같이 작성한 게시글 및 좋아요를 누른 게시글을 가져올 수 있으며, 클릭 시 해당 게시물로 연결된 버튼을 활성화합니다.



### 🌱#3-10 영화 세부 정보

![다이얼로그](https://user-images.githubusercontent.com/90893428/170536940-803c8125-46d0-4fd0-a092-67f7f6ba26b7.PNG)

- 영화의 세부 정보 및 유튜브 영상이 포함된 다이얼로그입니다.
- 유튜브로 영화 트레일러를 시청할 수 있으며, 프로필에 나의 영화 리스트에 추가할 수 있습니다.



### 🌱#3-11 관련 영화 추천

![연관 영화](https://user-images.githubusercontent.com/90893428/170536959-836cde3d-7a4f-41b7-b2a5-6e0c223b9706.PNG)

- 위와 같이 RELATED MOVIE에는 해당 영화와 연관된 추천 영화를 띄워줍니다. 사용자는 현재 영화와 관련된 영화를 즐길 수 있습니다.



### 🌱#3-12 리뷰 작성 & 삭제 및 추천 댓글

![리뷰 추천](https://user-images.githubusercontent.com/90893428/170536873-fd9a208e-d68a-4e3c-a31c-442f022ab473.PNG)

- 사용자가 리뷰를 작성 및 삭제하고, 좋아요를 누를 수 있습니다.
- 좋아요의 갯수에 따라 자동으로 좋아요 상위 3개의 댓글이 화면 상단에 실시간으로 배치됩니다.





### 🌱#3-13 영화 세부 정보

![다이얼로그세부정보](https://user-images.githubusercontent.com/90893428/170536878-1c9847ab-9c51-4db5-a09d-f13cda028202.PNG)

- 영화의 세부 설명 및 출연 배우들을 카드 형태로 접할 수 있습니다.
- 클릭 시에 해당 배우의 이름이 띄워집니다.

# 🌳#4 느낀 점

### 🌱이원우

쉼 없이 달리며 욕심껏 기획하고 만들며 첫 프로젝트의 끝에 도달했습니다. 처음으로 완성해본 협업 프로젝트이자 완전한 기능을하는 하나의 서비스를 만들었다는 기분이 들어 매우 벅찼습니다. 지금은, 더욱 완벽하게 만들고 싶은 아쉬움이 남고, 제한된 시간 내에 매 시간 매 분 매 초를 소통하며, 기능 단위로 구현해 서로 어려움도 있었고, 시행착오도 많았습니다.

하지만, 짧은 시간 내에 많은 깨달음과 성장이 있었던만큼 보람있었습니다. 이번 프로젝트에서 가장 좋았던 부분은 페어와 오랜 시간을 소통하며 문제를 함께 해결하며 나아가서 이 정도 결과물이 나올 수 있었던 것 같습니다. 이번 경험을 계기로 한 단계 더 나아가서, 팀원들과 원활히 소통해 2학기도 무사히 마치고싶었습니다. 모두 1학기와 최종 프로젝트 고생 많았습니다!
