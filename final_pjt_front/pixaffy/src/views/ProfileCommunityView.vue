<template>
  <div>
    <div class="profile">
      <div class="profile__gap">
        <div class="profile__div1__profile_img">
          <img
            :src="
              nowUserProfile.profile_img
                ? nowUserProfile.profile_img
                : 'https://user-images.githubusercontent.com/90893428/169695116-afc5cb17-b075-43c9-9ff8-7c8155c8dd79.png'
            "
            alt="프로필 사진이 없습니다."
          />
        </div>
      </div>

      <v-app class="profile__div1">
        <div class="profile__position">
          <div class="profile__position__header">
            {{ $route.params.username }}
          </div>
          <hr />
          <div class="profile__position__content">
            <i class="fa-solid fa-envelope fa-lg"></i>
            <div>{{ nowUserProfile.email }}</div>
          </div>
          <div class="profile__position__content">
            <i class="fa-solid fa-users-line fa-lg"></i>
            <div>
              게시글:
              {{
                nowUserProfile.articles.length
                  ? nowUserProfile.articles.length
                  : 0
              }}
              팔로워:
              {{
                nowUserProfile.followers.length
                  ? nowUserProfile.followers.length
                  : 0
              }}
              팔로잉:
              {{
                nowUserProfile.followings.length
                  ? nowUserProfile.followings.length
                  : 0
              }}
            </div>
          </div>
          <div class="profile__position__content">
            <i class="fa-solid fa-film fa-lg"></i>
            <div>
              좋아하는 장르:
              <span v-for="(genre, idx) in genres_list" :key="idx">
                {{ genre }}
              </span>
            </div>
          </div>

          <div class="profile__position__button">
            <button v-if="follow_bool" class="profile__div1__follow_btn">
              <router-link
                :to="{
                  name: 'profileEdit',
                  params: {
                    username: nowUserProfile.username,
                    userInfo: nowUserProfile,
                  },
                }"
                ><span class="span_edit">회원정보수정</span></router-link
              >
            </button>
            <button
              v-if="!follow_bool"
              @click="
                followProfile(nowUserProfile.pk);
                followOrUnfollow();
              "
              class="profile__div1__follow_btn"
            >
              <span v-if="unFollowButton">팔로우</span>
              <span v-if="!unFollowButton">언팔로우</span>
            </button>
            <button class="profile__div1__follow_btn">
              <router-link
                :to="{
                  name: 'community',
                }"
                ><span class="span_edit">뒤로가기</span></router-link
              >
            </button>
          </div>
        </div>
      </v-app>

      <div class="profile__div2">
        <v-app>
          <v-tabs color="deep-purple accent-4" style="padding: 20px">
            <v-tab>MY MOVIES</v-tab>
            <v-tab>작성한 게시글</v-tab>
            <v-tab>좋아요한 게시글</v-tab>

            <v-tab-item style="margin-top: 50px; margin-left: 10px; height: 600px;">
              <v-row justify="center">
                <v-col
                  cols="3"
                  outlined
                  tile
                  v-for="movie in nowUserProfile.keep_movies"
                  :key="movie.id"
                >
                  <card-movie-view-item
                    :movie="movie"
                    :profile="profile"
                    style="background-color: #1f293c !important"
                  ></card-movie-view-item>
                </v-col>
              </v-row>
            </v-tab-item>
            <v-tab-item style="margin-top: 50px; margin-left: 10px; height: 600px;">
              <div v-for="(article, idx) in this.articleList" :key="idx">
                <template>
                  <!-- <v-card
                    shaped
                    hover
                    color="#BBDEFB"
                    height="200"
                    @click="reveal2 = !reveal2"
                    style="box-shadow: 2px -2px 10px"
                  >
                    <v-card-text>
                      <p class="text-h4 text--primary">{{ article.title }}</p>
                      <div class="text-h6">
                        작성 시각: {{ new Date(article.created_at) }}
                      </div>
                      <div class="text-h6">
                        수정 시각: {{ new Date(article.updated_at) }}
                      </div>
                      <div class="text-h6">
                        좋아요 수: {{ article.liked_users.length }}
                      </div>
                    </v-card-text>

                    <v-expand-transition>
                      <v-card
                        v-if="reveal2"
                        color="#BBDEFB"
                        class="transition-fast-in-fast-out v-card--reveal"
                        style="height: 100%"
                      >
                        <v-card-text class="pb-0 text-absolute-card">
                          <p class="text-h4 text--primary">
                            {{ article.title }}
                          </p>
                          <p class="text-h6">
                            {{ article.content }}
                          </p>
                          <button class="profile__div1__follow_btn">
                            <router-link
                              :to="{
                                name: 'article',
                                params: {
                                  article: article,
                                  articlePk: article.pk,
                                  isLiked: !!likedArticleList.includes(
                                    article.pk
                                  ),
                                  articleComments: article.comments,
                                  user: article.user,
                                },
                              }"
                            >
                              <span>바로가기</span></router-link
                            >
                          </button>
                        </v-card-text>
                      </v-card>
                    </v-expand-transition>
                  </v-card> -->
                  <user-posted-articles :article="article"></user-posted-articles>
                </template>
              </div>
            </v-tab-item>
            <v-tab-item style="margin-top: 50px; margin-left: 10px; height: 600px;">
              <div v-for="(article, idx) in this.articleLikeList" :key="idx">
                <template>
                  <user-posted-articles :article="article"></user-posted-articles>
                </template>
              </div>
            </v-tab-item>
          </v-tabs>
        </v-app>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import CardMovieViewItem from "@/components/CardMovieViewItem.vue";
