# 1. Meeting Log



## # CommnunityView 작성 (박재현)



* 유저게시글의 조회페이지를 생성



### 와이어 프레임

![image](https://user-images.githubusercontent.com/97648026/169448792-8b550a6c-550d-4481-adf5-120712cc7eab.png)

### 완성된 결과 사진

![image](https://user-images.githubusercontent.com/97648026/169473859-f9bd456b-3a04-4865-9ae4-641103f8083a.png)



## # ArticleView 작성 (박재현)



### 와이어 프레임



![image](https://user-images.githubusercontent.com/97648026/169474123-a82c000d-0a60-4f66-bef4-34ffee87047c.png)

### 완성된 결과 사진


## #게시판 와이어프레임 설계 (이원우) -----

- ArticleDetailView

![캡처](https://user-images.githubusercontent.com/90893428/169447062-ea1df668-23de-449a-a535-65a08d1bb6f4.PNG)



## # Logout Profile 구현

- 로그아웃은 로컬스토리지에서 토큰을 삭제해 인증되지 않도록 만들었고 로그아웃 후에는 로그인 페이지로 이동하도록 해줬습니다.
- profile은 variable routing을 통해 구현했으며, 해당 유저의 정보를 가지고 프로필에 도달할 수 있도록 구성했습니다.



## # 커뮤니티 서버 생성 & 검증

- 검증은 postman을 통해 검증했습니다.
- 게시글 작성, 수정, 삭제 완료
- 댓글 작성, 수정, 삭제 완료
- 게시글 좋아요, 게시글에 달린 댓글 좋아요 완료



## 로그인 폼 UI 개선

![캡처](https://user-images.githubusercontent.com/90893428/169536362-5fafbdcb-d970-4a24-a4ca-adb97fbf203a.PNG)





### 문제 해결



#### #1. 알고리즘으로 보여주는 영화 카드가 새로고침 시에 사라지는 문제 발생

- 원인

  - 로그인되면 해당 유저의 pk에서 유저가 좋아하는 장르를 통해 가공하는 과정을 거침
  - 새로고침하면 로그인은 되어있으나 휘발성인 유저 정보는 state에서 사라짐

- 해결

  - 새로고침 시에도 사라지지 않도록 로컬스토리지에 저장
  - 저장된 유저 정보는 다른 유저가 로그인 시에는 자동으로 해당 유저 정보로 대체

- 2차 해결(개선)

  - 초기 app.vue에서 생명주기 인스턴스 생성 후 바로 로그인된 유저 정보를 불러 해결

  

#### #2. 게시글에 달린 댓글에 좋아요 누르기

- 댓글이 달린 게시글이 아닌 곳에서 요청을 보내 댓글에 좋아요를 남기는 것이 가능할 수 있음.
- 댓글에 좋아요를 누르려면 조회한 게시글과 댓글이 작성된 게시글의 ID값이 같은지 검증해야했음.
- 그래서 ORM으로 조회한 object를 직렬화한 후 딕셔너리 객체로 조회함으로써 pk를 비교해 검증함.








### 댓글 Onmouse

![image](https://user-images.githubusercontent.com/97648026/169535424-fe3361d9-e7b2-495b-9202-bd5e5684af7a.png)

* 댓글에 onMouse시 삭제버튼이 나오고 leaveMouse시 삭제버튼이 사라지도록 구현



### Comment 작성 버튼 클릭시

![image](https://user-images.githubusercontent.com/97648026/169535965-301cd332-cdc4-4e7d-9358-67db9cddb45e.png)

* Comment 작성하는 Modal 창이 생성된다.



![image](https://user-images.githubusercontent.com/97648026/169536299-1a9cc5f3-00ce-493a-9dc6-ce8006a8b2ee.png)

* 우측 위에 존재하는 세로 점을 클릭시, 게시글 수정, 게시글 삭제 창이 생성된다.



## #Movie-detail-review 작성 (박재현)



### 와이어 프레임

​	![image](https://user-images.githubusercontent.com/97648026/169550383-1cb8c572-febf-442f-a35d-82f2160527c4.png)



### 결과 사진

![image](https://user-images.githubusercontent.com/97648026/169555705-b10d12ee-d413-4de4-948f-32892f707cc2.png)

* 별을 클릭 함으로써 색상이 toggle 된다.

* 추천수 많이 받은 게시물의 여부에 따라, 색상이 바뀌어 표시된다.

  

### # 향후 과제

* 게시글 수정 페이지
* 게시글 작성 페이지
* Detail Modal과 연결

