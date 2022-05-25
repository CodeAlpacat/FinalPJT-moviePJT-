<template>
  <div class="login-card">
    <account-error-list v-if="authError"></account-error-list>
    <div class="login-card__div" :class="`rounded-lg`">
      <div>
        <v-img
          class="login-card__div__img"
          src="https://img.freepik.com/free-photo/white-brick-wall-texture-design-empty-white-brick-background-for-presentations_1962-1075.jpg?w=1800"
          height="600px"
          width="500px"
        >
          <v-img
            style="margin-top: 130px"
            src="https://user-images.githubusercontent.com/90893428/170347769-b6d9286e-a86b-42fd-8f52-1f5fc18fa6e8.png"
          ></v-img>
        </v-img>
      </div>
      <!-- div와 div로 grid를 이용해 반으로 분할 -->
      <form
        @submit.prevent="updateProfile(credentials)"
        class="login-card__div__form"
      >
        <div class="text-center my-3 login-card__div__header">
          <h1>Edit Profile</h1>
        </div>
        <div class="login-card__div__form__input">
          <v-text-field
            class="login-card__div__right"
            prepend-icon="fa-solid fa-user"
            v-model="credentials.username"
            filled
            color="blue-grey lighten-2"
            label="username"
            required
            height="10px"
          ></v-text-field>
          <div></div>
        </div>
        <div class="login-card__div__form__input">
          <v-text-field
            prepend-icon="mdi-email"
            v-model="credentials.email"
            filled
            color="blue-grey lighten-2"
            label="E-mail"
            required
            :rules="emailRules"
            hide-details="auto"
          ></v-text-field>
        </div>
        <div class="select-button">
          <v-select
            @input="limit_items"
            v-model="genres_list"
            :items="genres_DB"
            item-text="name"
            item-value="id"
            :menu-props="{ maxwidth: '400' }"
            hide-selected
            label="장르"
            multiple
            chips
            deletable-chips
            hint="장르를 다시 선택해 주세요!"
            persistent-hint
          ></v-select>
        </div>
        <label for="input-file" class="input-file-button">프로필 사진</label>
        <input
          type="file"
          ref="doc"
          id="input-file"
          @change="findImg"
          style="display: none"
        />
        <button class="login-card__div__form__btn">
          <span>수정완료</span>
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AccountErrorList from "@/components/AccountErrorList.vue";

export default {
  name: "ProfileEditFormView",
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        currentUsername: this.$route.params.username,
        username: this.$route.params.userInfo.username,
        genre_likes: this.$route.params.userInfo.genre_likes,
        email: this.$route.params.userInfo.email,
        profile_img: this.$route.params.userInfo.profile_img,
      },
      loadedImage: null,
      content: null,
      genres_list: [],
      genres_DB: [],
      emailRules: [
        (value) =>
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
            value
          ) || "이메일 형식을 확인하세요.",
      ],
    };
  },
  computed: {
    ...mapGetters(["authError"]),
  },

  methods: {
    ...mapActions(["updateProfile"]),
    limit_items(e) {
      if (e.length > 3) {
        alert("세 개만 고를 수 있습니다.");
        e.pop();
      }
    },
    findImg(e) {
      let that = this.credentials;
      let reader = new FileReader();
      reader.onload = function (e) {
        that.profile_img = e.target.result;
      };
      reader.readAsDataURL(e.target.files[0]);
    },
  },
  watch: {
    genres_list: function (val) {
      val = val.map((item) => {
        return item.toString();
      });
      const new_val = { genre_likes: val };
      this.credentials.genre_likes = JSON.stringify(new_val);
    },
  },
  async created() {
    const response = await fetch("http://127.0.0.1:8000/movies/genres/");
    this.genres_DB = await response.json();
  },
};
</script>

<style scoped>
.login-card {
  margin: 0 auto;
  margin-top: 110px;
  height: 100vh;
}

.login-card__div {
  display: grid;
  grid: auto-flow / 1fr 1fr;
  min-height: 450px;
  min-width: 700px;
  height: 600px;
  width: 900px;
  background-color: white;
  border-radius: 40px;
}

.login-card__div__header {
  padding-bottom: 20px;
}

.login-card__div__right {
  padding-bottom: 20px;
}

.login-card__div__form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.login-card__div__form__btn {
  width: 200px;
  height: 35px;
  border-radius: 30px;
  border: none;
  color: white;
  background-color: #2b54c4;
  text-align: center;
  opacity: 1;
  cursor: pointer;
  transition: 0.5s;
  margin-top: 15px;
}
.login-card__div__form__btn:hover {
  opacity: 0.7;
  width: 260px;
}

.login-card__div__form__btn span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
  font-size: 16px;
}

.login-card__div__form__btn span:after {
  content: "\00bb";
  font-size: 30px;
  position: absolute;
  opacity: 0;

  bottom: -8px;
  right: -15px;
  transition: 0.5s;
}

.login-card__div__form__btn:hover span {
  padding-right: 25px;
}

.login-card__div__form__btn:hover span:after {
  opacity: 1;
  right: 0;
}
.login-card__div__form__input {
  width: 270px;
  height: 80px;
}
.login-card__div__img {
  border-radius: 10px;
}
.select-button {
  max-width: 300px;
}

.input-file-button {
  margin-top: 40px;
  width: 200px;
  text-align: center;
  border-radius: 20px;
  padding: 6px 25px;
  background-color: #dbaf5d;
  color: white;
  cursor: pointer;
  transition: 0.5s;
  opacity: 1;
}

.input-file-button:hover {
  opacity: 0.7;
  background-color: #dbb55c;
  width: 260px;
}
</style>
