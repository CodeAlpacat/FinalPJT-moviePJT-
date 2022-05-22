# 1. Meeting Log



### # 게시판 이동시 댓글 작성자 이름을 받아 올 수 없는 문제(박재현)



> 문제 상황
>
> - 게시판 이동시, Detail 페이지에서 게시글 댓글 content는 정상 출력 되지만, 사용자 이름은 출력 되지 않는 문제가 발생하였다.
> - 확인한 결과, 게시판 -> Detail 이동시에 받아오는 article.comments에서는 user가 pk 값을 받아오지만 게시글 내에 댓글 작성 후 갱신되는 comments 정보는 user가 pk,username Object 형태로 갱신되어 정상 출력되었다.



![image](https://user-images.githubusercontent.com/97648026/169691525-6cd8e65a-cbab-4cff-9da8-21a7a16acc93.png)

* 게시판 -> Detail 이동시 받아오는 article.comments 정보

![image-20220522194756822](meeting_log_20220521.assets/image-20220522194756822.png)

* 댓글 생성후 갱신된 article.comments 정보



#### #해결 과정

* 게시판 -> Detail 이동시 받아오는 article.comments 정보는 comment 모델필드의 값을 가져오고, 갱신되는 article.comments 정보는 새로 재정의된 값을 가져왔다.

  ![image](https://user-images.githubusercontent.com/97648026/169691746-f84ff665-1de3-448f-929e-af3c6494e234.png)

![image](https://user-images.githubusercontent.com/97648026/169691764-d4a7da38-d563-4d07-9c7b-e3ef2396862e.png)

* 따라서 기존 게시판 -> Detail 이동시 받아오는 article.comments 정보를 새롭게 재정의하여 해결하였다.

  ![image](https://user-images.githubusercontent.com/97648026/169691783-44987fac-c8b4-48c4-afee-066e8ebd84f6.png)




## 기능 구현(이원우)

![캡처](https://user-images.githubusercontent.com/90893428/169707242-842ebc5f-42a2-4a1e-b1dc-399c481bf45b.PNG)

![2](https://user-images.githubusercontent.com/90893428/169707241-78d840a2-6324-47c8-b9b2-556db6409d05.PNG)

- 프로필 팔로우, 언팔로우 및 데이터 확인 / 팔로우, 팔로잉 갱신 확인
- 개별 좋아하는 영화 담기 기능 완료 (문제점 발생: 팔로우가 되었는지 다시 들어가면 갱신이 되지 않음.)
- 프로필 이미지 데이터베이스 저장 및 출력
- 영화 디테일 다이얼로그와 개별 영화 컴포넌트 및 데이터 연결 완료
- 좋아하는 영화 목록 프로필 페이지에 띄우기 성공

### # 향후 과제

* 상세 페이지에서 글 수정 페이지로 이동하는것 하기
* 글 작성 및 글 수정 페이지 만들기

