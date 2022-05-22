<template>
  <div style="background-color: grey">
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

      <v-app class="profile__div1">
        <div class="profile__position">
          <div class="profile__position__header">{{ profile.username }}</div>
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
              <span v-for="genre in genres_list" :key="genre">
                {{ genre }}
              </span>
            </div>
          </div>

          <div class="profile__position__button">
            <button
              v-show="!(currentUser.username === profile.username)"
              @click="
                followProfile(profile.pk, profile.username);
                followOrUnfollow();
              "
              class="profile__div1__follow_btn"
            >
              <span v-if="unFollowButton">팔로우</span>
              <span v-if="!unFollowButton">언팔로우</span>
            </button>
          </div>
        </div>
        <v-tabs color="deep-purple accent-4" left>
          <v-tab>Landscape</v-tab>
          <v-tab>City</v-tab>
          <v-tab>Abstract</v-tab>

          <v-tab-item class="rounded-container" v-for="n in 3" :key="n">
            <v-container fluid style="margin-top: 100px">
              <v-row class="rounded-container">
                <v-col
                  class="rounded-container"
                  v-for="i in 6"
                  :key="i"
                  cols="12"
                  md="4"
                >
                  <v-img
                    class="rounded-container"
                    :src="`https://picsum.photos/500/300?image=${
                      i * n * 5 + 10
                    }`"
                    :lazy-src="`https://picsum.photos/10/6?image=${
                      i * n * 5 + 10
                    }`"
                    aspect-ratio="1"
                  ></v-img>
                </v-col>
              </v-row>
            </v-container>
          </v-tab-item>
        </v-tabs>
      </v-app>

      <div class="profile__div2"></div>
    </div>

    <!-- <div>
    <h1>{{ profile.username }}</h1>

    <h2>작성한 글</h2>
    <ul>
      <li v-for="article in profile.articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>

    <h2>좋아요 한 글</h2>
    <ul>
      <li v-for="article in profile.liked_articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>
  </div> -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ProfileView",
  computed: {
    ...mapGetters(["profile", "currentUser"]),
  },
  methods: {
    ...mapActions(["fetchProfile", "followProfile"]),
    followOrUnfollow() {
      if (this.profile.followers.includes(this.currentUser.pk)) {
        this.unFollowButton = true;
      } else {
        this.unFollowButton = false;
      }
    },
  },
  data() {
    return {
      tab: null,
      items: ["My Movies", "작성한 게시글", "좋아요한 게시글!"],
      genres_list: [],
      myProfile: false,
      unFollowButton: true,
    };
  },

  async created() {
 

    const payload = { username: this.$route.params.username };
    this.fetchProfile(payload);

    const res = await fetch("http://127.0.0.1:8000/movies/genres/");
    const save_genres = await res.json();
    const list_gen = JSON.parse(this.profile.genre_likes);
    if (save_genres) {
      this.genres_list = list_gen.genre_likes.map((item) => {
        for (let i = 0; i < save_genres.length; i++) {
          if (parseInt(item) === save_genres[i].id) {
            return save_genres[i].name;
          }
        }
      });
    }
       //처음부터 로그인한 유저가 팔로워 목록에 없다면 팔로우를 띄우기 위해 false
    for (let i = 0; i < this.profile.followers.length; i++) {
      if (this.currentUser.pk === this.profile.followers[i]) {
        this.unFollowButton = false;
        console.log(this.unFollowButton);
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
</style>