import UserPostedArticles from "@/components/UserPostedArticles.vue";
export default {
  name: "ProfileCommunityView",
  components: {
    CardMovieViewItem,
    UserPostedArticles
  },
  computed: {
    ...mapGetters(["profile", "currentUser", "nowUserProfile", "articles", "likedArticleList",]),
    follow_bool() {
      return this.currentUser.username === this.nowUserProfile.username;
    },
  },
  methods: {
    ...mapActions([
      "fetchProfile",
      "followProfile",
      "fetchNowUserProfile",
      "fetchArticles",
      
    ]),
    followOrUnfollow() {
      if (
        this.nowUserProfile.followers.some(
          (item) => item == this.currentUser.pk
        )
      ) {
        this.unFollowButton = true;
      } else {
        this.unFollowButton = false;
      }
    },
  },
  data() {
    return {
      items: null,
      genres_list: [],
      unFollowButton: true,
      posterPath: null,
      reveal: false,
      reveal2: false,
      profileLoaded: null,
      articleList: [],
      articleLikeList: [],
    };
  },

  async created() {
    const payload = { username: this.$route.params.username };
    this.fetchNowUserProfile(payload);


    await this.fetchArticles();

    for (let i = 0; i < this.articles.length; i++) {
      if (this.nowUserProfile.pk == this.articles[i].user.pk) {
        this.articleList.push(this.articles[i]);
      }
      for (let j = 0; j < this.nowUserProfile.like_articles.length; j++) {
        if (this.nowUserProfile.like_articles[j].id == this.articles[i].pk) {
          this.articleLikeList.push(this.articles[i]);
        }
      }
    }

    const res = await fetch("http://127.0.0.1:8000/movies/genres/");
    const save_genres = await res.json();
    for (let i = 0; i < this.nowUserProfile.followers.length; i++) {
      if (this.currentUser.pk === this.nowUserProfile.followers[i]) {
        this.unFollowButton = false;
      }
    }
    this.items = this.nowUserProfile.keep_movies;
    const list_gen = JSON.parse(this.nowUserProfile.genre_likes);
    if (save_genres) {
      this.genres_list = list_gen.genre_likes.map((item) => {
        for (let i = 0; i < save_genres.length; i++) {
          if (parseInt(item) === save_genres[i].id) {
            return save_genres[i].name;
          }
        }
      });
    }
  },
};
</script>

<style>
.profile {
  margin: 0 auto;
  margin-top: 100px;
  width: 1400px;
  height: 1400px;
}
hr {
  margin-top: 20px;
  margin-bottom: 20px;
  border: 0px;
  width: 100%;
  border-top: 2px solid #663399;
  opacity: 0.35;
}

