<template>
  <div class="profile">
    <div class="profile__div1">
      <div class="profile__div1__profile_img">
        <img
          src="https://dimg.donga.com/wps/NEWS/IMAGE/2021/12/24/110942647.2.jpg"
          alt=""
        />
      </div>
      <div class="profile__div1__follow">
        <button class="profile__div1__follow_btn">
          <span>팔로우</span>
        </button>
      </div>
      <div>
        <img
          class="profile__div1__img"
          src="data:image/jpeg;base64,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"
        />
      </div>
    </div>
    <div class="profile__div2">
      <div class="profile__div2__user_info">유저네임</div>
      <div class="profile__div2__user_info">게시글 팔로잉 팔로우</div>
      <div class="profile__div2__user_info">이메일</div>
    </div>

    <div class="profile__div3"></div>
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
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "ProfileView",
  computed: {
    ...mapGetters(["profile"]),
  },
  methods: {
    ...mapActions(["fetchProfile"]),
  },
  created() {
    const payload = { username: this.$route.params.username };
    this.fetchProfile(payload);
  },
};
</script>

<style>
.profile {
  margin: 0 auto;
  margin-top: 70px;
  width: 1200px;
  height: 1700px;
  background-color: white;
}
.profile__div1 {
  background-color: rebeccapurple;
  height: 800px;
  position: relative;
}
.profile__div2 {
  background-color: darkcyan;
  height: 300px;
}

.profile__div3 {
  background-color: skyblue;
  height: 600px;
}

.profile__div1__img {
  width: 100%;
  height: auto;
  max-height: 600px;
}

.profile__div1__profile_img {
  position: absolute;
  margin-left: 425px;
  margin-top: 425px;
  width: 350px;
  height: 350px;
  border-radius: 50%;
  background-color: white;
}

.profile__div1__profile_img img {
  position: absolute;
  width: 350px;
  height: 350px;
  border: solid 3px;
  border-radius: 50%;
  border-color: white;
  background-color: white;
}

.profile__div1__follow {
  position: absolute;
  margin-left: 950px;
  margin-top: 537px;
  width: 125px;
  height: 125px;
  border-radius: 50%;
}

.profile__div2__user_info {
  text-align: center;
  font-size: 30px;
  font-weight: bold;
  font-family: sans-serif;
  margin-bottom: 40px;
}

.profile__div1__follow_btn {
  width: 120px;
  height: 50px;
  border-radius: 30px;
  border: none;
  color: white;
  background-color: rgb(82, 193, 237);
  text-align: center;
  opacity: 1;
  cursor: pointer;
  transition: 0.5s;
  margin-top: 35px;
}
.profile__div1__follow_btn:hover {
  opacity: 0.9;
}

.profile__div1__follow_btn span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
  font-size: 16px;
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
</style>
