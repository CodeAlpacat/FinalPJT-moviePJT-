# 1. Meeting Log



## # CommnunityView Backend 연동 (박재현)



## 결과 사진

![image](https://user-images.githubusercontent.com/97648026/169651288-62c73270-50ee-4d8c-b712-2f18d2951d60.png)

![image-20220521212052256](meeting_log_20220520.assets/image-20220521212052256.png)

#### 주요 기능

* pagination
  * 1페이지당 10개의 게시물을 출력, 가장 최근의 게시물이 보이도록 하였다.
* 생성 시간 표시
  * 1일이 지나갔을 경우 년,월,일을 출력
  * 24시간 내에 작성시, ~시간 전 출력
  * 1시간 이내에 작성시, ~분 전 출력
  * 1분 이내에 작성시, 방금 전 출력
* 하단 글 작성 버튼 글 작성 페이지와의 연동




## #ArticleDetailView Backend 연동 (박재현)



### 결과 사진

![image](https://user-images.githubusercontent.com/97648026/169666836-897c7a06-961a-4960-b7dc-33381cce206f.png)

![image](https://user-images.githubusercontent.com/97648026/169666888-f541fcb6-db88-4631-bfba-89fe2449e62e.png)

![image](https://user-images.githubusercontent.com/97648026/169666906-b319e60e-1c26-4a57-9a2e-979d5a4d4ed9.png)



### 구현된 주요 기능

* 작성된 글 삭제하기
* 사용자가 좋아요 했을 시, 상세 페이지에서 보이는 하트가 빨간색, 안 했을 시, 회색으로 보이게 하기
* 댓글 작성
* 작성한 사용자가 댓글 삭제 가능



### # 향후 과제

* accounts에 작성한 article관련 메서드들 articles로 옮기기
* 상세 페이지에서 글 수정 페이지로 이동하는것 하기
* 글 작성 및 글 수정 페이지 만들기

