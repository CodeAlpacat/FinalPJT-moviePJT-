<template>
  <div style="height: 100vh !important;">
    <div class="profile">
      <div class="profile__gap">
        <div class="profile__div1__profile_img">
          <img
            :src="
              profile.profile_img
                ? profile.profile_img
                : 'https://user-images.githubusercontent.com/90893428/169695116-afc5cb17-b075-43c9-9ff8-7c8155c8dd79.png'
            "
            alt="프로필 사진이 없습니다."
          />
        </div>
      </div>

      <v-app class="profile__div1 overflow-hidden">
        <div class="profile__position">
          <div class="profile__position__header">
            {{ $route.params.username }}
          </div>
          <hr />
          <div class="profile__position__content">
            <i class="fa-solid fa-envelope fa-lg"></i>
            <div>{{ profile.email }}</div>
          </div>
          <div class="profile__position__content">
            <i class="fa-solid fa-users-line fa-lg"></i>
            <div>
              게시글:
              {{ profile.articles.length ? profile.articles.length : 0 }}
              팔로워:
              {{ profile.followers ? profile.followers.length : 0 }}
              팔로잉:
              {{ profile.followings.length ? profile.followings.length : 0 }}
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
            <button class="profile__div1__follow_btn">
              <router-link
                :to="{
                  name: 'profileEdit',
                  params: { username: profile.username, userInfo: profile },
                }"
                ><span class="span_edit">회원정보수정</span></router-link
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
                  v-for="movie in profile.keep_movies"
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
              <div v-for="(article, idx) in profile.articles" :key="idx">
                <template>
                  <user-posted-articles :article="article"></user-posted-articles>
                </template>
              </div>
            </v-tab-item>
            <v-tab-item style="margin-top: 50px; margin-left: 10px; height: 600px;" >
              <div v-for="(article, idx) in profile.like_articles" :key="idx">
                <template>
                  <user-liked-articles :article="article"></user-liked-articles>
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
import UserLikedArticles from "@/components/UserLikedArticles.vue";
import axios from 'axios';
export default {
  name: "ProfileView",
  components: {
    CardMovieViewItem,
    UserPostedArticles,
    UserLikedArticles
  },
  computed: {
    ...mapGetters([
      "profile",
      "currentUser",
      "nowUserProfile",
      "isCommentLiked",
      "articles",
      "likedArticleList",
    ]),
    follow_bool() {
      return this.$route.params.username === this.nowUserProfile.username;
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
      if (this.profile.followers.some((item) => item == this.currentUser.pk)) {
        this.unFollowButton = true;
      } else {
        this.unFollowButton = false;
      }
    },
  },
  data() {
    return {
      tab: null,
      items: null,
      genres_list: [],
      unFollowButton: true,
      posterPath: null,
      reveal: false,
      reveal2: false,
      genre_save: null,
    };
  },

created() {
    const payload = { username: this.$route.params.username };
    this.fetchProfile(payload);

    this.fetchArticles()
    
    axios({
      url: "http://127.0.0.1:8000/movies/genres/"
    }).
    then((res) => {
      this.genre_save = res.data
      const list_gen = JSON.parse(this.profile.genre_likes);
      this.genres_list = list_gen.genre_likes.map((item) => {
        for (let i = 0; i < this.genre_save.length; i++) {
          if (parseInt(item) === this.genre_save[i].id) {
            return this.genre_save[i].name;
          }
        }
      });
    })

    this.items = this.profile.keep_movies;

    for (let i = 0; i < this.profile.followers.length; i++) {
      if (this.currentUser.pk === this.profile.followers[i]) {
        this.unFollowButton = false;
      }
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
  height: 600px;
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
  height: 800px;
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
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100px;
  height: 30px;
  border-radius: 30px;
  border: none;
  color: white;
  background-color: rgb(23, 146, 195);
  text-align: center;
  opacity: 1.3;
  cursor: pointer;
  transition: 0.5s;
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
  color: white;
}

a {
  text-decoration: none;
  color: white !important ;
}

.action-card {
  background-color: rgb(51, 56, 66) !important;
}
</style>
