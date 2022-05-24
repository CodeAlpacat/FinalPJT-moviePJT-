# 1. Meeting Log

## 세부 기능 구현 및 수정(이원우)
> 앱 이름 브레인 스토밍
>
> * 영화
> * 무비
> * 파이썬
> * 도라에몽
> * 외국어 섞기
> * 비바라 비다
> * 무비바라 ★★★
>   * 무비보라
>   * MOVIEVOLA
>   * ALOVEIOM
>   * 무비볼래
>   * MOVIEVOLAE
>   * EALOVEIVOM
>   * 무비무라
> * 무비바라했다
> * MOVIEVALA
> * 무비잇
> * 펜 파이에썬 애플
> * 무비 아무르
> * 무비홀릭
> * 무비비스트로
> * 아이
> * 오피스
> * 박스
> * 시네
> * 시네마
> * 무비타임
> * MV.GG
> * 무터레스팅
> * 엠터레스팅
> * Mteresting
> * 무마초
> * 무스트코
> * 무비트레이더스
> * 무텔라
> * 무웅치킨
> * 함무바라  ★★★★★★★★★★★★★★★★★★★★★★★★
>   * 직인다 아이가
>     * 서울에는 이런거 읎제?



#### 영화 앱 이름 결정 완료

* 함무바라
  * 한번 Movie 보아라 줄임말

### 

#### 가로형 로고

![image](https://user-images.githubusercontent.com/97648026/170070287-cbed1e07-d24c-4a2b-811e-7c784283b2e5.png)

![캡처](https://user-images.githubusercontent.com/90893428/170109065-970d6c97-8850-46d7-b5a5-54788189ccdb.PNG)

![캡처](https://user-images.githubusercontent.com/90893428/170108929-2c3d94f9-0ffd-43f4-b2a6-1660670a16a9.PNG)

### 문제해결 및 달성

- 게시판에 방문 시에 유저 정보가 새로고침이 일어나지 않으나 같은 컴포넌트를 참조함으로 인해서 정보가 갱신되지 않는 문제점 발생.
- 현재 유저가 아닌 새로운 유저의 정보를 받아와 props, params로 넘겨주는 get 요청을 위한 actions 생성.
- 네비게이션 바 UI 디자인 및 영화 검색 기능 구현.
- 영화 페이지 로고 디자인 완료

- 메인 페이지 Carousel 생성 및 추천 영화 비율 조정. 기존 카드들에 생성된 UI의 Detail을 띄우기 위한 링크 각각 생성 및 연동


#### 세로형 로고

![image](https://user-images.githubusercontent.com/97648026/170069349-abe837bb-28aa-470f-8fd6-ea754c9ca0ac.png)







### #Detail Dialog 상단 영화, 포스터 크라우젤 생성 (박재현)

![image](https://user-images.githubusercontent.com/97648026/170106641-41361b64-fdf0-4016-8943-c6ff53d53486.png)



#### 주요기능

* 상단에 영화 트레일러 주소를 요청하여 출력.
* 비동기 처리를 위하여 created에 axios 요청, 요청성공시 필요한 데이터를 data에 선언 후, 값 갱신하여 출력하였다.
* 1번째는 영화, 2번째는 영화 포스터가 노출되도록 설정.



### #Description 페이지 개선 및 하단 영화배우 목록 출력(박재현)



![image](https://user-images.githubusercontent.com/97648026/170107293-0f2480b4-49c1-483c-a569-e7b0a2b363b6.png)



![image](https://user-images.githubusercontent.com/97648026/170107527-f739a812-5db8-4017-b5f6-86f2e39064f7.png)



#### 주요기능

* 요청을 통해 얻어지는 배우들의 프로필 사진과 이름으로 하단에 출연자 목록을 출력.
* 프로필 사진을 클릭시, 가운데에 배우의 이름을 출력한다.



### 추후 과제

- Overview -> Related movie로 바꾸고 Related movie 목록 출력 페이지로 바꾸기
- 상단 선택바에서 더 나은 사용자 경험을 선보일 수 있도록 vuetify나 transition 속성 적용하기
- 모든 색상 테마에 맞춰 바꾸기