.profile__div1 {
  background-color: rgb(226, 216, 216);
  height: 600px;
  position: relative;
  box-shadow: -5px 2px 10px rgb(86, 75, 75);
}

.profile__div2 {
  background-color: rgb(226, 216, 216);
  height: 800px;
  box-shadow: -5px 2px 10px rgb(86, 75, 75);
}

.profile__position {
  width: 700px;
  height: 520px;
  margin-left: 40px;
  margin-top: 40px;
  margin-bottom: 100px;
}
.profile__position__button {
  margin-top: 22px;
  margin-left: 10px;
}

.profile__position__header {
  font-size: 53px;
  font-weight: bold;
  font-family: sans-serif;
}
.profile__position__content {
  display: flex;
  font-size: 28px;
  font-weight: bold;
  font-family: sans-serif;
  align-items: center;
  margin-top: 30px;
}
.profile__position__content div {
  margin-left: 20px;
}

.profile__div2 {
  height: 600px;
}

.profile__div1__profile_img {
  z-index: 1;
  position: absolute;
  margin-left: 950px;
  width: 500px;
  height: 680px;
  border-radius: 5%;
  background-color: white;
}

.profile__div1__profile_img img {
  width: 500px;
  height: 680px;
  border-radius: 5%;
  box-shadow: -5px 0px 40px rgb(86, 75, 75);
}

.profile__div2__user_info {
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  font-family: sans-serif;
  margin-bottom: 40px;
}

.profile__div1__follow_btn {
  width: 170px;
  height: 50px;
  border-radius: 30px;
  border: none;
  color: white;
  background-color: rgb(23, 146, 195);
  text-align: center;
  opacity: 1.3;
  cursor: pointer;
  transition: 0.5s;
  margin-top: 35px;
  box-shadow: 2px 2px 2px grey;
}

.profile__div1__follow_btn:hover {
  opacity: 0.9;
}

.profile__div1__follow_btn span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
  font-size: 20px;
  font-weight: bold;
}

.profile__div1__follow_btn .span_edit:after {
  content: "\f4ff";
  font-family: "Font Awesome 5 Free";
  font-weight: 900;
  font-size: 20px;
  position: absolute;
  opacity: 0;
  bottom: -2px;
  right: -10px;
  transition: 0.5s;
}

.profile__div1__follow_btn .profile__div__follow_btn_span:after {
  content: "\f100";
  font-family: "Font Awesome 5 Free";
  font-weight: 900;
  font-size: 20px;
  position: absolute;
  opacity: 0;
  bottom: -2px;
  right: -10px;
  transition: 0.5s;
}
.profile__div1__follow_btn .profile__div__follow_btn_content:after {
  content: "\f05a";
  font-family: "Font Awesome 5 Free";
  font-weight: 900;
  font-size: 20px;
  position: absolute;
  opacity: 0;
  bottom: -2px;
  right: -10px;
  transition: 0.5s;
}

.profile__div1__follow_btn span:after {
  content: "\f234";
  font-family: "Font Awesome 5 Free";
  font-weight: 900;
  font-size: 20px;
  position: absolute;
  opacity: 0;
  bottom: -2px;
  right: -10px;
  transition: 0.5s;
}

.profile__div1__follow_btn a span:after {
  content: "\f70c";
  font-family: "Font Awesome 5 Free";
  font-weight: 900;
  font-size: 20px;
  position: absolute;
  opacity: 0;
  bottom: -2px;
  right: -10px;
  transition: 0.5s;
}

.profile__div1__follow_btn:hover span {
  padding-right: 25px;
}

.profile__div1__follow_btn:hover span:after {
  opacity: 1;
  right: -1;
}

.profile__gap {
  height: 40px;
}

.rounded-container {
  border-radius: 50px;
}

.v-card--reveal {
  bottom: 0;
  opacity: 1 !important;
  position: absolute;
  width: 100%;
}

a {
  text-decoration: none;
  color: white !important ;
}
</style>
