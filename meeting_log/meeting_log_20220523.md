# 1. Meeting Log



### # 커뮤니티 작성글 삭제 기능 연결 (박재현)

* 어제에 이어, 작성글 삭제 버튼과 실제 요청을 연결하였다.

![image](https://user-images.githubusercontent.com/97648026/169882831-cd127074-9c2a-41f7-8111-c98b2067974d.png)



### # 영화 상세페이지 기능 구현 (박재현)

**주요 구현 내용**

* 리뷰 페이지네이션
* 베스트 리뷰 3개 상단 노출
* 리뷰 삭제



### 결과 사진

* 갱신되기 이전 베스트3 리뷰

![image](https://user-images.githubusercontent.com/97648026/169883326-ec8266fe-ce06-4dd0-a550-b9362639af1c.png)

* 베스트3 리뷰 갱신된 모습

![image](https://user-images.githubusercontent.com/97648026/169883701-07c64b94-dedc-496c-b54e-c0534cb2c2cb.png)



#### 베스트 3 알고리즘

![image](https://user-images.githubusercontent.com/97648026/169884010-85756925-a812-49df-bbec-fbdeb5f6956b.png)

> for문을 통해, best 3 항목을 찾아내고, splice로 인한 index 변화에 영향 받지 않도록 정렬하여 return 하였다.



### # 게시글 작성후, Detail페이지로 정상 이동하지 않는 문제 해결(박재현)

> 문제 상황
>
> * 이전에 작성 후 Detail페이지로 이동이 되었으나, 이동하지 않는 것을 발견하였다.

**해결**

* 게시판에서 Detail페이지로 이동은 이루어지나, 게시글 작성 후 이동이 안되어 두 코드를 비교
  * 게시판 -> Detail에서 넘겨지는 params 목록이 추가되어, 게시글 작성 후 이동에 넘겨지는 params가 부족하여 정상 작동하지 않았다.
  * params에 필요 항목을 추가하여 해결 완료



### **# 향**후 과제









## 세부 기능 구현 및 수정(이원우)

![332](https://user-images.githubusercontent.com/90893428/169887339-7a726362-22b4-4faa-b8ec-9441a08e41a3.PNG)
![캡처](https://user-images.githubusercontent.com/90893428/169887345-054a6b92-b9f9-45f4-9814-99fbe745034a.PNG)
![13](https://user-images.githubusercontent.com/90893428/169887349-4e1c257c-7b93-42a2-8f9a-bed144372946.PNG)

### 문제해결 및 달성

- 영화 상세 모달 버튼 업데이트 수정 => 토글 부분이 가끔 delete가 한 번씩 안눌리는데 어떻게 해야할지 모름.
- 프로필 페이지 영화 정보 카드뷰로 만들기 => 완료
- 작성한 게시글, 좋아요한 게시글 카드로 만들기 / 링크 연결 => 완료 
- 회원 정보 수정 페이지 만들기 => 완료
- 게시판 글쓴이 클릭하면 프로필로 이동 / 빠짐없이 링크 걸어줌 => 완료
- => 문제 발생 라우터를 거칠 때, 유저 정보의 불일치 발생

### 아직 해결하지 못한 문제

- 다른 사람의 프로필로 갔을 때 팔로우 팔로잉이 업데이트 되지 않고 params로 넘어와 프로필이 나의 프로필만 보여주는 문제 발생
