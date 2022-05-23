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



