<template>
  <div style="background-color: grey">
    <div class="profile__div1__profile_img">
      <img
        src="https://www.hidomin.com/news/photo/202105/453232_224470_4025.jpg"
        alt=""
      />
    </div>
    <div class="profile">
      <div class="profile__div1">
        <div class="profile__position">
          <div>
            <button class="profile__div1__follow_btn">
              <span>팔로우</span>
            </button>
          </div>
        </div>
      </div>
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
  opacity: 0.7;
  border-radius: 2%;
  margin: 0 auto;
  margin-top: 150px;
  width: 1100px;
  height: 1400px;
}

.profile__div1 {
  border-radius: 2%;
  background-color: rgb(192, 177, 177);
  height: 600px;
  position: relative;
}

.profile__position {
  position: absolute;
  background-color: black;
  width: 550px;
  height: 520px;
  margin-left: 40px;
  margin-top: 40px;
}

.profile__div2 {
  background-color: darkcyan;
  height: 600px;
}

.profile__div1__profile_img {
  z-index: 100;
  position: absolute;
  margin-left: 1100px;
  margin-top: 100px;
  width: 500px;
  height: 700px;
  border-radius: 5%;
  background-color: red;
}

.profile__div1__profile_img img {
  width: 500px;
  height: 700px;
  border-radius: 5%;
  box-shadow: -5px 0px 30px rgb(161, 157, 157);
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
