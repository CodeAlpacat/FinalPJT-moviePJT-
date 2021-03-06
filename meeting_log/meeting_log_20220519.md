# 1. Meeting Log



## #이미지 필드 저장문제

>  signup과정에서, vue의 이미지파일 저장 형식과 rest_api의 이미지파일 저장 형식이 달라, 같은 방법으로 인코딩, 디코딩 해야하는 문제가 발생하였다.

* 해결방안
  * base64로 통일
  * but, 매우 복잡하여 추후 과제로 돌렸다.



## # 유저 Signup 연동

> 이전에 제작한 Vue Signup 페이지와 Rest_api간의 연동을 성공하였다.
>
> * signup을 통하여 db에 사용자가 생성된 것을 확인

**확인된 문제**

* genre필드가 제대로 DB에 저장되지 않았다. JSONField 형식에 맞지 않게 들어가는 것으로 판단되어 확인중

**해결**

* vue와 rest_api간의 key값이 통일되지 않아 발생하였고, JSONField 형식에 맞지 않아 data 값이 들어가지 않았다.



### # 유저 선호 genre를 통한 추천 알고리즘 연동

> 가상의 genre 리스트를 통해 구현한 추천 알고리즘을 실제 로그인한 유저의 genre 리스트를 통해 추천받기

**주요 변경사항**

* 추천 url에 user_pk값을 추가로 요청한다.
  * `'recommend/'` => `'recommend/<int:user_pk>/'`
  * view함수 또한 user_pk인자를 받아야한다.
  * user_pk로부터 user를 가져와 genre_list를 참조한다. 이때, parsing을 진행하고, 비교시 str형태의 숫자로 비교한다.

### # Vue 카드 컴포넌트 및 맞춤형 추천 영화 출력

- 이진 탐색을 통해 장르 선호도에 따른 추천 영화들을 JSON으로 받아옴.
- 실제 카드 컴포넌트를 넣고 구현

#### 발생한 문제점

- 로그인한 유저가 없는 경우에는 유저의 pk값이 넘어오지 않는 문제점 발생

- vue에서 if문을 통해 생명주기의 created에서 로그인한 유저가 존재하면 추천 영화를 가져오고, 로그인한 유저가 없다면 현재 상영중인 영화를 자동으로 요청해 가져옴.

- 카드 컴포넌트의 craousel-3d 컴포넌트를 활용해 추천 알고리즘을 적용한 영화 리스트를 강조함.

  

### # V-Dialog를 이용한 Detail Modal 생성

> Vuetify의 V-Dialog를 이용하여 Detail-Modal을 생성 및 하위 컴포넌트를 생성하였다.

* Overview, Review, Recommendation 창의 바뀌는것은 v-show와 @click을 통해 구현하였으며, 정상적으로 토글하는 것을 확인하였다.
* Detail Modal에서 기본적으로 존재하는 닫기버튼과 Add my movie 버튼은 생성하였으며, 닫기버튼의 경우, 누를 경우 modal이 닫히도록 하였다.



### # 향후 과제

* Detail Modal 구체화
* Detail Modal과 연결

