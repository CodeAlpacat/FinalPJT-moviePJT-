# 1. Meeting Log

### 1) 영화 추천 알고리즘 브레인 스토밍

> 
>
> 기본 틀:  특정 ?? 사람들은 ?? 장르를 좋아한다. 
>
> - 특정 A에 관심있는 사람들은 B 장르를 좋아한다. => MBTI의 enfj들은 B장르를 좋아한다.
> - 거주 지역이 A인 사람들은 B 장르를 좋아한다.
> - 취미가 A이고 취미와 관련된 장르가 a, b, c,.. 이면 해당 장르의 영화들 중 평점이 N 이상인 영화
> - 날씨 API에 맞는 영화 추천
> - 특정 영화에 평점을 부여 => 부여한 평점이 N 이상 => 유저 favorite에 저장 => favorite 필드의 영화의 장르가 호러, 액션, 드라마 => 해당 장르의 영화 추천 
>
> - 특정 ?? 사람들은 시리즈 영화를 좋아한다. => 캐리비안의 해적1 => 2 ... 3.. 시리즈의 한 편을 좋아요? or follow? or 평점 매김? 하면 해당 시리즈의 영화 or 해당 영화 감독의 영화들을 추천

### 2) ERD

![erd](https://user-images.githubusercontent.com/90893428/167900154-dfad3db7-f7cb-407f-8c2d-16d53ed6db64.png)

#### 1) movies_movie => movies_actor(1:N)

- 해당 영화의 배우들 참조 
- 역참조를 통해 해당 배우가 출연한 영화 목록

#### 2) movies_movie => movies_review (1:N)

- 영화에 달린 리뷰
- 역참조를 통해 영화에는 여러 개의 리뷰 작성이 가능

#### 3) movies_review => movies_review_likes(1:N)

- 리뷰 좋아요
- 역참조를 통해 리뷰엔 여러 개의 좋아요가 가능
- 좋아요의 개수 순위로 가장 많은 좋아요가 달린 리뷰 3개만 베스트 댓글로 지정(정렬)

#### 4)  movies_movie <= movies_genres_name(N:1)

- 영화의 장르들을 참조
- 역참조를 통해 해당 장르의 영화

#### 5) movies_movie => user_keep_movie(1:N)

- 나중에 볼 영화 keep
- 역참조를 통해 keep한 영화들의 목록 가져오기

#### 6) accounts_user => movies_review (1:N)

- 작성한 리뷰
- 역참조를 통해 리뷰를 작성한 유저인지 판단

#### 7) accounts_user => movies_review_likes(1:N)

- 리뷰를 좋아요 했는지 안했는지

#### 8) accounts_user => user_keep_movie(1:N)

- 해당 유저가 영화를 킵했는지





